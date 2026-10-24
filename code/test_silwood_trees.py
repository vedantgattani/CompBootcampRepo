from clean_silwood_trees import validate_record # import functions from main script
from clean_silwood_trees import process_records
from clean_silwood_trees import summarise_oaks

### TEST validate_record() FUNCTION ###

## test for a normal record ##
# create a hypothetical row of data
row = {
    "record_id": " ST001 ",
    "location": "silwood bottom",
    "genus": "quercus",
    "species": "robur",
    "distance_m": "12.5",
    "angle_degrees": "35"
}

# create an empty set of accepted IDs
accepted_ids = set()

# validate the record using function
cleaned_record, reasons = validate_record(row, 2, accepted_ids)

# check results
assert cleaned_record["record_id"] == "ST001"
assert cleaned_record["location"] == "Silwood Bottom"
assert cleaned_record["genus"] == "Quercus"
assert reasons == []

# if no issues:
print("Normal check passed!")

## test a record with a missing location ##
row_missing_location = {
    "record_id": "ST002",
    "location": "",
    "genus": "Quercus",
    "species": "robur",
    "distance_m": "15",
    "angle_degrees": "40"
}

# validate record
cleaned_record, reasons = validate_record(
    row_missing_location, 3, accepted_ids)

# check if the record was rejected
assert cleaned_record == None

# check if the correct reason was returned
assert reasons == ["missing location"]

print("Missing location test passed!")

## test a record with multiple problems ##
row_multiple_issues = {
    "record_id": "ST003",
    "location": "Unknown Forest",
    "genus": "Quercus",
    "species": "robur",
    "distance_m": "120",
    "angle_degrees": "40"
}

# validate the record
cleaned_record, reasons = validate_record(
    row_multiple_issues, 4, accepted_ids)

# check that the record was rejected
assert cleaned_record == None

# check that both problems were identified
assert reasons == [
    "invalid location",
    "distance_m out of range"]

print("Multiple issues test passed!")

## test for duplicate IDs ##
row_duplicate = {
    "record_id": "ST001",   # id has been used previously in the script
    "location": "Manor House",
    "genus": "Acer",
    "species": "pseudoplatanus",
    "distance_m": "20",
    "angle_degrees": "45"
}

cleaned_record, reasons = validate_record(
    row_duplicate, 5, accepted_ids)

assert cleaned_record == None
assert reasons == ["duplicate record_id"]

print("Duplicate ID test passed!")

## test for invalid numbers in distance_m
row_invalid_distance = {
    "record_id": "ST004",
    "location": "Manor House",
    "genus": "Quercus",
    "species": "robur",
    "distance_m": "unknown",
    "angle_degrees": "45"
}

cleaned_record, reasons = validate_record(
    row_invalid_distance, 7, accepted_ids)

assert cleaned_record == None
assert reasons == ["invalid distance_m"]

print("Invalid distance test passed!")

## test for out-of-range ditance_m
row_distance_range = {
    "record_id": "ST005",
    "location": "Nash's Field",
    "genus": "Acer",
    "species": "pseudoplatanus",
    "distance_m": "0",
    "angle_degrees": "30"
}

cleaned_record, reasons = validate_record(
    row_distance_range, 8, accepted_ids)

assert cleaned_record == None
assert reasons == ["distance_m out of range"]

print("Distance range test passed!")

## test for invalid angle_degrees ##
row_invalid_angle = {
    "record_id": "ST006",
    "location": "Reactor Wood",
    "genus": "Betula",
    "species": "pendula",
    "distance_m": "25",
    "angle_degrees": "90"
}

cleaned_record, reasons = validate_record(
    row_invalid_angle, 9, accepted_ids)

assert cleaned_record == None
assert reasons == ["angle_degrees out of range"]

print("Angle range test passed!")

## test for invalid and special numbers in angle_degrees and distance_m ##
row_nonfinite = {
    "record_id": "ST007",
    "location": "Silwood Bottom",
    "genus": "Fagus",
    "species": "sylvatica",
    "distance_m": "nan",
    "angle_degrees": "inf"
}
cleaned_record, reasons = validate_record(
    row_nonfinite, 10, accepted_ids)
assert cleaned_record == None
assert reasons == [
    "invalid distance_m",
    "invalid angle_degrees"
]

print("Non-finite measurement test passed!")

## test for valid boundary values ##
row_boundary = {
    "record_id": "ST008",
    "location": "Manor House",
    "genus": "Quercus",
    "species": "petraea",
    "distance_m": "100", # <= 100, so valid
    "angle_degrees": "89.9" # <90, so valid
}

cleaned_record, reasons = validate_record(
    row_boundary, 11, accepted_ids)

assert cleaned_record != None
assert reasons == []
assert cleaned_record["distance_m"] == "100.0"
assert cleaned_record["angle_degrees"] == "89.9"

print("Boundary measurement test passed!")

