#!/bin/bash
# Author: vg726@ic.ac.uk
# Script: tabtocsv.sh
# Desc: substitute the tabs in the files with commas
#       saves the output into a .csv file
# Arguments: 1-> tab delimited file
# Date: Oct 2026

if [[ "$#" -ne 1 ]]; then
    echo "provide one input file only" >&2
    exit 1
fi

if [[ ! -r "$1" ]]; then
    printf "provide a readable/valid file" >&2
    exit 2
fi

filename=$(basename "$1")

echo "Creating a comma delimited version of $1 ..."

cat $1 | tr "\t" "," > "../results/$filename.csv"

echo "Done!"

exit 0