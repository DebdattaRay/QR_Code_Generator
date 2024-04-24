import qrcode
import json

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

    # Generate QR code for student details
    generate_qr_code(student_details)

if __name__ == "__main__":
    main()
