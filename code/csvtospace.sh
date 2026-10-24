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

# make results directory if not already existing
mkdir -p

if ! tr ',' ' ' < "$1" > "results/$filename.txt"; then
    printf "Error: conversion failed\n" >&2
    exit 3
fi

echo "Done!"

exit 0