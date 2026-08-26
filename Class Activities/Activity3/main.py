from class_classes import Classroom

def menu():
    while True:
        print("\n****************** Main Menu ********************")
        print("1. Create a New Class")
        print("2. Add a Student to a Class")
        print("3. Find a Student in a Class")
        print("4. Quit")
        try:
            menu_option = int(input("Select an option: "))
            if 1 <= menu_option <= 4:
                return menu_option
            print("Please select a valid option from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def select_classroom(classrooms):
    if not classrooms:
        print("\n[!] No classrooms exist yet. Please create a class first (Option 1).")
        return None
    
    print("\n--- Select a Classroom ---")
    for idx, c in enumerate(classrooms, 1):
        print(f"{idx}. {c.class_title}")
    
    try:
        choice = int(input("Choose classroom number: ")) - 1
        if 0 <= choice < len(classrooms):
            return classrooms[choice]
        print("Invalid classroom choice.")
    except ValueError:
        print("Invalid input.")
    return None

def main():
    classrooms = []
    while True:
        menu_option = menu()
        
        if menu_option == 4:
            print("Exiting application. Good luck!")
            break
            
        elif menu_option == 1:
            title = input("Enter the title of your class: ")
            classrooms.append(Classroom(title))
            print(f"Class '{title}' created successfully!")
            
        elif menu_option == 2:
            target_class = select_classroom(classrooms)
            if target_class:
                fname = input("First Name: ")
                sname = input("Surname: ")
                dob = input("DOB (DD/MM/YYYY): ")
                gender = input("Gender: ")
                target_class.add_student(fname, sname, dob, gender)
                print(f"Added {fname} {sname} to {target_class.class_title}!")
                
        elif menu_option == 3:
            target_class = select_classroom(classrooms)
            if target_class:
                search_dob = input("Enter student DOB to search (DD/MM/YYYY): ")
                student = target_class.find_student(search_dob)
                if student:
                    print(f"\n[Found] {student.student_first_name} {student.student_surname} | DOB: {student.student_dob} | Gender: {student.student_gender}")
                else:
                    print("No student found with that DOB in this classroom.")

if __name__ == "__main__":
    main()