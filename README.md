# Computational Bootcamp Repo 2026
This repository contains all files used and created during the 2026 computational bootcamp at Imperial College London, Silwood Park.    
Important files/directories: README.md, code/, and data/    

## Project structure ##
code/ contains all scripts cloned from MulQuaBio repo or created for assignments.   
data/ contains all files used for assignments/practicals through the course.    

# Week 1 Assignment notes

## Important directories ##
data/fasta contains all data files used for FASTA exercise. 
data/temperature contains all data files used to test csvtospace.sh 
data/tab-example.tsv was used to test tabtocsv.sh   

code/unixPrac1.txt contains both code and text explaining what it does for FASTA exercise.  
code/tabtocsv.sh contains script that converts space delimited files to comma delimited files.  
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