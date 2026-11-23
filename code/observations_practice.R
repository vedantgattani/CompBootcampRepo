# Observations practice: validation, summarising and plotting
# Run from the project root:
# Rscript code/observations_practice.R

# read and validate observations
read_observations <- function(path) {

  observations <- read.csv(
    path,
    colClasses = "character",
    na.strings = "",
    check.names = FALSE
  )

  # check the required column names and order
  if (!identical(names(observations), c("site", "date", "count"))) {
    stop("Columns must be site, date, count in that order")
  }

  # every observation must have a site and date
  if (any(is.na(observations$site) | trimws(observations$site) == "")) {
    stop("Missing site")
  }

  if (any(is.na(observations$date) | trimws(observations$date) == "")) {
    stop("Missing date")
  }

  # validate non-missing counts before converting to integers
  known <- !is.na(observations$count)

  valid <- grepl("^(0|[1-9][0-9]*)$", observations$count[known])

  if (!all(valid)) {
    stop("Counts must be non-negative integers")
  }

  observations$count <- as.integer(observations$count)

  if (any(is.na(observations$count[known]))) {
    stop("Count is outside the supported integer range")
  }

  return(observations)
}

# remove duplicates and summarise by site 
summarise_observations <- function(data) {

  data <- unique(data)

  sites <- unique(data$site)

  summary <- data.frame(
    site = sites,
    total_known = rep(NA_integer_, length(sites)),
    missing_count = integer(length(sites))
  )

  for (i in seq_along(sites)) {

    counts <- data$count[data$site == sites[i]]

    summary$missing_count[i] <- sum(is.na(counts))

    # Keep NA if all observations for a site are missing
    if (!all(is.na(counts))) {
      summary$total_known[i] <- sum(counts, na.rm = TRUE)
    }
  }

  return(summary)
}

# read both datasets
ordinary <- read_observations("data/bootcamp_observations.csv")
boundary <- read_observations("data/bootcamp_observations_boundary.csv")

# combine observations from both datasets
observations <- rbind(ordinary, boundary)

#str(observations)
#print(observations)

site_summary <- summarise_observations(observations)

print(site_summary)

# check the expected results 
stopifnot(
  site_summary$total_known[site_summary$site == "A"] == 2,
  site_summary$missing_count[site_summary$site == "A"] == 1,

  site_summary$total_known[site_summary$site == "B"] == 0,
  site_summary$missing_count[site_summary$site == "B"] == 0,

  is.na(site_summary$total_known[site_summary$site == "C"]),
  site_summary$missing_count[site_summary$site == "C"] == 2,

  site_summary$total_known[site_summary$site == "D"] == 0,
  site_summary$missing_count[site_summary$site == "D"] == 0
)

cat("All summary checks passed!\n")

# check invalid input

invalid_result <- try(
  read_observations("data/bootcamp_observations_invalid.csv"),
  silent = TRUE
)

stopifnot(inherits(invalid_result, "try-error"))

cat("Invalid input correctly rejected!\n")


# create figure

dir.create("results", showWarnings = FALSE)

pdf("results/observations_by_site.pdf", width = 7, height = 5)

# plot known totals; leave the all-missing site as NA
barplot(
  site_summary$total_known,
  names.arg = site_summary$site,
  main = "Known observation totals by site",
  xlab = "Site",
  ylab = "Total known count",
  ylim = c(0, max(site_summary$total_known, na.rm = TRUE) + 1),
  col = "lightblue"
)

mtext("Site C has only missing counts (NA), not an observed zero",
      side = 1, line = 4, cex = 0.8)

dev.off()

cat("Figure saved to results/observations_by_site.pdf\n")
