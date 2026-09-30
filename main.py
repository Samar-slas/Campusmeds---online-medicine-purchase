import sqlite3

con = sqlite3.connect("campusmeds.db")
cur = con.cursor()

cur.execute("create table if not exists students(id text, name text, room text)")
cur.execute(
    "create table if not exists medicine("
    "id integer, name text, price integer, stock integer)"
)
cur.execute(
    "create table if not exists orders("
    "student text, medicine text, quantity integer, total integer, delivery text)"
)
cur.execute(
    "create table if not exists requests("
    "student text, medicine text, delivery text)"
)
con.commit()

cur.execute("select count(*) from medicine")
if cur.fetchone()[0] == 0:
    medicines = [
        ("Paracetamol 500mg", 10, 50),
        ("Paracetamol 650mg", 15, 50),
        ("Ibuprofen", 20, 40),
        ("Aspirin", 15, 40),
        ("Cetirizine", 10, 40),
        ("Levocetirizine", 15, 40),
        ("ORS", 5, 50),
        ("Antacid Tablet", 5, 50),
        ("Antacid Syrup", 80, 20),
        ("Cough Syrup", 90, 20),
        ("Pain Relief Gel", 90, 20),
        ("Pain Relief Spray", 120, 20),
        ("Antiseptic Cream", 50, 30),
        ("Antiseptic Liquid", 70, 30),
        ("Burn Cream", 60, 20),
        ("Calamine Lotion", 80, 20),
        ("Moisturizer", 100, 20),
        ("Sunscreen", 180, 20),
        ("Antifungal Cream", 80, 20),
        ("Antibiotic Cream", 70, 20),
        ("Bandage", 10, 50),
        ("Cotton", 30, 40),
        ("Medical Tape", 25, 30),
        ("Cotton Buds", 30, 30),
        ("Thermometer", 150, 10),
        ("Vitamin C", 30, 50),
        ("Vitamin B Complex", 40, 40),
        ("Calcium Tablet", 50, 30),
        ("Iron Tablet", 40, 30),
        ("Multivitamin", 100, 30),
        ("Electrolyte Powder", 20, 40),
        ("Glucose Powder", 60, 30),
        ("Vaseline", 50, 30),
        ("Lip Balm", 50, 30),
        ("Eye Drops", 70, 20),
        ("Nasal Drops", 50, 20),
        ("Ear Drops", 60, 20),
    ]
    i = 0
    while i < len(medicines):
        cur.execute(
            "insert into medicine values(?,?,?,?)",
            (i + 1, medicines[i][0], medicines[i][1], medicines[i][2]),
        )
        i = i + 1
    con.commit()

while True:
    print("\n================================")
    print("          CAMPUSMEDS")
    print("     CAMPUS PHARMACY SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. Buy Medicine")
    print("3. Show Orders")
    print("4. Request New Medicine")
    print("5. Exit")
    print("================================")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n----- ADD STUDENT -----")
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        room = input("Enter Hostel Room: ")
        cur.execute(
            "insert into students values(?,?,?)",
            (student_id, name, room),
        )
        con.commit()
        print("Student added successfully")

    elif choice == "2":
        student_id = input("\nEnter Student ID: ")
        cur.execute("select * from students where id=?", (student_id,))
        student = cur.fetchone()
        if student is None:
            print("Student not found")
            print("Please add student first")
        else:
            total = 0

            print("\n----------- MEDICINES -----------")
            print("ID   MEDICINE                         PRICE   STOCK")
            print("-----------------------------------------------")

            cur.execute("select * from medicine")
            medicines = cur.fetchall()

            i = 0
            while i < len(medicines):
                print(
                    medicines[i][0],
                    "   ",
                    medicines[i][1],
                    " " * (32 - len(medicines[i][1])),
                    "Rs.",
                    medicines[i][2],
                    "   ",
                    medicines[i][3],
                )
                i = i + 1

            while True:
                medicine_id = int(input("\nEnter Medicine ID (0 to finish): "))

                if medicine_id == 0:
                    break

                quantity = int(input("Enter Quantity: "))

                cur.execute("select * from medicine where id=?", (medicine_id,))
                medicine = cur.fetchone()

                if medicine is None:
                    print("Medicine not found")
                elif quantity <= 0:
                    print("Enter a valid quantity")
                elif quantity > medicine[3]:
                    print("Not enough stock")
                else:
                    medicine_total = medicine[2] * quantity
                    cur.execute(
                        "insert into orders values(?,?,?,?,?)",
                        (
                            student_id,
                            medicine[1],
                            quantity,
                            medicine_total,
                            "15 minutes",
                        ),
                    )
                    new_stock = medicine[3] - quantity
                    cur.execute(
                        "update medicine set stock=? where id=?",
                        (new_stock, medicine_id),
                    )
                    total = total + medicine_total
                    print(medicine[1], "added to your order")

                    again = input("Add another medicine? (yes/no): ")
                    if again == "no":
                        break

            if total > 0:
                con.commit()
                print("\n==============================")
                print("Order placed successfully")
                print("Total Amount: Rs.", total)
                print("Delivery Time: 15 minutes")
                print("Medicine will be delivered to your room")
                print("==============================")
            else:
                print("No medicines were added to the order")

    elif choice == "3":
        student_id = input("\nEnter Student ID: ")
        cur.execute("select * from orders where student=?", (student_id,))
        orders = cur.fetchall()
        if len(orders) == 0:
            print("No orders found")
        else:
            print("\n----------- YOUR ORDERS -----------")
            i = 0
            total = 0
            while i < len(orders):
                print("\nMedicine :", orders[i][1])
                print("Quantity :", orders[i][2])
                print("Amount   : Rs.", orders[i][3])
                print("Delivery :", orders[i][4])
                total = total + orders[i][3]
                i = i + 1
            print("\nTotal Amount: Rs.", total)

    elif choice == "4":
        student_id = input("\nEnter Student ID: ")
        cur.execute("select * from students where id=?", (student_id,))
        student = cur.fetchone()
        if student is None:
            print("Student not found")
            print("Please add student first")
        else:
            medicine_name = input("Enter medicine you want: ")
            cur.execute(
                "insert into requests values(?,?,?)",
                (student_id, medicine_name, "7 days"),
            )
            con.commit()
            print("\nRequest submitted successfully")
            print("Requested Medicine:", medicine_name)
            print("Expected Delivery: 7 days")

    elif choice == "5":
        print("\nThank you for using CampusMeds")
        break

    else:
        print("Wrong choice. Please try again.")

con.close()
