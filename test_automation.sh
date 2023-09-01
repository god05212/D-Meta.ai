#!/bin/bash

# cut_image.py 실행
python cut_image.py input_image.png 3 4 output_prefix

# merge_image.py 실행
python merge_image.py output_prefix 3 4 merged_image.png
