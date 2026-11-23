# SeseCare
PLP 2 demo of terminal menu app.
🏥 SeseCare – Personal Health Tracker

Take control of your health, one record at a time!

SeseCare is a simple, menu-driven health tracking application built with Python. It allows users to record daily health activities, manage medications, and monitor their progress through summaries and personalized health alerts.

The application uses SQLite for storing health readings and text-file storage for managing medication information.

📌 Features
1. 💧 Record Health Readings

Track important daily health activities, including:

Water Intake: Record daily water consumption in liters.
Exercise Minutes: Track daily physical activity in minutes.
Sleep Hours: Monitor daily sleeping hours.

The application validates user input to ensure that recorded values fall within acceptable ranges.

Health Metric	Recommended Goal	Maximum Allowed
Water Intake	2 liters	20 liters
Exercise	30 minutes	1,440 minutes
Sleep	7 hours	24 hours
2. 💊 Medication Management

Manage your medication records through an interactive menu.

Available operations:

Add new medications.
Record medication names.
Specify medication dosage.
Set medication times.
View saved medications.
Remove medications from the list.

Medication details are stored locally in medications.txt.

3. 📊 Health Summary & Alerts

Review your health tracking progress using automatically generated summaries.

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
├── sesecare.db        # SQLite database (created automatically)
├── medications.txt    # Medication records (created when needed)
└── README.md          # Project documentation


Note: The database and medication file are generated automatically when the application needs them.

🚀 Installation and Setup

Follow these steps to run SeseCare on your computer.

Prerequisites

Ensure you have:

Python 3.x installed.
Git installed.
A terminal or command-line interface.

SQLite3 is included in Python's standard library, so no additional package installation is required.

Step 1: Clone the Repository
bash
git clone https://github.com/Eden-GNI/SeseCare.git

Step 2: Navigate to the Project Directory
bash
cd SeseCare

Step 3: Run the Application
bash
python3 sesecare.py


On Windows, you can use:

bash
python sesecare.py

🖥️ Application Usage

When you launch SeseCare, the following main menu appears:

text
=== HEALTH TRACKER ===
1. Record Health Reading
2. Manage Medications
3. View Summary & Alerts
4. Exit

Enter your choice (1-4):

Option 1: Record Health Reading

Choose option 1 to record a health metric.

You can select:

text
--- Record Health Reading ---
What would you like to record?
1. Water Intake
2. Exercise Minutes
3. Sleep Hours
4. Back to Main Menu


For example, selecting Water Intake allows you to enter your daily water consumption.

Option 2: Manage Medications

Choose option 2 to manage your medication records.

The medication menu provides:

text
--- Manage Medications ---
1. Add Medication
2. View Medications
3. Remove Medication
4. Back to Main Menu


When adding a medication, you provide:

Medication name.
Medication dose.
Medication time (HH:MM AM/PM).
Option 3: View Summary & Alerts

Choose option 3 to review your health statistics.

You can select Water Intake, Exercise Minutes, or Sleep Hours to view:

Average values.
Highest values.
Lowest values.
Health alerts and recommendations.

The application evaluates your seven most recent records and displays an alert if more than half are below the recommended goal.

Option 4: Exit

Choose option 4 to safely exit the application.

💾 Data Storage

SeseCare uses two local storage mechanisms:

1. SQLite Database (sesecare.db)

Stores health readings with the following fields:

id – Unique reading identifier.
metric – Type of health metric.
value – Recorded measurement.
date – Date of the reading.

2. Text File (medications.txt)

Stores medication information, including:

Medication name.
Medication dosage.
Medication time.

All data is stored locally on the computer.

🔒 Input Validation and Error Handling

SeseCare includes basic validation mechanisms to improve reliability:

Rejects invalid menu selections.
Prevents non-numeric health readings.
Checks that health readings fall within acceptable ranges.
Ensures required medication details are provided.
Validates medication time formats.
Handles database and file-related errors.
Supports graceful application exit using Ctrl+C.
🔮 Future Improvements

Potential enhancements include:

Adding user registration and authentication.
Introducing multiple user profiles.
Implementing medication reminders.
Adding weekly and monthly health reports.
Creating graphical health progress charts.
Introducing automatic backups.
Developing a graphical user interface.
Adding customizable health goals.
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

No license has currently been specified for this repository. Please contact the repository owner for permission before redistributing the project.

👨‍💻 Author

Eden-GNI

GitHub: https://github.com/Eden-GNI

Project: SeseCare – Personal Health Tracker

⭐ If you find SeseCare useful, consider giving this repository a star!

Built with ❤️ using Python.
