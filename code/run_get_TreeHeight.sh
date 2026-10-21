#!/bin/bash

## test the generalized tree height R script ##

# run R script with original dataset
Rscript code/get_TreeHeight.R data/trees.csv

# check number of lines in the output (expected: 120 data rows + 1 header)
wc -l results/trees_treeheights.csv

# display output header and first few records to confirm
head results/trees_treeheights.csv

# create a small test csv in sandbox
echo "Species,Distance.m,Angle.degrees" > sandbox/test_trees.csv
echo "Test species,8,45" >> sandbox/test_trees.csv  # using height 8 and angle 45

# run the script with the small test csv
Rscript code/get_TreeHeight.R sandbox/test_trees.csv

# display results
cat results/test_trees_treeheights.csv

# run the small dataset again
Rscript code/get_TreeHeight.R sandbox/test_trees.csv

# check number of lines remains the same (2)
wc -l results/test_trees_treeheights.csv

# display output header shows the same stuff
head results/test_trees_treeheights.csv
