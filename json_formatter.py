#!/usr/bin/env python3
"""
JSON Formatter - Pretty-print and validate JSON files
"""
import json
import sys
import argparse

def format_json(input_file, output_file=None, indent=2):
    """Format JSON file with proper indentation."""
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        formatted = json.dumps(data, indent=indent, sort_keys=True, ensure_ascii=False)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(formatted)
            print(f"Formatted JSON written to: {output_file}")
        else:
            print(formatted)
            
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {input_file}")
        print(f"Details: {e}")
        return False
    except FileNotFoundError:
        print(f"Error: File {input_file} not found")
        return False
    
    return True

def validate_json(file_path):
    """Validate JSON file structure."""
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        print(f"✓ Valid JSON: {file_path}")
        return True
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON: {file_path}")
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="JSON formatter and validator")
    parser.add_argument("input", help="Input JSON file")
    parser.add_argument("-o", "--output", help="Output file (default: stdout)")
    parser.add_argument("-i", "--indent", type=int, default=2, help="Indentation level")
    parser.add_argument("-v", "--validate", action="store_true", help="Validate only")
    
    args = parser.parse_args()
    
    if args.validate:
        validate_json(args.input)
    else:
        format_json(args.input, args.output, args.indent)
