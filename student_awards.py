# Name: Thanussha Sri Ganeson
# File Name: student_awards.py
# Description: This Python app accepts student names and GPAs and determines if they qualify for the Dean's List or the Honor Roll.

def main():
    print("Welcome to the Student Awards App!")
    print("Enter 'ZZZ' for the last name to quit.")

    while True:
        last_name = input("\nEnter student's last name: ")
        if last_name == 'ZZZ':
            print("Exiting...")
            break

        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"Sorry, {first_name} {last_name} did not qualify for any awards.")

if __name__ == "__main__":
    main()
