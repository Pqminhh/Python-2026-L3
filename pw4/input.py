import curses
import math
from domains.student import Student
from domains.course import Course

def get_input(stdscr, prompt):
    stdscr.addstr(prompt)
    curses.echo()
    user_input = stdscr.getstr().decode('utf-8').strip()
    curses.noecho()
    return user_input

def input_students(stdscr, students):
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

def input_courses(stdscr, courses):
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

def input_marks(stdscr, students, courses):
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
                s.marks[selected_course] = math.floor(raw_mark * 10) / 10
            except ValueError:
                stdscr.addstr("Invalid mark! Skipping...\n")
    else:
        stdscr.addstr("\nError: That course ID does not exist.\n")
    
    stdscr.addstr("\nPress any key to return to the menu...")
    stdscr.getch()