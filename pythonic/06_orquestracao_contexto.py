from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterator
from typing import Iterable
import logging

FOOD_CSV = Path("food.csv")
ACTIVITY_CSV = Path("activities.csv")


logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

@dataclass(frozen=True)
class Entry:
    date: str
    description: str
    calories: int

def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")

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

def summarize_entries(
    food: Iterable[Entry],
    activity: Iterable[Entry],
    date: str
) -> dict[str, int]:
    food_total = sum(e.calories for e in food if e.date == date)
    activity_total = sum(e.calories for e in activity if e.date == date)

    return {
        "food": food_total,
        "activity": activity_total,
        "net": food_total - activity_total
    }
print(summarize_entries(
    read_entries(FOOD_CSV),
    read_entries(ACTIVITY_CSV),
    today()
))
    

log_food = Entry(date=today(), description="Apple", calories=95)
append_entry(FOOD_CSV, log_food)



print("Log de atividades concluído.")
print(summary)
