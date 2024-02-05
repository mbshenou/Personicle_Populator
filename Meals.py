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
        food = random.choice(food)

        # Create a dictionary for the activity
        activity = {
            "activity_type": exercise,
            "start_time": log_time.strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration": duration,
            "location": location
        }

        # Add the activity to the activity log
        activity_log.append(activity)

        # Move to the next activity
        current_date = end_time

    # Save the activity log to a JSON file
    with open("activity_log.json", "w") as f:
        json.dump(activity_log, f, indent=4)


generate_activity_log()
