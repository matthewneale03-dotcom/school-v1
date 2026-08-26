from subjects import Subject

subjects = []

def main():
    while True:
        print("\n=== Subject Management UI ===")
        print("1. Add a Subject")
        print("2. View a Chosen Subject")
        print("3. View All Subjects")
        print("4. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter subject name: ")
            year = input("Enter year level: ")
            code = input("Enter class code: ")
            enrolled = input("Enter enrolled students count: ")
            subjects.append(Subject(name, year, code, enrolled))
            print("Subject added successfully!")

        elif choice == "2":
            code = input("Enter class code to search: ")
            found = False
            for s in subjects:
                if s.code.lower() == code.lower():
                    s.display_details()
                    found = True
                    break
            if not found:
                print("Subject not found.")

        elif choice == "3":
            if not subjects:
                print("No subjects registered yet.")
            else:
                print("\n--- All Subjects ---")
                for s in subjects:
                    s.display_details()

        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose between 1-4.")

if __name__ == "__main__":
    main()
    