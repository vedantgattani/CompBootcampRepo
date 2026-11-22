import csv


def load_observations(path):
    with open(path, newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))

def parse_count(count_text):
    if count_text == "":
        return None
    if not isinstance(count_text, str):
        raise ValueError("count must be text")
    count = int(count_text)
    if count < 0:
        raise ValueError("Count must be non-negative")
    return count


if __name__ == "__main__":
    rows = load_observations("data/bootcamp_observations.csv")
    print(rows[0])
    print(rows[2])
