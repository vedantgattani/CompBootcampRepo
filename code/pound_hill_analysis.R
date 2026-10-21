# Wrangle the Pound Hill dataset.
# Run from the coursework project root with:
# Rscript code/pounc_hill_analysis.R

# Load the data ----------------------------------------------------------
# The first rows describe the sampling design, so do not use one as a header yet.
MyData <- as.matrix(read.csv("data/pound_hill_data.csv", header = FALSE))

# The metadata file does have a header and uses semicolons as separators.
MyMetaData <- read.csv("data/pound_hill_meta_data.csv", header = TRUE, sep = ";")

# Inspect the data -------------------------------------------------------
# check dimensions
#dim(MyData)
#dim(MyMetaData)

# check column type and structure
#str(MyData)
#str(MyMetaData)

# view first six rows
#head(MyData)
#head(MyMetaData)

# Transpose so species become columns and sampled quadrats become rows.
MyData <- t(MyData) 
#head(MyData)
#dim(MyData)

# For this dataset, we have been told that blanks are observed absences.
# That knowledge is what allows us to record them as zero rather than NA.
MyData[MyData == ""] <- 0

# Convert the raw matrix to a data frame --------------------------------

TempData <- as.data.frame(MyData[-1, ], stringsAsFactors = FALSE)
colnames(TempData) <- MyData[1, ]
rownames(TempData) <- NULL

#print(dim(TempData))
#print(head(TempData))
#print(names(TempData))

# Convert from wide to long form ----------------------------------------
# This script keeps the older reshape2 route because it is still common in
# ecological code. For new work, the chapter introduces tidyr::pivot_longer().
library(reshape2)

MyWrangledData <- melt(
  TempData,
  id = c("Cultivation", "Block", "Plot", "Quadrat"),
  variable.name = "Species",
  value.name = "Count"
)

MyWrangledData[, "Cultivation"] <- as.factor(MyWrangledData[, "Cultivation"])
MyWrangledData[, "Block"] <- as.factor(MyWrangledData[, "Block"])
MyWrangledData[, "Plot"] <- as.factor(MyWrangledData[, "Plot"])
MyWrangledData[, "Quadrat"] <- as.factor(MyWrangledData[, "Quadrat"])
MyWrangledData[, "Count"] <- as.integer(MyWrangledData[, "Count"])

# check if species counts are numeric
is.numeric(MyWrangledData$Count)

# check for missing counts
sum(is.na(MyWrangledData$Count))

# check for negative counts
sum(MyWrangledData$Count < 0)

# count distinct species in dataset
number_species <- length(unique(MyWrangledData$Species))
#print(number_species)

# identify distinct quadrats using all four columns
unique_quadrats <- unique(MyWrangledData[, c("Cultivation", "Block", "Plot", "Quadrat")])

# count all quadrats
number_quadrats <- nrow(unique_quadrats)
#print(number_quadrats)

# identify distinct plots (by leaving out quadrat)
unique_plots <- unique(MyWrangledData[, c("Cultivation", "Block", "Plot")])

# count all plots
number_plots <- nrow(unique_plots)
#print(number_plots)

## calculaitng species richness ##
library(dplyr)

QuadratRichness <- MyWrangledData %>%
    group_by(Cultivation, Block, Plot, Quadrat) %>%
    summarise(Richness = sum(Count > 0)) %>% #sum up all occurances of when species count is >0
    ungroup()

#print(QuadratRichness)

## calculate mean species richness for each plot ##

PlotRichness <- QuadratRichness %>%
    group_by(Cultivation, Block, Plot) %>% # leave out qudrat when grouping
    summarise(MeanRichness = mean(Richness)) %>%
    ungroup()

#print(PlotRichness)

# save plot-level richness tables
write.csv(PlotRichness, "results/pound_hill_plot_richness.csv", row.names = FALSE)

## create species richness plot ##
library(ggplot2)

pdf("results/observations_by_site.pdf")
print(RichnessPlot <- ggplot(PlotRichness, aes(x = Cultivation, y = MeanRichness)) +
    geom_point() +
    labs(title = "Plant species richness by cultivation treatment",
            x = "Cultivation treatment",
            y = "Mean species richness per quadrat") +
    theme_classic())
dev.off()

## interpretation of plot ##

# may cultivation seems to have the higher mean species richness epr quadrat
# but richness varies among plots within each treatment and ranges considerably overlap.
# the figure alone cannot establish that cultivation timing is what caused such differences, 
# other environmental factors and design choices will need to be factored in to get a better picture. 

## calculating total abundance for each quadrat ##

QuadratAbundance <- MyWrangledData %>%
    group_by(Cultivation, Block, Plot, Quadrat) %>%
    summarise(Abundance = sum(Count)) %>% # same as richness, except with just Count
    ungroup()

# calculating mean abundance for each plot 

PlotAbundance <- QuadratAbundance %>%
    group_by(Cultivation, Block, Plot) %>% 
    summarise(MeanAbundance = mean(Abundance)) %>% # again same as richness
    ungroup()

# create similar plot for abundance to compare with richness 

AbundancePlot <- ggplot(PlotAbundance, aes(x = Cultivation, y = MeanAbundance)) +
    geom_point() +
    labs(title = "Plant abundance by cultivation treatment",
            x = "Cultivation treatment",
            y = "Mean plant abundance per quadrat") +
    theme_classic()

# save the figure in results
pdf("results/pound_hill_plot_abundance.pdf")
print(AbundancePlot)
dev.off()

## interpretation and comparison to richness ##

# while may cultivation seems to have the highest typical species richness,
# october has the highest typical plant abundance. 
# this suggests that treatments with more individual plants do not necessarily 
# support a greater number of species.