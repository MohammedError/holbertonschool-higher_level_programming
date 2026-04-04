#!/usr/bin/env python3
"""Task 3: Displaying Data from JSON or CSV Files in Flask"""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


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


@app.route('/products')
def products():
    """Display products from JSON or CSV based on source query parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id', None)
    error = None
    product_list = []

    if source == 'json':
        product_list = read_json()
    elif source == 'csv':
        product_list = read_csv()
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
    app.run(debug=True, port=5000)
