import json

students = []

def display_menu():
    print("\n--- Student Grade Management System ---")
    print("1. Add a Student")
    print("2. Display All Students")
    print("3. Search for a Student")
    print("4. Calculate Grade Statistics")
    print("5. Save Data to file")
    print("6. Load Data From File")
    print("0. Exit")

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter your grade (0-100): "))

    if 0 <= grade <= 100:
        students.append({"name": name, "grade": grade})
        print("Student added successfully.")
    else:
        print("Grade must be between 0 and 100.")

def calculate_statistics():
    if not students:
        print("No student data available.")
        return
    
    grades = [s["grade"] for s in students]
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    print(f"Average Grade: {average:.2f}")
    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest}")

def display_all_students():
    if not students:
        print("No student records to display.")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"Name: {s['name']}, Grade: {s['grade']}")

def search_student():
    name_to_search = input("Enter the student name to search: ")
    found = False
    for s in students:
        if s['name'].lower() == name_to_search.lower():
            print(f"Found student: Name: {s['name']}, Grade: {s['grade']}")
            found = True
            break
    if not found:
        print("Student not found.")

def save_data():
    with open("students.txt", "w") as file:
        for s in students:
            file.write(f"{s['name']},{s['grade']}\n")
    print("Data saved to file.")

def load_data():
    students.clear()
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, grade = line.strip().split(",")
                students.append({"name": name, "grade": float(grade)})
        print("Data loaded from file.")
    except FileNotFoundError:
        print("No data file found. Start by adding students.")
        
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            calculate_statistics()
        elif choice == "5":
            save_data()
        elif choice == "6":
            load_data()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()
