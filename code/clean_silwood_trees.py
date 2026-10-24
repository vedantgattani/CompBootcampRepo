#!/usr/bin/env python3
"""Validate and clean the synthetic Silwood tree survey."""

from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "silwood_trees_raw.csv"
RESULTS_DIR = PROJECT_ROOT / "results"

INPUT_FIELDS = [
    "record_id",
    "location",
    "genus",
    "species",
    "distance_m",
    "angle_degrees",
]
ISSUE_FIELDS = ["source_row", "record_id", "reasons"]
OAK_COUNT_FIELDS = ["species", "count"]


def load_records(path: Path = INPUT_PATH) -> list[dict[str, str]]:
    """Read the survey and check its column names."""
    with path.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != INPUT_FIELDS:
            raise ValueError(
                f"Expected columns {INPUT_FIELDS}, found {reader.fieldnames}"
            )
        return list(reader)

def validate_record(
    row: dict[str, str],
    source_row: int,
    accepted_ids: set[str],
) -> tuple[dict[str, str] | None, list[str]]:
    """Clean one record, or return the reasons it cannot be used."""
    # empty list to store reasons for rejection
    reasons = []

    # clean record ID
    record_id = row["record_id"].strip()

    ## check if record ID is valid

    # if ID is empty
    if record_id == "":
        reasons.append("missing record_id")

    # if length is anything but 5
    elif len(record_id) != 5:
        reasons.append("invalid record_id")

    # if ID doesn't start with ST
    elif record_id.startswith("ST") == False:
        reasons.append("invalid record_id")

    # if final three places are digits
    elif record_id[2:].isdigit() == False:
        reasons.append("invalid record_id")

    # if ID has already been accepted
    elif record_id in accepted_ids:
        reasons.append("duplicate record_id")

    # clean location and turn everything to lowercase
    location = row["location"].strip().lower()

    if location == "":
        reasons.append("missing location")

    # fix capitalisation for each valid location
    elif location == "silwood bottom":
        location = "Silwood Bottom"
    elif location == "nash's field":
        location = "Nash's Field"
    elif location == "manor house":
        location = "Manor House"
    elif location == "reactor wood":
        location = "Reactor Wood"

    # if nothing matches the above names
    else:
        reasons.append("invalid location")

    # clean genus and species, turn everything lowercase
    genus = row["genus"].strip().lower()
    species = row["species"].strip().lower()

    ## validate genus names + fix capitalisation
    if genus == "":
        reasons.append("missing genus")

    elif genus == "quercus":
        genus = "Quercus"
    elif genus == "acer":
        genus = "Acer"
    elif genus == "betula":
        genus = "Betula"
    elif genus == "fagus":
        genus = "Fagus"
    elif genus == "fraxinus":
        genus = "Fraxinus"

    # if nothing matches above names
    else:
        reasons.append("invalid genus")

    ## validate species names
    if species == "":
        reasons.append("missing species")

    elif species == "robur":
        species = "robur"
    elif species == "petraea":
        species = "petraea"
    elif species == "pseudoplatanus":
        species = "pseudoplatanus"
    elif species == "pendula":
        species = "pendula"
    elif species == "sylvatica":
        species = "sylvatica"
    elif species == "excelsior":
        species = "excelsior"

    # if nothing matches above names
    else:
        reasons.append("invalid species")
    
    ## check genus and species combination
    if "missing genus" not in reasons:
        if "invalid genus" not in reasons:
            if "missing species" not in reasons:
                if "invalid species" not in reasons:

                    valid_combination = False

                    if genus == "Quercus":
                        if species == "robur":
                            valid_combination = True
                        elif species == "petraea":
                            valid_combination = True

                    elif genus == "Acer":
                        if species == "pseudoplatanus":
                            valid_combination = True

                    elif genus == "Betula":
                        if species == "pendula":
                            valid_combination = True

                    elif genus == "Fagus":
                        if species == "sylvatica":
                            valid_combination = True

                    elif genus == "Fraxinus":
                        if species == "excelsior":
                            valid_combination = True

                    if valid_combination == False:
                        reasons.append("invalid genus/species combination")
    

    ## clean and validate distance
    # remove spaces
    distance = row["distance_m"].strip()

    # validate distance according to given range
    if distance == "":
        reasons.append("missing distance_m")

    else:
        try:
            distance = float(distance)  # try to convert distance to numeric

            # if distance is not a number
            if math.isfinite(distance) == False:
                reasons.append("invalid distance_m")

            # if distance is below range
            elif distance <= 0:
                reasons.append("distance_m out of range")

            # if distance is above range
            elif distance > 100:
                reasons.append("distance_m out of range")

        # attempt to convert distance to numeric, note reason if failed
        except ValueError:
            reasons.append("invalid distance_m")

    ## clean and validate angle
    # remove space
    angle = row["angle_degrees"].strip()

    if angle == "":
        reasons.append("missing angle_degrees")

    else:
        try:
            angle = float(angle) # try converting to numeric

            # if angel is not a number
            if math.isfinite(angle) == False:
                reasons.append("invalid angle_degrees")

            # if angle is below range
            elif angle <= 0:
                reasons.append("angle_degrees out of range")

            # if angle is above range
            elif angle >= 90:
                reasons.append('angle_degrees out of range')

        # if doesn't convert t numeric, show reason
        except ValueError:
            reasons.append("invalid angle_degrees")
    
    # if number of items in reasons is >0, at least one problem was found
    # so return None and the reasons
    if len(reasons) > 0:
        return None, reasons
    
    # create dictionary with all cleaned fields
    cleaned_record = {
        "record_id": record_id,
        "location": location,
        "genus": genus,
        "species": species,
        "distance_m": str(distance), # since previously converted to numbers
        "angle_degrees": str(angle) # since previously converted to numbers
    }
    # add accepted ID to set every time there's no issue
    accepted_ids.add(record_id)

    #return the cleaned record and reasons
    return cleaned_record, reasons

