#!/usr/bin/python3

import argparse
import sys

"""
Implementing the parser for named args
"""
parser=argparse.ArgumentParser(
    prog="File Name Generator", 
    description="This is help to create file name from given text and remove all the unwanted, unsupported characters from the file name"
    )

parser.add_argument("name", help="The string for the file name. The output string will strip all the unsuppored characters from the string")
parser.add_argument("--extention", "-e", help="The type of the file. Eg: pdf, jpg, etc.")
args = parser.parse_args()

"""
Function to generate a valid file name from entered string:wq
"""
if args.name:
    input_text = args.name
    unwanted_symbols = "!@#$%^&*(),.:;'|`'~-+=/><?\\\n\t "
    output_text = "".join("_" if char in unwanted_symbols else char for char in input_text )
    output_text += f".{args.extention}" if args.extention else ''
    print(f"Generated file name: {output_text}")
else:
    print(f"Name is not provided. Please provide the name")