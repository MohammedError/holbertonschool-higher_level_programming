#!/usr/bin/env python3
"""Task 4: Extending Dynamic Data Display to Include SQLite in Flask"""
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def create_database():
    """Create and populate the SQLite database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES (1, 'Laptop', 'Electronics', 799.99)
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()


def read_json():
    """Read and parse data from the JSON file."""
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv():
    """Read and parse data from the CSV file."""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except (FileNotFoundError, KeyError, ValueError):
        return []
    return products


def read_sql():
    """Read data from the SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
    except sqlite3.Error:
        return []
    return products


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQL based on source query parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id', None)
    error = None
    product_list = []

    if source == 'json':
        product_list = read_json()
    elif source == 'csv':
        product_list = read_csv()
    elif source == 'sql':
        product_list = read_sql()
    else:
        error = "Wrong source"

    if error is None and product_id is not None:
        try:
            product_id = int(product_id)
            filtered = [p for p in product_list if int(p.get('id', -1)) == product_id]
            if filtered:
                product_list = filtered
            else:
                error = "Product not found"
                product_list = []
        except ValueError:
            error = "Product not found"
            product_list = []

    return render_template('product_display.html', products=product_list, error=error)


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
