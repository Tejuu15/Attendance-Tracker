from datetime import datetime

students = ["Alice", "Bob", "Charlie"]

def mark_attendance():
    date = datetime.now().strftime("%Y-%m-%d")

    with open("attendance.txt", "a", encoding="utf-8") as file:
        file.write(f"\n--- {date} ---\n")

        for student in students:
            status = input(f"{student} (P/A): ").upper()

            if status == "P":
                record = "Present"
            else:
                record = "Absent"

            file.write(f"{student}: {record}\n")

    print("✅ Attendance recorded!\n")

def view_attendance():
    try:
        with open("attendance.txt", "r", encoding="utf-8") as file:
            print("\n=== Attendance Records ===\n")
            print(file.read())
    except FileNotFoundError:
        print("No attendance records found.\n")

def main():
    while True:
        print("1. Mark Attendance")
        print("2. View Records")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()