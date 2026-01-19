#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_val = None
    best_key = None
    for k, v in a_dictionary.items():
        if max_val is None or v > max_val:
            max_val = v
            best_key = k
    return best_key
