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

## Generalizing tree height calculation ##
The code/get_TreeHeight.R script calculates tree heights from a user-specified CSV file containing tree distances and angles. Unlike the fixed-input script, it accepts the input filename as a command-line argument.  

To run the script from the project root:    

    Rscript code/get_TreeHeight.R data/trees.csv    

The script saves its output to results/trees_treeheights.csv. The output directory is created automatically if it does not already exist.   

Testing the script: 
The shell script code/run_get_TreeHeight.sh tests the generalised tree-height script using valid and invalid inputs.    

Run it from the project root using:

    bash code/run_get_TreeHeight.sh

The wrapper creates the directories required for testing and checks whether the script produces the expected outputs or errors. 

I tested additional boundary using distances of 0, 0.1, 100 and 100.1 metres. The script correctly rejected 0 and 100.1 metres while accepting 0.1 and 100 metres, consistent with the required distance range of greater than 0 and at most 100 metres.    

## Pound hill practical ##
This analysis investigates how mean plant species richness per quadrat varies among March, May and October cultivation treatments at Pound Hill. It also compares species richness with total plant abundance.  
    Input: data/pound_hill_data.csv ; data/pound_hill_meta_data.csv     
    Output:     
            results/pound_hill_plot_richness.csv - mean species richness per quadrat for each of the 12 plots  
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

This script primarily validates each row of data in the input file against rules, range, and acceptable value/entry for each variable. Accepted and rejected records are separted to different files, and using only the accepted records, the script gives a count of each oak species in the inpit data file.     

The program will create three output csv files in the results/ directory   
    - silwood_trees_clean.csv - accepted records with standardised values, sorted by ID 
    - silwood_tree_issues.csv - rejected records, their original row numbers, and the reasons for rejection 
    - oak_species_counts.csv - counts of accepted oak records grouped by species    

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

## Corrected data flow ##
Based on Assignment 2 feedback, I found that code/clean_silwood_trees.py was missing a validation check for the correct genus-species combination, and code/test_silwood_trees.py was missing a test that checks for the same. I added the checks in each script and, as advised in feedback, turned the diagnosis into a regression test by adding a focused assertion for the identified rule, checking both its validation result and its destination.

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

# In-class scripts
The following are the descriptions, commands, and input files (if applicable) needed to run several scripts in the code/ directory that were created in class. All commands should be run from the project root.  

`variables.sh`    
Demonstrates Bash positional arguments, variable assignment, interactive input, and integer arithmetic. 
Run:    bash code/variables.sh string1 string2
When prompted, enter a string (e.g., hello world), followed by two integers separated by a space (e.g., 12 8).  
Confirm that the script reports two command-line arguments, displays the correct argument values, accepts the new string, and calculates 12 + 8 = 20     

`MyExampleScript.sh`  
Demonstrates Bash variable assignment, accessing the $USER environment variable, and formatted output using printf. 
Run:    bash code/MyExampleScript.sh    
Confirm that the script prints Hello followed by the username returned by echo "$USER". 

`boilerplate.sh`  
Demonstrates a basic Bash script structure, including a shebang, comments, terminal output, and an exit status. 
Run:    bash code/boilerplate.sh   
Confirm that it prints This is a shell script! and exits successfully.   

`CheckLabel.sh`   
Demonstrates Bash conditional statements, argument validation, and exit codes.  
Run and check:

bash code/CheckLabel.sh oak       # Valid: prints "Selected species: oak"   
bash code/CheckLabel.sh birch     # Invalid: reports unknown label  
bash code/CheckLabel.sh           # Invalid: displays usage instructions    

`CountLines.sh`   
Demonstrates command-line arguments, input redirection, and line counting using wc -l.  
Run:    bash code/CountLines.sh data/trees.csv 
Compare the reported line count with wc -l < data/trees.csv. Both should match. 
Input: User-specified text/CSV file. Output: Line count printed to the terminal; no files created.  

`ConcatenateTwoFiles.sh`  
Demonstrates file concatenation using cat and output redirection (> and >>).    
Run:    
mkdir -p results    
bash code/ConcatanateTwoFiles.sh data/trees.csv data/trees.csv results/combined.csv 
Confirm that results/combined.csv contains two consecutive copies of data/trees.csv, using wc -l to verify that its line count is twice the original.   
Inputs: Two user-specified files. Output: One concatenated file, printed to the terminal and saved at the specified path.   

