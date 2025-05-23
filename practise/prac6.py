class FindError(Exception):
    """Raised when there is invalid marks input"""
    pass
grades={}
def input_grades():

    try:
        while True:

            stud_name=input("Enter student name:")
            if stud_name.lower()=="done":
                break
            score_input=(input("Enter mark: "))
            # Try to convert a score to an integer
            try:
                score=int(score_input)
            except ValueError:
                raise ValueError("Mark must be a number.")

            #Check for valid score range
            if score <0 or score >100:
                raise FindError("Enter score within 0 and 100!")

            grades[stud_name]=score
    except FindError as e:
        print(f"enter a number: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")


    finally:
        print("Grade entry session ended.")

def display_grades():
    input_grades()
    if grades:
        print("\nStudent Grades:")
        for student, mark in grades.items():
            print(f"{student}: {mark}")
    else:
        print("No grades to display")
display_grades()
