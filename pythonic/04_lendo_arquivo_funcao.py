from datetime import datetime
from pathlib import Path
import csv
from typing import Iterable


def current_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def append_log(
    file: Path,
    date: str,
    item: str,
    calories: int
) -> None:
    with file.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, item, calories])


def read_calories_by_date(
    file: Path,
    date: str
) -> Iterable[int]:
    if not file.exists():
        return []

    with file.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == date:
                yield int(row[2])


def calculate_day_summary(
    food_file: Path,
    activity_file: Path,
    date: str
) -> dict[str, int]:
    food_total = sum(read_calories_by_date(food_file, date))
    activity_total = sum(read_calories_by_date(activity_file, date))

    return {
        "food": food_total,
        "activity": activity_total,
        "net": food_total - activity_total,
    }

print(calculate_day_summary(Path("food.csv"), Path("activities.csv"), current_date()))