`tiff2_png.sh`    
Converts TIFF images in data/ to PNG format using ImageMagick.  
Run:    bash code/tiff2_png.sh 
With at least one .tif file in data/, confirm that a corresponding .png file is created in results/.    
Input: data/*.tif. Output: results/*.png.   

`loops.py`    
Demonstrates Python for and while loops, iteration over lists, and cumulative addition. 
Run:    python3 code/loops.py  
Confirm that the script prints integers 0–4, iterates through the list, calculates a final cumulative sum of 1234, and prints integers 1–100.   

`cfexercises1.py` 
Demonstrates Python functions, conditionals, sorting, iteration, and recursive and iterative factorial calculations.    
Run and check: Import the functions using python3 from the project root. Verify that foo_1(9) = 3, foo_2(3,5) = 5, foo_3(3,1,2) = [1,2,3], and all three factorial functions return 120 for input 5. Also check that foo_5(0) and foo_6(0) both return 1.   
I updated the recursive factorial function's base case to handle 0! = 1, as suggested in the practical. 

`cfexercises2.py` 
Demonstrates Python control flow using for and while loops, conditional statements, modulo operations, and break.   
Run:    python3 code/cfexercises2.py   
Confirm that all six functions execute without errors and print the expected number of hello messages:  
hello_1: 4  
hello_2: 5  
hello_3: 14 
hello_4: 5  
hello_5: 8  
hello_6: 6 (hello! followed by numbers 0–5) 

`MyExampleScript.py`  
Demonstrates defining and calling a Python function, using docstrings, and formatted output with f-strings. 
Run:    python3 code/MyExampleScript.py    
Confirm that it prints The square of 2 is 4.    

`boilerplate.py`  
Demonstrates a basic Python script structure, including a main() function, docstrings, and the if __name__ == "__main__": convention.   
Run:    python3 code/boilerplate.py    
Confirm that it prints This is a boilerplate. Importing the module should not execute main().   

`using_name.py`   
Demonstrates Python's __name__ variable and the difference between running a script directly and importing it as a module.  
Run and check:

python3 code/using_name.py

Expected: This module's name is: __main__   

cd code 
python3 -c "import using_name; print(using_name.module_name())" 
cd ..   
Expected: using_name, with no additional output during import.  

`sysargv.py`  
Demonstrates accessing command-line arguments using Python's sys.argv.  
Run:

python3 code/sysargv.py oak pine

Confirm that it prints:

Script name: code/sysargv.py    
Number of arguments: 2  
Arguments: ['oak', 'pine']  

`control_flow.py` 
Demonstrates Python conditional statements, loops, functions, default arguments, and prime-number calculations. 
Run:    python3 code/control_flow.py   
Confirm that the script runs without errors, correctly identifies 22 as even and 33 as odd, finds 5 as the largest divisor of 120, identifies 59 as prime and 60 as non-prime, and returns 25 prime numbers between 2 and 100.  

`test_control_flow.py`    
Demonstrates automated function testing using Python's doctest module.  
Run:    python3 -m doctest -v code/test_control_flow.py    
Confirm that all 3 doctests pass, including positive even and odd numbers and a negative even number. The output should report 3 passed and 0 failed.   

`observations_practice.py`    
Demonstrates reading CSV data using csv.DictReader and validating numerical counts. 
Run:    python3 code/observations_practice.py  
Confirm that the first and third observations are printed. Test parse_count() with "5", "0", "", and "-1" to verify valid, missing, and invalid counts. 
Input: data/bootcamp_observations.csv. Output: Terminal output only.    
I corrected parse_count() to compare and return integer counts rather than strings.

`test_observations_practice.py`   
Demonstrates automated testing using assertions and exception handling. 
Run:    python3 code/test_observations_practice.py 
Confirm that the script exits successfully without errors. It tests valid counts (2, 0), a missing count (""), and invalid inputs ("-1", "many", 2). Any failed test raises an error.   

