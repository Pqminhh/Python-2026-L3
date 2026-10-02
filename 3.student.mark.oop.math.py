import curses
import math
import numpy as np

# Although this year requirement is gonna be 8/20, its still scary
class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  #store
        self.gpa = 0.0

    def calculate_gpa(self, courses):
        #numpy moment
        mark_list = []
        credit_list = []
        
        for course in courses:
            if course.id in self.marks:
                mark_list.append(self.marks[course.id])
                credit_list.append(course.credits)
                
        if not credit_list:
            self.gpa = 0.0
            return

        marks_array = np.array(mark_list)
        credits_array = np.array(credit_list)
        self.gpa = np.sum(marks_array * credits_array) / np.sum(credits_array)


class Course:
    def __init__(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits


def get_input(stdscr, prompt):
    stdscr.addstr(prompt)
    curses.echo()
    user_input = stdscr.getstr().decode('utf-8').strip()
    curses.noecho()
    return user_input


def main(stdscr):
    curses.curs_set(1)
    stdscr.clear()
    
    students = []
    courses = []

    #Students
    try:
        num_students = int(get_input(stdscr, "Enter the number of students: "))
    except ValueError:
        num_students = 0

    for i in range(num_students):
        stdscr.clear()
        stdscr.addstr(f"--- Entering Student {i+1} ---\n")
        name = get_input(stdscr, "Enter name: ")
        s_id = get_input(stdscr, "Enter student ID: ")
        dob = get_input(stdscr, "Enter Date of Birth: ")
        students.append(Student(s_id, name, dob))

    #Courses
    stdscr.clear()
    try:
        num_courses = int(get_input(stdscr, "Enter the number of courses: "))
    except ValueError:
        num_courses = 0

    for i in range(num_courses):
        stdscr.clear()
        stdscr.addstr(f"--- Entering Course {i+1} ---\n")
        c_id = get_input(stdscr, "Enter course ID: ")
        name = get_input(stdscr, "Enter course name: ")
        try:
            credits = float(get_input(stdscr, "Enter course credits (e.g. 3): "))
        except ValueError:
            credits = 1.0
        courses.append(Course(c_id, name, credits))

    #Main Menu 
    while True:
        stdscr.clear()
        stdscr.addstr("=== STUDENT MARK MANAGEMENT SYSTEM ===\n", curses.A_BOLD)
        stdscr.addstr("1. Enter marks for a course\n")
        stdscr.addstr("2. View Students & GPA\n")
        stdscr.addstr("3. View Courses\n")
        stdscr.addstr("4. Calculate GPA & Sort Students Descending\n")
        stdscr.addstr("5. Exit\n")
        
        choice = get_input(stdscr, "Select an option (1-5): ")

        if choice == '1':
            stdscr.clear()
            stdscr.addstr("--- Select a Course ---\n")
            for c in courses:
                stdscr.addstr(f"ID: {c.id} | Name: {c.name} | Credits: {c.credits}\n")
            
            selected_course = get_input(stdscr, "\nEnter course ID to enter marks: ")
            
            course_obj = next((c for c in courses if c.id == selected_course), None)
            if course_obj:
                stdscr.addstr(f"\nEntering marks for course: {course_obj.name}\n")
                for s in students:
                    try:
                        raw_mark = float(get_input(stdscr, f"Enter mark for {s.name} (ID {s.id}): "))
                        # Use math module to round down 
                        s.marks[selected_course] = math.floor(raw_mark * 10) / 10
                    except ValueError:
                        stdscr.addstr("Invalid mark! Skipping...\n")
            
            stdscr.clear()
            if not course_obj:
                stdscr.addstr("Error: That course ID does not exist.\n")
                
            stdscr.addstr("\nPress any key to return to the menu...")
            stdscr.getch()

        elif choice == '2':
            stdscr.clear()
            stdscr.addstr("--- Student Directory ---\n")
            for s in students:
                stdscr.addstr(f"ID: {s.id} | Name: {s.name} | DoB: {s.dob} | GPA: {s.gpa:.2f}\n")
                if s.marks:
                    stdscr.addstr("  Marks: ")
                    for cid, m in s.marks.items():
                        stdscr.addstr(f"[{cid}: {m}] ")
                    stdscr.addstr("\n")
            stdscr.addstr("\nPress any key to return to the menu...")
            stdscr.getch()

        elif choice == '3':
            stdscr.clear()
            stdscr.addstr("--- Courses ---\n")
            for c in courses:
                stdscr.addstr(f"ID: {c.id} | Name: {c.name} | Credits: {c.credits}\n")
            stdscr.addstr("\nPress any key to return to the menu...")
            stdscr.getch()

        elif choice == '4':
            for s in students:
                s.calculate_gpa(courses)
            
            #Sort
            students.sort(key=lambda x: x.gpa, reverse=True)
            
            stdscr.clear()
            stdscr.addstr("Calculated GPA and sorted students descending by GPA!\n")
            stdscr.addstr("Navigate to Option 2 to view the results.\n")
            stdscr.addstr("\nPress any key to return to the menu...")
            stdscr.getch()

        elif choice == '5':
            break

if __name__ == "__main__":
    #Decorate
    curses.wrapper(main)