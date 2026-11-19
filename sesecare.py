#!/usr/bin/env python3
"""Health Tracker - Person 1: Main Menu and Add Medication."""

def show_menu():
    """Print the main menu."""
    print("\n=== HEALTH TRACKER ===")
    print("1. Record Health Reading")
    print("2. Manage Medications")
    print("3. View Summary & Alerts")
    print("4. Exit")

def record_reading():
    """Option 1: record water intake, exercise minutes, weight or sleep hours."""
    print("\n--- Record Health Reading ---")
    # TODO: add the code that records a reading here

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

def view_summary():
    """Option 3: show average, highest, lowest and alerts."""
    print("\n--- View Summary & Alerts ---")
    # TODO: add the code that shows the summary and alerts here

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
