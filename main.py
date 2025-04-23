"""
# File: main.py
# This script reads a JSON file containing meal options for breakfast, lunch, and dinner,
# and prints the options to the console.
"""
import json


def main():
    """
    The main function of the script.
    """
    json_file = open("meals.json", "r", encoding="utf-8")
    data = json.load(json_file)
    json_file.close()
    breakfast = data["breakfast"]
    lunch = data["lunch"]
    dinner = data["dinner"]
    print("Breakfast options:")
    for meal in breakfast:
        print(meal)
    print("\nLunch options:")
    for meal in lunch:
        print(meal)
    print("\nDinner options:")
    for meal in dinner:
        print(meal)


if __name__ == "__main__":
    main()
