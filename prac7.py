


class GradeInputError(Exception):
    """Raised when an invalid grade is entered"""
    pass

def input_grade():
    name=input("Enter student name:")
    if name.lower().strip()=="done":
        return None,None

    score_input=input("Enter score(0-100):")

    try:
        score=int(score_input)
        if (score <0 or score>100):
            raise GradeInputError("Score must be between 0 and 100")
        return name,score
    except ValueError:
        print("Score must be a number.")
        return input_grade()
    except GradeInputError as e:
        print(e)
        input_grade()

def save_grade_to_file(name,score):
    with open("grades.txt","a")as file:
        file.write(f"{name}:{score}\n")

def collect_grade():
    print("Enter student grades. Type 'done' to finish.\n")
    while True:
        name, score=input_grade()
        if name is None:
            break
        save_grade_to_file(name,score)
        print(f"Saves:{name}-{score}")

def read_grades_from_file():
    try:
        with open("grades.txt","r")as file:
            lines=file.readlines()
            if not lines:
                print("No grades recorded yet.\n")
                return
        print("\n--- Student Grades ---")
        for line in lines:
            print(line.strip())
        print("----------------------\n")
    except FileNotFoundError:
        print("No grade file found. Please enter grades first.\n")

def clear_grades_file():
    try:
        with open("grades.txt","w")as file:
            pass
        print("All grades have been cleared!\n")
    except Exception as e:
        print(f"An error occurred while clearing the file: {e}")


def menu():
    while True:
        print("\n===== Student Grades Menu =====")
        print("1. Add Grades")
        print("2. View Grades")
        print("3. Clear All Grades")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            collect_grade()

        elif choice == '2':
            read_grades_from_file()
        elif choice == '3':
            clear_grades_file()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")
if __name__=="__main__":
     menu()