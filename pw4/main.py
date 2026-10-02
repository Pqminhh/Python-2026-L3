import curses
from input import get_input, input_students, input_courses, input_marks
from output import show_menu, display_students, display_courses

def main(stdscr):
    curses.curs_set(1)
    stdscr.clear()
    
    students = []
    courses = []

    input_students(stdscr, students)
    input_courses(stdscr, courses)

    while True:
        show_menu(stdscr)
        choice = get_input(stdscr, "Select an option (1-5): ")

        if choice == '1':
            input_marks(stdscr, students, courses)
            
        elif choice == '2':
            display_students(stdscr, students)

        elif choice == '3':
            display_courses(stdscr, courses)

        elif choice == '4':
            for s in students:
                s.calculate_gpa(courses)
            
            students.sort(key=lambda x: x.gpa, reverse=True)
            
            stdscr.clear()
            stdscr.addstr("Calculated GPA and sorted students descending by GPA!\n")
            stdscr.addstr("Navigate to Option 2 to view the results.\n")
            stdscr.addstr("\nPress any key to return to the menu...")
            stdscr.getch()

        elif choice == '5':
            break

if __name__ == "__main__":
    curses.wrapper(main)
    