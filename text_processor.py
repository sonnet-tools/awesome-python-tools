#!/usr/bin/env python3
"""
Text Processor - Common text processing utilities
"""
import re
import sys
import argparse

def count_words(text):
    """Count words in text."""
    words = re.findall(r'\w+', text.lower())
    return len(words)

def count_lines(text):
    """Count lines in text."""
    return len(text.splitlines())

def remove_duplicates(text):
    """Remove duplicate lines from text."""
    lines = text.splitlines()
    seen = set()
    result = []
    
    for line in lines:
        if line not in seen:
            seen.add(line)
            result.append(line)
    
    return '\n'.join(result)

def extract_emails(text):
    """Extract email addresses from text."""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

def process_file(file_path, operation):
    """Process a text file with specified operation."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return
    
    if operation == 'words':
        print(f"Word count: {count_words(content)}")
    elif operation == 'lines':
        print(f"Line count: {count_lines(content)}")
    elif operation == 'dedup':
        print(remove_duplicates(content))
    elif operation == 'emails':
        emails = extract_emails(content)
        if emails:
            print("Found emails:")
            for email in emails:
                print(f"  {email}")
        else:
            print("No email addresses found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text processing utilities")
    parser.add_argument("file", help="Input text file")
    parser.add_argument("operation", choices=['words', 'lines', 'dedup', 'emails'],
                       help="Operation to perform")
    
    args = parser.parse_args()
    process_file(args.file, args.operation)
