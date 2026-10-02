import curses
                    #Main Menu
def show_menu(stdscr):
    stdscr.clear()
    stdscr.addstr("=== STUDENT MARK MANAGEMENT SYSTEM ===\n", curses.A_BOLD)
    stdscr.addstr("1. Enter marks for a course\n")
    stdscr.addstr("2. View Students & GPA\n")
    stdscr.addstr("3. View Courses\n")
    stdscr.addstr("4. Calculate GPA & Sort Students Descending\n")
    stdscr.addstr("5. Exit\n")

def display_students(stdscr, students):
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

def display_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr("--- Courses ---\n")
    for c in courses:
        stdscr.addstr(f"ID: {c.id} | Name: {c.name} | Credits: {c.credits}\n")
    stdscr.addstr("\nPress any key to return to the menu...")
    stdscr.getch()