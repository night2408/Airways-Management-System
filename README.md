# Airways Management System

## Overview

The **Airways Management System** is a Python-based application designed to manage various aspects of an airline's operations. It includes functionalities for administrator, employee, and passenger management. The system interacts with a MySQL database to store and retrieve data such as employee details, passenger information, flight schedules, and snack services.

## Features

- **Admin Login and Management**:
  - Admins can log in using their unique ID and password.
  - Admins can create and delete employee records.

- **Employee Login and Management**:
  - Employees can log in to view and manage passenger information.
  - Employees can insert new snack items and delete existing ones.

- **Passenger Login and Ticket Management**:
  - Passengers can log in to view their ticket details or reschedule their flights.
  - New passengers can create an account, book tickets, and select their class type (First, Business, or Economy).
  - Passengers can also add extra baggage or select snacks.

- **Review System**:
  - Passengers can write reviews, rate their experience, and provide suggestions.
  - Reviews can be read by other users.

## Database Setup

The system requires a MySQL database named `Airways_Management`. The following tables are used in the system:

- `Admin`: Stores admin credentials.
- `employee`: Stores employee details.
- `customer1`: Stores passenger details.
- `passen_data`: Stores passenger travel data.
- `snack`: Stores snack options available for purchase.
- `classtype`: Stores different class types available (First, Business, Economy).

## How to Use

1. **Admin Login**: Enter your Admin ID and password to log in and manage employee data.
2. **Employee Login**: Enter your Employee ID, name, and password to log in and manage passenger data and snacks.
3. **Passenger Login**: Log in with your Passenger ID, name, and password to view or reschedule your flight.
4. **Create New Passenger ID**: New passengers can sign up by providing their name, password, and other details. After signup, they can book tickets and select additional services.
5. **Reviews**: Passengers can write or read reviews after logging in.

## Dependencies

- **Python 3.x**
- **MySQL Connector**: Install using `pip install mysql-connector-python`
- **CSV module**: This is part of the Python Standard Library.

## Running the Application

1. Ensure MySQL is installed and running.
2. Set up the database and tables as described above.
3. Run the Python script using `python script_name.py`.
4. Follow the prompts to interact with the system.

