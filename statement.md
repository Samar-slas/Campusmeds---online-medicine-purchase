# Campusmeds---online-medicine-purchase

## Problem Statement

CampusMeds is a simple Python and SQLite3 based campus pharmacy management system developed to solve a practical problem faced by college hostel students.

The system allows a student to:

- Register using Student ID, name and hostel room.
- View the medicines available in the campus pharmacy.
- Select one or multiple medicines and enter the required quantity.
- Automatically calculate the total order amount.
- Automatically update the medicine stock after an order.
- View previous orders and their total amount.
- Request a medicine that is not currently available.

The project uses **Python 3** for the application logic and **SQLite3** for storing student, medicine, order and medicine-request data. It is designed as a terminal-based application so that the main focus remains on understanding Python programming and database concepts.

## Main Objective

The main objective of CampusMeds is to provide a simple and convenient way for students to order medicines within the college campus without needing to visit an outside pharmacy.

## Technologies Used

- Python 3
- SQLite3
- Terminal / Command Prompt

## Database

The application uses four main SQLite tables:

- `students` – stores student information
- `medicine` – stores medicine name, price and stock
- `orders` – stores medicine order details
- `requests` – stores requests for unavailable medicines

  ## Target Users

- Hostellers
- Pharma Shop Owners
- Hospitals
