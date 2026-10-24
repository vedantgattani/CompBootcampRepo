# Computational Bootcamp Repo 2026
This repository contains all files used and created during the 2026 computational bootcamp at Imperial College London, Silwood Park.    
Important files/directories: README.md, code/, and data/    

## Project structure ##
code/ contains all scripts cloned from MulQuaBio repo or created for assignments.   
data/ contains all files used for assignments/practicals through the course.    

# Week 3 Assignment notes     

## Overview ##
This practical uses R to calculate tree heights from a dataset containing 120 tree measurements. The TreeHeight() function applies a calculation to every record, and the estimated heights are added as a fourth column next to the original measurements. 
    Input: data/trees.csv - this is the original dataset with columns Species, Distance.m, and Angle.degrees   
    Output: results/TreeHts.csv - this contains the original three columns plus the calculated height_m column. 

## Running the script ##
From the project root directory, run:

    Rscript code/TreeHeight.R   

OR, run the following from an R session:    

    source("code/TreeHeight.R")

## Validation ##
Before calculating heights, the script checks:  
    - all three required columns are present    
    - distance and angle measurements are numeric, finite, and within range 
If any of the checks fails, the script stops and returns an error message.  

## Manual verification ##
I manually checked the TreeHeight() function by feeding it a distance of 8m and angle of 45. The function responded with 8, which is the correct height.    

Additionally, I also checked the first record from data/trees.csv:  
    Species: Populus tremula     
    Distance: 31.67 
    Angle: 41.28    
    Calculated height: 27.80       
And it matched the height calculated by physcially using the formula.    

Finally, I confirmed there were 120 data rows in the output file by using nrow(), and rerunning the script replaced outputs without appending suplicate rows.   

## Pound hill practical ##
This analysis investigates how mean plant species richness per quadrat varies among March, May and October cultivation treatments at Pound Hill. It also compares species richness with total plant abundance.  
    Input: data/pound_hill_data.csv ; data/pound_hill_meta_data.csv 
    Output: results/pound_hill_plot_richness.csv - mean species richness per quadrat for each of the 12 plots  
            results/pound_hill_plot_richness.pdf - figure comparing plot-level species richness across cultivation treatments    
            results/pound_hill_plot_abundance.pdf - figure comparing plot-level abundance across treatments 

From the project root, run: 

    Rscript code/pound_hill_analysis.R

The script uses the reshape2, dplyr and ggplot2 packages.
To verify reproducibility, I ran the script twice from the project root and confirmed that the output csv and pdf files are recreated successfully without changing the original data.  

## AI use ##
ChatGPT; Oct 20: Learn what commandArgs(trailingOnly = TRUE) does, before using it for get_TreeHeight.R 
ChatGPT; Oct 20: Learned how to remove .csv from file names using sub(), and use paste0() to join two strings together, so file name can be attached with _treeheights. 
ChatGPT; Oct 20: Found file.path() that specifically joins directory and file name, used in get_TreeHeight.R    

## Additional utilties ##
sub() - used to to remove .csv from file names. 
paste0() used to join two strings together. 
file.path() used to join directory and any file name together.  

# Week 2 Assignment notes

## Pseudocode for practical (validating tree-survey records)
INPUT: tree observations at silwood, inlcuding record ID, location, genus, species, distance and angle (import silwood_trees_raw.csv)   
    1. Read csv file    
    2. Create empty lists for accepted records and rejected records      
    3. For each tree:   
            - remove whitespace      
            - check that ID is valid and not duplicated      
            - check that location is valid      
            - check that genus and species are recognized          
            - check that disance and angles are valid numbers and within range        
        If all checks pass, add cleaned record to accepted list.    
        Otherwise, record all reasons for rejection.    
    4. Sort accepted records by ID  
    5. Count each oak species among accepted records    
    6. Write three csv files    
OUTPUT: silwood_trees_clean.csv (accepted records with standardised values, sorted by ID); silwood_tree_issues.csv (rejected records, their original row numbers, and the reasons for rejection) ; oak_species_counts.csv (counts of accepted oak records grouped by species)   

## Running the program ##
From the project root directory, run:   

    python3 code/clean_silwood_trees.py 

The program will create three output csv files in the results/ directory        

To run the test script: 

    python 3 code/test_silwood_trees.py

The test script will run hypothetical data rows to test the following:  
    - valid records with inconsistent capitalization and space
    - missing and unrecognized values       
    - multiple errors within a single record        
    - duplicate record IDs and reuse of IDs from rejected records       
    - invalid, non-finite, and out-of-range measurements        
    - valid numeric boundary values     
    - seperation and sorting of accepted and rejected records       
    - oak species counting, near matches, and datasets containing no oaks           

## AI use ##
ChatGPT; Oct 13: Using elif conditions  
ChatGPT; Oct 13: Learnt about .isdigits() while finding a way to test if characters are digits - used in clean_silwood_trees.py 
ChatGPT; Oct 13: Used to fix indentation problem in script. "Unexpected indentation" and "Expected expression" messages on script.  
ChatGPT; Oct 14: Used to explore math package, using functions such as math.isfinite() - used in def validate_record().  
ChatGPT; Oct 14: Used to fix indentation and formatting again - constant red and yellow squigly lines on script. In the process, model also provided unsolicited advice on typos that were eventually fixed.    
ChatGPT; Oct 15: Used to confirm the need, and correct use of .join(), used in def process_records().   
ChatGPT; Oct 15: Used to find a way to sort records by record_id - suggested .sort() with key=lambda... Used in def process_records().  
ChatGPT; Oct 15: Used to find a way to sort keys alphabetically, using sorted().    
ChatGPT; Oct 16: Used to understand error messages in test_silwood_trees.py - backtracked to fixing issues with clean_silwood_trees.py  

## Additional utilties ##
.sort(key=lambda...) found through ChatGPT (Oct 15). Used in def process_records() function in clean_silwood_trees.py   

# Week 1 Assignment notes

## Important directories ##
data/fasta contains all data files used for FASTA exercise. 
data/temperature contains all data files used to test csvtospace.sh 
data/tab-example.tsv was used to test tabtocsv.sh   

code/unixPrac1.txt contains both code and text explaining what it does for FASTA exercise.  
code/tabtocsv.sh contains script that converts tab delimited files to comma delimited files.  
code/csvtospace.sh contais script that converts comma delimited files to space delimited files.

## AI use ##
ChatGPT; Oct 5: Used to learn how to clone files from git, used to clone MulQuaBio to use FASTA files.  
ChatGPT; Oct 5: Used to learn what wc -l does, and why it matters for newline.  
ChatGPT; Oct 6: Used to learn usage of bs -l, and whether it can be used in the case of calculating AT/GC ratio.    
ChatGPT; Oct 7: Used to check loop that allows only one input file on tabtocsv.sh   
ChatGPT; Oct 7: Used to learn difference between append with >> and overwrite with > to avoid duplication when tabtocsv.sh is run twice.    
ChatGPT; Oct 7: Used to learn difference between tr and tr -s   
ChatGPT; Oct 7: Used to understand standard error using >&2  
ChatGPT; Oct 9: Used to learn difference between '[ATGC]' and 'ATGC', tried both on FASTA question 3 and 4. 

## Additional utilities ##
echo "scale = x;" | bc found on stack overflow. Tried on basic arithmetic first, then used for final code.  

# learning README 
My Git practice repository   
I am trying a new naughty thing on this experimental branch 