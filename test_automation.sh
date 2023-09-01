#!/bin/bash

# Run cut_image.py
python cut_image.py input_image.png 3 4 output_prefix

# Run merge_image.py
python merge_image.py output_prefix 3 4 merged_image.png
