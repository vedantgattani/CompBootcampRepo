
# wrangle the Pound Hill dataset using tidyr.
# run from the coursework project root:
# rscript code/data_wrang_tidy.R

# load the data 
MyData <- as.matrix(read.csv("data/pound_hill_data.csv", header = FALSE))

MyMetaData <- read.csv("data/pound_hill_meta_data.csv",
                       header = TRUE, sep = ";")

# transpose and clean the data
MyData <- t(MyData)

# Blank species counts represent observed absences in this dataset.
MyData[MyData == ""] <- 0

TempData <- as.data.frame(MyData[-1, ], stringsAsFactors = FALSE)
colnames(TempData) <- MyData[1, ]
rownames(TempData) <- NULL

# convert from wide to long format using tidyr
library(dplyr)
library(tidyr)

MyWrangledData <- TempData |>
  tidyr::pivot_longer(
    cols = -c(Cultivation, Block, Plot, Quadrat),
    names_to = "Species",
    values_to = "Count"
  )

# convert columns to appropriate data types
MyWrangledData$Cultivation <- as.factor(MyWrangledData$Cultivation)
MyWrangledData$Block <- as.factor(MyWrangledData$Block)
MyWrangledData$Plot <- as.factor(MyWrangledData$Plot)
MyWrangledData$Quadrat <- as.factor(MyWrangledData$Quadrat)
MyWrangledData$Count <- as.integer(MyWrangledData$Count)

# check the resulting dataset 
str(MyWrangledData)
head(MyWrangledData)
dim(MyWrangledData)

# save the long-format data 
dir.create("results", showWarnings = FALSE)

write.csv(MyWrangledData,
          "results/pound_hill_long_tidy.csv",
          row.names = FALSE)
