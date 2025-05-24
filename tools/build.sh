#!/usr/bin/env bash

app_version=${APP_VERSION:-'0.0.0'}
app_filename='TkCalc_'
output_filename="${app_filename}_${app_version}"


python -m nuitka ./app/main.py --output-filename="$output_filename" --output-dir=${APP_OUTPUT_DIR} --remove-output
