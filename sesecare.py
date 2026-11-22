#!/usr/bin/env python3
"""Health Tracker - Person 1: Main Menu and Add Medication."""
import sqlite3
from datetime import date

DB_FILE = "sesecare.db"

# Settings for the summary and alerts feature (option 3).
# goal = recommended amount per record; the alert uses it.
METRICS = {
    "1": {"key": "water", "name": "Water Intake", "unit": "liters", "goal": 2.0,
          "tip": "Try drinking a glass of water with each meal."},
    "2": {"key": "exercise", "name": "Exercise Minutes", "unit": "minutes", "goal": 30.0,
          "tip": "A brisk 30 minute walk each day is a good start."},
    "3": {"key": "sleep", "name": "Sleep Hours", "unit": "hours", "goal": 7.0,
          "tip": "Try a fixed bedtime and keep screens away before sleeping."},
}

MAX_VALUES = {"water": 20, "exercise": 1440, "sleep": 24}

def show_menu():
    """Print the main menu."""
    print("\n=== HEALTH TRACKER ===")
    print("1. Record Health Reading")
    print("2. Manage Medications")
    print("3. View Summary & Alerts")
    print("4. Exit")


def save_reading(metric_key, value, reading_date):
    """Save one reading into the SQL database."""
    conn = sqlite3.connect(DB_FILE)
    try:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS readings ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "metric TEXT NOT NULL, "
            "value REAL NOT NULL, "
            "date TEXT NOT NULL)"
        )

        conn.execute(
            "INSERT INTO readings (metric, value, date) "
            "VALUES (?, ?, ?)",
            (metric_key, value, reading_date)
        )

        conn.commit()
    finally:
        conn.close()



def record_reading():
    """Option 1: record water intake, exercise minutes or sleep hours."""
    print("\n--- Record Health Reading ---")
    print("What would you like to record?")
    for number, info in METRICS.items():
        print("{}. {}".format(number, info["name"]))
    print("4. Back to Main Menu")

    choice = input("Enter your choice (1-4): ").strip()
    if choice == "4":
        return
    if choice not in METRICS:
        print("Invalid choice. Please type a number from 1 to 4.")
        return

    info = METRICS[choice]
    prompt = "Enter {} in {}: ".format(info["name"].lower(), info["unit"])
    try:
        value = float(input(prompt))
    except ValueError:
        print("Invalid input. Please type a number, for example 2.5.")
        return

    maximum = MAX_VALUES[info["key"]]
    if not (0 < value <= maximum):
        print("That value does not look right. Please enter a number "
              "above 0 and up to {:g} {}.".format(maximum, info["unit"]))
        return

    reading_date = date.today().isoformat()
    try:
        save_reading(info["key"], value, reading_date)
    except sqlite3.Error as error:
        print("Could not save to the database: {}".format(error))
        return

    print("Saved! {}: {:g} {} recorded on {}.".format(
        info["name"], value, info["unit"], reading_date))

def manage_medications():
    """Option 2: add, view or remove medications."""
    print("\n--- Manage Medications ---")
    print("1. Add Medication")
    print("2. View Medications")
    print("3. Remove Medication")

    med_choice = input("Choose an option (1-3): ")

    if med_choice == "1":
        med_name = input("Enter medication name: ")
        med_dose = input("Enter medication dose (e.g., 500mg, 1 tablet): ")
        med_time = input("Enter medication time (e.g., 08:00 AM): ")

        with open("medications.txt", "a") as file:
            file.write("Name: {} | Dose: {} | Time: {}\n".format(med_name, med_dose, med_time))

        print("Success! '{}' has been saved to medications.txt.".format(med_name))

    elif med_choice == "2":
        print("View Medications feature coming soon...")
    elif med_choice == "3":
        print("Remove Medication feature coming soon...")
    else:
        print("Invalid choice. Returning to main menu.")

def get_recent_readings(metric_key, limit=7):
    """Return the newest readings for one metric as a list of (value, date)."""
    conn = sqlite3.connect(DB_FILE)
    conn.execute("CREATE TABLE IF NOT EXISTS readings ("
                 "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                 "metric TEXT NOT NULL, value REAL NOT NULL, date TEXT NOT NULL)")
    rows = conn.execute("SELECT value, date FROM readings WHERE metric = ? "
                        "ORDER BY date DESC, id DESC LIMIT ?",
                        (metric_key, limit)).fetchall()
    conn.close()
    return rows


def show_alert(info, readings, lowest):
    """Warn when more than half of the records are below the recommended goal."""
    below = [r for r in readings if r[0] < info["goal"]]
    if len(below) > len(readings) / 2:
        print("\nALERT: {} of {} records were below the recommended {:g} {}".format(
            len(below), len(readings), info["goal"], info["unit"]))
        print("(lowest: {:g} {} on {}).".format(lowest[0], info["unit"], lowest[1]))
        print(info["tip"])
    else:
        print("\nGood job! You are meeting your recommended amount most days.")


def view_summary():
    """Option 3: show average, highest, lowest and alerts."""
    print("\n--- View Summary & Alerts ---")
    print("Which reading would you like to see a summary for?")
    for number, info in METRICS.items():
        print("{}. {}".format(number, info["name"]))
    print("4. Back to Main Menu")

    choice = input("Enter your choice (1-4): ").strip()
    if choice == "4":
        return
    if choice not in METRICS:
        print("Invalid choice. Please type a number from 1 to 4.")
        return

    info = METRICS[choice]
    try:
        readings = get_recent_readings(info["key"], 7)
    except sqlite3.Error as error:
        print("Could not read the database: {}".format(error))
        return

    if not readings:
        print("No {} records yet. Record one from option 1 first.".format(info["name"].lower()))
        return

    values = [r[0] for r in readings]
    average = sum(values) / len(values)
    highest = max(readings, key=lambda r: r[0])
    lowest = min(readings, key=lambda r: r[0])

    print("\n--- Summary for {} (last {} records) ---".format(info["name"], len(readings)))
    print("Average: {:.1f} {}".format(average, info["unit"]))
    print("Highest: {:g} {}".format(highest[0], info["unit"]))
    print("Lowest:  {:g} {}".format(lowest[0], info["unit"]))

    show_alert(info, readings, lowest)
    input("\nPress Enter to return to the main menu...")


def main():
    """Main loop to display menu and handle user choices."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            record_reading()
        elif choice == "2":
            manage_medications()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Exiting SeseCare Health Tracker. Stay healthy!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
