# buggy_file_processing.py
# Contains intentional bugs for AI code testing

import json
import csv
import os


def read_json_config(filepath):
    """Read a JSON config file and return as dict."""
    f = open(filepath, 'r')  # Bug: file handle never closed (no context manager)
    data = json.load(f)
    return data


def write_csv(filepath, rows):
    """Write rows to a CSV file."""
    with open(filepath, 'w') as f:  # Bug: missing newline='' on Windows causes extra blank rows
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)


def merge_json_files(file_list):
    """Merge multiple JSON files into one dict."""
    merged = {}
    for filepath in file_list:
        with open(filepath, 'r') as f:
            data = json.load(f)
            merged.update(data)  # Bug: silently overwrites duplicate keys from earlier files
    return merged


def count_lines(filepath):
    """Count non-empty lines in a file."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    count = 0
    for line in lines:
        if line != "\n":  # Bug: doesn't handle lines with only whitespace
            count += 1
    return count  # Bug: counts lines with \n at end as non-empty even if just spaces


def safe_delete(filepath):
    """Delete a file if it exists."""
    if os.path.exists(filepath):
        os.remove(filepath)
        return True
    return False
    # Bug: race condition - file could be deleted between exists check and remove


def read_file_lines(filepath, start=0, end=None):
    """Read specific lines from a file."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    if end is None:
        end = len(lines)
    return lines[start:end]  # Bug: doesn't strip newlines, caller gets trailing \n


def parse_key_value_file(filepath):
    """Parse a file with key=value pairs."""
    result = {}
    with open(filepath, 'r') as f:
        for line in f:
            if '=' in line:
                key, value = line.split('=')  # Bug: fails if value contains '=' sign
                result[key.strip()] = value.strip()
    return result


def backup_file(filepath):
    """Create a backup of a file."""
    backup_path = filepath + ".bak"
    with open(filepath, 'r') as src:
        content = src.read()
    with open(backup_path, 'w') as dst:
        dst.write(content)
    return backup_path
    # Bug: only works with text files, binary files will be corrupted


def find_files_by_extension(directory, extension):
    """Find all files with a given extension in a directory."""
    result = []
    for item in os.listdir(directory):  # Bug: not recursive, misses subdirectories
        if item.endswith(extension):
            result.append(item)  # Bug: returns filenames only, not full paths
    return result


def tail_file(filepath, n=10):
    """Return last n lines of a file."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return lines[-n:]  # Bug: if n > len(lines), returns all lines (not really a bug)
    # Real bug: reads entire file into memory, fails on huge files
