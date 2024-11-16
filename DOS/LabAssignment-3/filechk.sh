#!/bin/bash

# Check if exactly two arguments are provided
if [[ $# -ne 2 ]]; then
    echo "Usage: $0 file1 file2"
    exit 1
fi

# Assign arguments to variables
file1="$1"
file2="$2"

# Compare the contents of the two files
if cmp "$file1" "$file2" >/dev/null 2>&1; then
    echo "Files $file1 and $file2 have the same content."
    rm "$file2"
    echo "So $file2 is deleted."
else
    echo "Files $file1 and $file2 have different content."
fi

