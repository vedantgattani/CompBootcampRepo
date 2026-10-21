# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"

# command-line arguments
args <- commandArgs(trailingOnly = TRUE)

# check that only one input file was provided
if (length(args) != 1) {
    stop("Error: provide exactly one csv file path")
}

# store input file
input_file <- args[1]

# function
TreeHeight <- function(degrees, distance) {
    radians <- degrees * pi / 180
    height <- distance * tan(radians)
    return (height)
}

# read the supplied csv
trees <- read.csv(input_file) 

# glance at the column names and first few rows
print(names(trees))
print(head(trees))

# check that all three required columns are present
required_columns <- c("Species", "Distance.m", "Angle.degrees")

if (!all(required_columns %in% names(trees))) {
    stop("Error: input file is missing required columns")
}

# check if distance are numeric
if (!is.numeric(trees$Distance.m)) {
    stop("Error: Distance.m must contain numeric values.")
}

# check if angles are numeric
if (!is.numeric(trees$Angle.degrees)) {
    stop("Error: Angle.degrees must contain numeric values.")
}

# check if all measurements are finite
if (!all(is.finite(trees$Distance.m))) {
    stop("Error: Distance.m contains missing or non-finite values.")
}
if (!all(is.finite(trees$Angle.degrees))) {
    stop("Error: Angle.degrees contains missing or non-finite values.")
}

# check that distances are within range
if (any(trees$Distance.m <= 0 | trees$Distance.m > 100)) {
    stop("Error: Distance.m must be >= 0 and < 100.")
}

# check that angles are within range
if (any(trees$Angle.degrees <= 0 | trees$Angle.degrees >= 90)) {
    stop("Error: Angle.degrees must be > 0 and < 90.")
}

# make a new column that applies the TreeHeight function
trees$height_m <- TreeHeight(
    trees$Angle.degrees,
    trees$Distance.m
)

# get the input filename without its directory
file_name <- basename(input_file)

# remove the .csv extension
file_name <- sub("\\.csv$", "", file_name)

# create the output filename
output_name <- paste0(file_name, "_treeheights.csv")

# create the full output path
output_file <- file.path("results", output_name)

# export a file with tree height values
write.csv(trees, output_file, row.names = FALSE)