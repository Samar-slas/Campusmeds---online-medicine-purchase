# CampusMeds

## Campus Pharmacy Management System

CampusMeds is a simple **Python + SQLite3** project made to manage medicine orders inside a college campus.

Students can register themselves, buy medicines, view their orders, and request medicines that are not available.

## Features

* Add Student
* View available medicines
* Buy multiple medicines in one order
* Calculate total price automatically
* Update medicine stock automatically
* View previous orders
* Request unavailable medicines
* 15-minute medicine delivery
* 7-day delivery for requested medicines

## Project Motivation

As a college hosteller, I have personally faced the problem of needing medicine and having to go to a pharmacy to buy it.

CampusMeds is designed to make this process easier by allowing **students and campus pharmacy owners to interact through an online system using their college ID**.

Students can order medicine from the campus pharmacy, and the pharmacy can receive the order and deliver the medicine directly to the student's **hostel room or room location**.

The main idea is to make medicine ordering inside the campus **simple, convenient and time-saving** for both students and pharmacy owners.

## Technologies Used

* **Python 3**
* **SQLite3**
* Terminal / Command Prompt

No external Python libraries are required.

## Project Files

```text
CampusMeds/
│
├── campusmeds.py
├── campusmeds.db
└── README.md
```

`campusmeds.db` is created automatically when the program is run.

## How to Run

### 1. Check Python

```bash
python --version
```

or:

```bash
python3 --version
```

### 2. Open the Project Folder

```bash
cd CampusMeds
```

### 3. Run the Program

Linux:

```bash
python3 campusmeds.py
```

Windows:

```bash
python campusmeds.py
```

The main menu will appear:

```text
1. Add Student
2. Buy Medicine
3. Show Orders
4. Request New Medicine
5. Exit
```

## How It Works

### Add Student

Enter:

* Student ID
* Student Name
* Hostel Room

### Buy Medicine

Enter Student ID → Select medicine → Enter quantity → Add more medicines if required → Place order.

The program calculates the total and updates the stock.

### Show Orders

Enter Student ID to see previous orders and total amount.

### Request Medicine

Enter Student ID and the medicine name. The request is saved with an expected delivery time of **7 days**.

## Database

The project uses four SQLite tables:

* `students` – student details
* `medicine` – medicine, price and stock
* `orders` – order details
* `requests` – new medicine requests

## Troubleshooting

### Python not found

Try:

```bash
python3 --version
```

If it does not work, install Python 3.

### File not found

Make sure you are inside the project folder and `campusmeds.py` exists.

### Student not found

Add the student first using **Option 1** and use the same Student ID while ordering.

### Not enough stock

Enter a smaller quantity.

### IndentationError

Check the indentation of `if`, `else`, `while` and other blocks. Use **4 spaces** for indentation.

## Important

Do not delete `campusmeds.db` if you want to keep your saved data.

If the database is deleted, a new database will be created when the program runs again.

## About the Author

**Samar Yadav**

I am a first-year **B.Tech CSE (AI/ML) student and a college hosteller**.

I created CampusMeds based on a real problem I experienced while living in a hostel. The purpose of this project is to use basic Python and database concepts to solve a practical problem faced by students on campus.

**Made as a college Python project.**
