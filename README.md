# SeseCare
PLP 2 demo of terminal menu app.
🏥 SeseCare – Personal Health Tracker

PLP 2 Demo Project | Python Terminal Menu Application

Take control of your health, one record at a time!

SeseCare is a simple, menu-driven personal health tracking application developed using Python as part of the Power Learn Project (PLP) 2.

It allows users to record daily health activities, manage medication records, and monitor their progress through health summaries and personalized alerts.

The application uses SQLite to store health readings and text-file storage to manage medication information.

📌 Features
💧 1. Record Health Readings

Track important daily health activities, including:

Water Intake: Record daily water consumption in liters.
Exercise Minutes: Track daily physical activity in minutes.
Sleep Hours: Monitor daily sleeping hours.

The application validates user input to ensure recorded values fall within acceptable ranges.

Health Tracking Goals
Health Metric	Recommended Goal	Maximum Allowed
Water Intake	2 liters	20 liters
Exercise	30 minutes	1,440 minutes
Sleep	7 hours	24 hours
💊 2. Medication Management

Manage medication records through an interactive menu.

Available operations:

Add new medications.
Record medication names.
Specify medication dosage.
Set medication times.
View saved medications.
Remove medications from the list.

Medication details are stored locally in medications.txt.

📊 3. Health Summary & Alerts

Review your health tracking progress through automatically generated summaries.

For each health metric, SeseCare provides:

Average recorded value.
Highest recorded value.
Lowest recorded value.
Analysis of the seven most recent records.
Alerts when more than half of recent records fall below the recommended goal.
Helpful health tips to encourage better habits.
🛠️ Technologies Used
Technology	Purpose
Python 3	Main programming language
SQLite3	Health reading database
Text Files	Medication record storage
Datetime	Date and time management
Git & GitHub	Version control
📂 Project Structure
text
SeseCare/
│
├── sesecare.py        # Main application
├── sesecare.db        # SQLite database (auto-generated)
├── medications.txt    # Medication records (auto-generated)
└── README.md          # Project documentation


Note: The database and medication file are generated automatically when needed.

🚀 Installation and Setup

Follow these steps to run SeseCare on your computer.

Prerequisites

Ensure you have the following installed:

Python 3.x
Git
A terminal or command-line interface

Note: SQLite3 is included in Python's standard library. No additional package installation is required.

Step 1: Clone the Repository
bash
git clone https://github.com/Eden-GNI/SeseCare.git

Step 2: Navigate to the Project Directory
bash
cd SeseCare

Step 3: Run the Application

Linux / macOS:

bash
python3 sesecare.py


Windows:

bash
python sesecare.py

🖥️ Application Usage

After launching the application, the following main menu will appear:

text
=== HEALTH TRACKER ===

1. Record Health Reading
2. Manage Medications
3. View Summary & Alerts
4. Exit

Enter your choice (1-4):

1. Record Health Reading

Select option 1 to record a health metric.

Available options:

text
--- Record Health Reading ---

What would you like to record?

1. Water Intake
2. Exercise Minutes
3. Sleep Hours
4. Back to Main Menu


Choose a metric and enter the corresponding measurement.

2. Manage Medications

Select option 2 to manage medication records.

Available options:

text
--- Manage Medications ---

1. Add Medication
2. View Medications
3. Remove Medication
4. Back to Main Menu


When adding a medication, you will provide:

Medication name.
Medication dose.
Medication time (HH:MM AM/PM).
3. View Summary & Alerts

Select option 3 to review your health statistics.

Choose one of the available metrics:

Water Intake.
Exercise Minutes.
Sleep Hours.

The application displays the average, highest, and lowest recorded values.

It also evaluates the seven most recent records and generates an alert if more than half fall below the recommended goal.

4. Exit

Select option 4 to exit the application safely.

💾 Data Storage

SeseCare uses two local storage mechanisms.

1. SQLite Database (sesecare.db)

Stores health readings using the following fields:

Field	Description
id	Unique reading identifier
metric	Type of health metric
value	Recorded measurement
date	Date of the reading
2. Text File (medications.txt)

Stores medication information, including:

Medication name.
Medication dosage.
Medication time.

All application data is stored locally on the computer.

🔒 Input Validation and Error Handling

SeseCare includes basic validation and error-handling mechanisms to improve reliability.

These include:

Rejecting invalid menu selections.
Preventing non-numeric health readings.
Checking that health readings fall within acceptable ranges.
Ensuring required medication details are provided.
Validating medication time formats.
Handling database and file-related errors.
Supporting graceful application exit using Ctrl + C.
🔮 Future Improvements

Potential enhancements include:

User registration and authentication.
Multiple user profiles.
Medication reminders.
Weekly and monthly health reports.
Graphical health progress charts.
Automatic data backups.
Graphical user interface (GUI).
Customizable health goals.
🤝 Contributing

Contributions, suggestions, and improvements are welcome!

To contribute:

Fork this repository.
Create a feature branch:
bash
git checkout -b feature/new-feature

Make your changes.
Commit your changes:
bash
git commit -m "Add: new feature"

Push your branch:
bash
git push origin feature/new-feature

Open a Pull Request.
📄 License

No license has currently been specified for this project.

Please contact the repository owner for permission before redistributing the project.




⭐ If you find SeseCare useful, consider giving this repository a star!

Built with ❤️ using Python.

Disclaimer: SeseCare is an educational health-tracking application. Its goals and alerts are general tracking guidelines, not medical advice. It records medication information but does not provide automated medication reminders.