## test an invalid genus/species combination ##
row_invalid_combination = {
    "record_id": "ST009",
    "location": "Reactor Wood",
    "genus": "Quercus",
    "species": "pendula",
    "distance_m": "20",
    "angle_degrees": "45"
}

cleaned_record, reasons = validate_record(
    row_invalid_combination, 12, accepted_ids
)

assert cleaned_record == None
assert reasons == ["invalid genus/species combination"]

# check that the invalid record goes into issues, not clean_records (as suggested in formative feedback)
clean_records, issues = process_records([row_invalid_combination])

assert len(clean_records) == 0
assert len(issues) == 1
assert issues[0]["record_id"] == "ST009"
assert issues[0]["reasons"] == "invalid genus/species combination"

print("Invalid combination test passed!")

## test for missing measurements ##
row_missing_measurements = {
    "record_id": "ST010",
    "location": "Silwood Bottom",
    "genus": "Acer",
    "species": "pseudoplatanus",
    "distance_m": "",
    "angle_degrees": ""
}

cleaned_record, reasons = validate_record(
    row_missing_measurements, 13, accepted_ids)

assert cleaned_record == None
assert reasons == [
    "missing distance_m",
    "missing angle_degrees"
]

print("Missing measurements test passed!")

### TEST process_record() FUNCTION ###

## test for correct sorting by ID, using valid and invalid records ##
test_rows = [
    {
        "record_id": "ST003", # appears before ST001, will help test if sorting works
        "location": "Manor House",
        "genus": "Quercus",
        "species": "robur",
        "distance_m": "20",
        "angle_degrees": "45"
    },
    {
        "record_id": "ST002",
        "location": "Unknown Forest",
        "genus": "Acer",
        "species": "pseudoplatanus",
        "distance_m": "30",
        "angle_degrees": "40"
    },
    {
        "record_id": "ST001",
        "location": "Reactor Wood",
        "genus": "Betula",
        "species": "pendula",
        "distance_m": "15",
        "angle_degrees": "35"
    }
]

# process the example records
clean_records, issues = process_records(test_rows)

# check that two records were accepted and one rejected
assert len(clean_records) == 2
assert len(issues) == 1

# check that every input record is accounted for (as suggested in formative feedback)
assert len(clean_records) + len(issues) == len(test_rows)

# check that accepted records are sorted by record ID
assert clean_records[0]["record_id"] == "ST001"
assert clean_records[1]["record_id"] == "ST003"

# check the rejected record's information
assert issues[0]["source_row"] == "3"
assert issues[0]["record_id"] == "ST002"
assert issues[0]["reasons"] == "invalid location"

print("Process records test passed!")

### TEST summarise_oaks() FUNCTION ###

## test whether counting oaks works ##
oak_test_records = [
    {"genus": "Quercus", "species": "robur"},
    {"genus": "Quercus", "species": "petraea"},
    {"genus": "Acer", "species": "pseudoplatanus"},
    {"genus": "Quercus", "species": "robur"}
]

oak_counts = summarise_oaks(oak_test_records)

assert oak_counts == [
    {"species": "petraea", "count": "1"}, # petraea should appear before robur b/c alphabetical order
    {"species": "robur", "count": "2"}
]

print("Oak counting test passed!")

## test a near-match ##
near_match_records = [
    {"genus": "Quercus", "species": "robur"},
    {"genus": "Quercuss", "species": "robur"},
    {"genus": "quercus", "species": "petraea"}
]

oak_counts = summarise_oaks(near_match_records)

assert oak_counts == [
    {"species": "robur", "count": "1"} # since Quercuss and quercus are invalid 
]

print("Oak near-match test passed!")

## test for dataset with no oaks ##
no_oak_records = [
    {"genus": "Acer", "species": "pseudoplatanus"},
    {"genus": "Betula", "species": "pendula"}
]

oak_counts = summarise_oaks(no_oak_records)

assert oak_counts == []

print("No oak test passed!")

## test that rejected oak records are not counted ##

oak_test_rows = [
    {
        "record_id": "ST011",
        "location": "Manor House",
        "genus": "Quercus",
        "species": "robur",
        "distance_m": "20",
        "angle_degrees": "45"
    },
    {
        "record_id": "ST012",
        "location": "Manor House",
        "genus": "Quercus",
        "species": "pendula",  # invalid genus-species combination
        "distance_m": "25",
        "angle_degrees": "40"
    },
    {
        "record_id": "ST013",
        "location": "Reactor Wood",
        "genus": "Quercus",
        "species": "petraea",
        "distance_m": "30",
        "angle_degrees": "35"
    }
]

# validate and separate the records
clean_records, issues = process_records(oak_test_rows)

# count only accepted oak records
oak_counts = summarise_oaks(clean_records)

# check that the invalid oak was rejected
assert len(clean_records) == 2
assert len(issues) == 1
assert issues[0]["record_id"] == "ST012"

# check that only the two valid oaks were counted
assert oak_counts == [
    {"species": "petraea", "count": "1"},
    {"species": "robur", "count": "1"}
]

print("Accepted oak counting test passed!")