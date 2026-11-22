#!/bin/bash

mkdir -p results

for filename in data/*.tif
do
    [ -f "$filename" ] || continue
    echo "Converting $filename"
    convert "$filename" "results/$(basename "$filename" .tif).png"
done