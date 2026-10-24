#!/bin/bash
# Author: vg726@ic.ac.uk
# Script: tabtocsv.sh
# Desc: substitute the tabs in the files with commas
#       saves the output into a .csv file
# Arguments: 1-> tab delimited file
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

echo "Creating a comma delimited version of $1 ..."

# make results directory if not already existing
mkdir -p

if ! tr '\t' ',' < "$1" > "results/$filename.csv"; then
    printf "Error: conversion failed\n" >&2
    exit 3
fi

echo "Done!"

exit 0