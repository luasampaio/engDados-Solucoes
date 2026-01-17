from datetime import datetime
from pathlib import Path
import csv
from typing import Iterable


DATA_DIR = Path(".")
FOOD_FILE = DATA_DIR / "food.csv"
ACTIVITY_FILE = DATA_DIR / "activities.csv"


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def append_log(file: Path, item: str, calories: int, date: str | None = None) -> None:
    date = date or today()
    with file.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, item, calories])
    print(f"Appended {file.stem}: {item} ({calories} kcal) on {date}")


def read_calories(file: Path, date: str) -> Iterable[int]:
    if not file.exists():
        return []

    with file.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == date:
                yield int(row[2])


def log_food(item: str, calories: int, date: str | None = None) -> None:
    append_log(FOOD_FILE, item, calories, date)


def log_activity(item: str, calories: int, date: str | None = None) -> None:
    append_log(ACTIVITY_FILE, item, calories, date)


def run_day_summary(date: str) -> None:
    food_total = sum(read_calories(FOOD_FILE, date))
    activity_total = sum(read_calories(ACTIVITY_FILE, date))
    net = food_total - activity_total

    print(f"\nSummary for {date}")
    print(f"  Food:     {food_total} kcal")
    print(f"  Activity: {activity_total} kcal")
    print(f"  Net:      {net} kcal")
