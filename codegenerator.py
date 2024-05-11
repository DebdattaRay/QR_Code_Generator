import qrcode
import json
import mysql.connector

def generate_qr_code(student_details):
    # Convert student details to JSON
    json_data = json.dumps(student_details)

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(json_data)
    qr.make(fit=True)

    # Create QR code image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save("student_qr.png")
    print("QR Code generated successfully.")

def create_students_table(cursor):
    # SQL code to create Students table
    sql = """
    CREATE TABLE IF NOT EXISTS Students (
        name VARCHAR(255) NOT NULL,
     address VARCHAR(255) NOT NULL,
     parent_contact INT NOT NULL,
     aadhar_card_number INT  NOT NULL,
     roll_number INT PRIMARY KEY NOT NULL,
     photo_path VARCHAR(255) NOT NULL
    )
    """
    cursor.execute(sql)
    print("Students table created successfully.")

def save_to_database(student_details):
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )

        cursor = connection.cursor()

        # Create Students table if not exists
        create_students_table(cursor)

        # Insert student details into the database
        sql = "INSERT INTO Students (name, address, parent_contact, aadhar_card_number, roll_number, photo_path) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (student_details["name"], student_details["address"], student_details["parent_contact"], student_details["aadhar_card_number"], student_details["roll_number"], student_details["photo_path"])
        cursor.execute(sql, val)

        # Commit changes and close connection
        connection.commit()
        print("Student details saved to the database.")
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table:", error)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def main():
    # Input student details
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    parent_contact = input("Enter your parent's contact number: ")
    aadhar_card_number = input("Enter your Aadhar card number: ")
    roll_number = input("Enter your roll number: ")
    photo_path = input("Enter the path to your photo: ")

    # Store student details in a dictionary
    student_details = {
        "name": name,
        "address": address,
        "parent_contact": parent_contact,
        "aadhar_card_number": aadhar_card_number,
        "roll_number": roll_number,
        "photo_path": photo_path
    }

    # Save student details to the database
    save_to_database(student_details)

    # Generate QR code for student details
    generate_qr_code(student_details)

if _name_ == "_main_":
    main()