def process_records(
    rows: Iterable[dict[str, str]],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Sort records into accepted rows and issue reports."""
    
    # create empty lists and a set 
    clean_records = []  # all accepted, clean records
    issues = [] # info about rejectde records
    accepted_ids = set()    # for storing results

    # start at row 2 b/c row 1 contains the csv header
    source_row = 2

    # loop through every tree record
    for row in rows:

        # validate the current record using our previous function
        cleaned_record, reasons = validate_record(
            row, source_row, accepted_ids)

        # store accepted records
        if cleaned_record != None:
            clean_records.append(cleaned_record)
        # store rejected records and their reasons
        else:
            issue = {
                "source_row": str(source_row),
                "record_id": row["record_id"].strip(),
                "reasons": "; ".join(reasons)
            }
            issues.append(issue)

        # move to the next row number
        source_row = source_row + 1

    # sort accepted records by record_id
    clean_records.sort(key=lambda record: record["record_id"])  # additional utility mentioned in README.md

    # return both lists
    return clean_records, issues


def summarise_oaks(clean_records: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    """Count accepted oak records by species."""
        # create empty dictionary to store oak species counts
    oak_counts = {}

    # loop through all accepted records
    for record in clean_records:
        # xheck whether the tree is an oak
        if record["genus"] == "Quercus":
            # get the species name
            species = record["species"]
            # increase the count by 1 if the species already exists
            if species in oak_counts:
                oak_counts[species] = oak_counts[species] + 1
            # otherwise, start the count at 1
            else:
                oak_counts[species] = 1

    # create an empty list for the final summary
    summary = []

    # loop through the species in alphabetical order
    for species in sorted(oak_counts):  # additional utility sorted() used, mentioned in README.md
        # add the species and its count to the summary
        summary.append({
            "species": species,
            "count": str(oak_counts[species])
        })

    # return the completed summary
    return summary


def write_csv(
    path: Path,
    fieldnames: list[str],
    rows: Iterable[dict[str, str]],
) -> None:
    """Write rows to a CSV file, replacing an older copy."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as destination:
        writer = csv.DictWriter(destination, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """Clean the survey and write the three result files."""
    clean_records, issues = process_records(load_records())
    oak_counts = summarise_oaks(clean_records)

    write_csv(
        RESULTS_DIR / "silwood_trees_clean.csv",
        INPUT_FIELDS,
        clean_records,
    )
    write_csv(
        RESULTS_DIR / "silwood_tree_issues.csv",
        ISSUE_FIELDS,
        issues,
    )
    write_csv(
        RESULTS_DIR / "oak_species_counts.csv",
        OAK_COUNT_FIELDS,
        oak_counts,
    )


if __name__ == "__main__":
    main()
