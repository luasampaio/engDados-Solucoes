from datetime import datetime
import os
import sys

# Força UTF-8 no console (Windows)
sys.stdout.reconfigure(encoding="utf-8")

def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")

def log_food(item, calories, date=None):
    if date is None:
        date = today()
    with open("food.csv", "a", encoding="utf-8") as f:
        f.write(f"{date},{item},{calories}\n")
    print(f"Appended food: {item} ({calories} kcal) on {date}")

def log_activity(item, calories, date=None):
    if date is None:
        date = today()
    with open("activities.csv", "a", encoding="utf-8") as f:
        f.write(f"{date},{item},{calories}\n")
    print(f"Appended activity: {item} ({calories} kcal) on {date}")

def run_day_summary(date):
    food = []
    if os.path.exists("food.csv"):
        with open("food.csv", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == date:
                    food.append(int(parts[2]))

    activity = []
    if os.path.exists("activities.csv"):
        with open("activities.csv", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == date:
                    activity.append(int(parts[2]))

    food_total = sum(food)
    activity_total = sum(activity)
    net = food_total - activity_total

    print(f"\nSummary for {date}")
    print(f"  🍎 Food:     {food_total} kcal")
    print(f"  🏃 Activity: {activity_total} kcal")
    print(f"  ⚖️  Net:       {net} kcal")


log_food("Banana", 100)
log_activity("Running", 300)
run_day_summary(today())
