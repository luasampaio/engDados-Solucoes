from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterator
from typing import Iterable
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

@dataclass(frozen=True)
class Entry:
    date: str
    description: str
    calories: int

def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


food_csv = Path("food.csv")
activity_csv = Path("activities.csv")

date = today()

def append_entry(path: Path, entry: Entry) -> None:
    with path.open("a") as f:
        f.write(f"{entry.date},{entry.description},{entry.calories}\n")
    print(f"Appended to {path}: {entry.description} ({entry.calories} kcal)")


def read_entries(path: Path) -> Iterator[Entry]:
    try:
        with path.open() as f:
            for line in f:
                date, desc, cals = line.strip().split(",")
                yield Entry(date, desc, int(cals))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return iter([])


def summarize_entries(food: Iterable[Entry], activity: Iterable[Entry], date: str) -> dict:
    food_total = sum(entry.calories for entry in food)
    activity_total = sum(entry.calories for entry in activity)
    return {
        "date": date,
        "food": food_total,
        "activity": activity_total,
        "net": food_total - activity_total,
    }

append_entry(food_csv, Entry(date, "Apple", 95))
append_entry(activity_csv, Entry(date, "Running", 300))


summary = summarize_entries(
    read_entries(food_csv),
    read_entries(activity_csv),
    date,
)

logging.info(
    "Daily summary | intake=%s kcal | burned=%s kcal | net=%s kcal",
    summary["food"],
    summary["activity"],
    summary["net"],
)

print(summary)
