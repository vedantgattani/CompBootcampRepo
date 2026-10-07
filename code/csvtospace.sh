#!/bin/bash
# Author: vg726@ic.ac.uk
# Script: csvtospace.sh
# Desc: substitute the commas in the files with spaces
#       saves the output into a .txt file
# Arguments: 1-> comma delimited file
# Date: Oct 2026

if [[ "$#" -ne 1 ]]; then
    echo "Error: provide one input file only" >&2
    exit 1
fi

if [[ ! -r "$1" ]]; then
    printf "Error: provide a readable/valid file" >&2
    exit 2
fi

filename=$(basename "$1")

echo "Creating a space delimited version of $1 ..."

cat $1 | tr "\t" "," > "../results/$filename.txt"

echo "Done!"

exit 0