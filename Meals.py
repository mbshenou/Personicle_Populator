import json
from datetime import datetime, timedelta
import random


def generate_meal_log():
    entry_count = 10

    # Later we can implement a call to a file with a large list of food
    food = ["carrot", "celery", "onion", "garlic", "potato", "chicken", "salt", "pepper", "thyme", "bay leaf",
            "chicken"]

    # Define the possible locations for the activities
    locations = ["gym", "park", "home", "office"]
    meal_log = []
    for i in range(entry_count):
        # class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

        # not going for accuracy just trying to get MVP
        # not inclusive so max will be 2024
        year = random.randrange(2000, 2025)
        month = random.randrange(1, 13)
        day = random.randrange(1, 29)
        hour = random.randrange(1, 24)
        minute = random.randrange(1, 60)
        second = random.randrange(1, 60)

        log_time = datetime(year, month, day, hour, minute, second)

        # Generate a random location
        location = random.choice(locations)
        curr_meal = []
        j_range = random.randrange(1, 10)
        for j in range(j_range):
            curr_meal.append(random.choice(food))


        # Create a dictionary for the activity

        meals = {
            "food": curr_meal,
            "start_time": log_time.strftime("%Y-%m-%d %H:%M:%S"),
            "location": location
        }

        # Add the activity to the activity log
        meal_log.append(meals)

        # Move to the next activity
    print(meal_log)
    # Save the activity log to a JSON file
    with open("meal_log.json", "w") as f:
        json.dump(meal_log, f, indent=4)


generate_meal_log()
