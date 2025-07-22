#!/usr/bin/env python3
"""
File Analyzer - Analyze file types and sizes in directories
"""
import os
import sys
from collections import defaultdict

def analyze_directory(path):
    """Analyze files in a directory and return statistics."""
    if not os.path.exists(path):
        print(f"Error: Directory '{path}' does not exist")
        return
    
    file_stats = defaultdict(list)
    total_size = 0
    
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                ext = os.path.splitext(file)[1].lower()
                file_stats[ext].append((file, size))
                total_size += size
            except OSError:
                continue
    
    print(f"Directory Analysis: {path}")
    print(f"Total files: {sum(len(files) for files in file_stats.values())}")
    print(f"Total size: {total_size / (1024*1024):.2f} MB")
    print("\nFile types:")
    
    for ext, files in sorted(file_stats.items()):
        count = len(files)
        size = sum(f[1] for f in files)
        print(f"  {ext or '(no extension)'}: {count} files, {size / 1024:.2f} KB")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_analyzer.py <directory_path>")
        sys.exit(1)
    
    analyze_directory(sys.argv[1])
