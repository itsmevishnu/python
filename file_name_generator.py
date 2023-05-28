#!/usr/bin/python3

import sys

"""
Function to generate a valid file name from entered string:wq
"""
if len(sys.argv) !=2:
    print(f"File name is not provided. Please provide the file name")
else:
    input_text = sys.argv[1]
    output_text = input_text.replace(' ', '_').replace('\\', '_').replace('-','_')
    print(f"Generated file name: {output_text}")
