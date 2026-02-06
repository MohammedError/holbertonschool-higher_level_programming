#!/usr/bin/env python3
"""
Task 2: Converting CSV Data to JSON Format
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it to data.json.

    Args:
        csv_filename (str): The name of the CSV file to read.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
