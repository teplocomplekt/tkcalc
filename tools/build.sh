#!/usr/bin/env bash

set -e

echo "Using Windows Python: $WINE_PYTHON"



app_version=${APP_VERSION:-'0.0.0'}
app_filename='TkCalc_'
output_filename="${app_filename}_${app_version}"


#python3 -m nuitka ./app/main.py --output-filename="$output_filename" --output-dir=${APP_OUTPUT_DIR} --remove-output

wine64 "$WINE_PYTHON" -m nuitka \
    ./app/main.py \
    --output-filename="$output_filename" \
    --output-dir="${APP_OUTPUT_DIR}" \
    --remove-output \
    --onefile \
    --windows-console-mode=disable \
    --enable-plugin=tk-inter