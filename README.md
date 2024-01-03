# Fees Management System

![Status](https://img.shields.io/badge/status-under%20developement-red)
![Forks](https://img.shields.io/github/forks/AKGames2001/online-examination-system)
![Stars](https://img.shields.io/github/stars/AKGames2001/online-examination-system)
![Issues](https://img.shields.io/github/issues/AKGames2001/online-examination-system)

## Description

The Fees Management System is designed to streamline & automate the process of managing fees within an educational institution. This system aims to provide an efficient & transparent way to handle fee-related transactions, ensuring accuracy, timeliness, and ease 
of use.

This app is developed while keeping in mind the necessities of the admins/clerks as well as students.

### Technologies Used:
* Project Based on Python/Django stack
  - **FMS** - Client (HTML5 + Bootstrap)
  - **Server** - Backend (Python + Django)
  - **Database** - SQLite3

* Libraries Used
  - **[Django](https://www.djangoproject.com/)** - Web Framework used to develope big websites
  - **[Pandas](https://pandas.pydata.org/)** - Data Handling Library of Python
  - **[Tablib](https://tablib.readthedocs.io/)** - Used for Handling Pythonic Tabular Datasets

<br>

## How to Install?
1. Ensure that Python is installed on your system.
```
python --version
```

2. Clone this repository into your system.
```
git clone https://github.com/AKGames2001/fees-management-system
```

3. Install required libraries using following Python command. <br>
( **Note**: Make sure you are in the same directory as requirements.txt )
```
pip install -r requirements.txt
```
**Note**: This process may take time depending on your internet connectivity, so have patience.

<br>

## How to Run Server?
Now that you have installed the dependancies, it is time to run the server. 
<br>
1. Ensure that you are in correct directory. (Tip: you can use 'cd' to go into directory)
```
../fms_main
```

2. Make migrations for Database.
```
python manage.py makemigrations

python manage.py migrate
```

3. Once there's no error, run the server.
```
python manage.py runserver
```
( **Note**: Your website will be hosted on your local server. )

<br>

## Using FMS - Fees Management System
FMS works for both admin/clerks and students.

Given their respective roles, we can categorize them as follows:

### Students
The accessibility of students is listed below:
- Enter Student_ID
- View Current Status of Fees for current year
- Pay the fees using Pay now button (Work in Progress)

### Admin/Clerks
The accessbility of teachers is listed below:
- View Database of currently registered students
- Upload .xlsx file to update the database

<br>
