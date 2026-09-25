# I just started Python :sob: crazy first practice lesson
num_students = int(input("Enter the number of students: "))
students = [] # Directory for students

for i in range(num_students): # please work
    name = input(f"Enter name for student {i+1}: ") 
    student_id = input("Enter student ID: ")
    DoB = input("Enter Date of Birth of student: ")
    students.append({"Name": name, "id": student_id, "DoB": DoB})

num_courses = int(input("Enter the number of courses: "))
courses = [] # hope there isnt too much courses for us

for i in range(num_courses):
    courses_id = input(f"Enter the courses number: {i+1}, enter id: ")
    courses_name =  input("Enter courses name: ")
    courses.append({"Course id": courses_id, "name": courses_name})

mark = {} # Although this year is gonna be 8/20, its still scary

print("Courses: ")
for c in courses:
    print(f"ID: {c['id']} | Name: {c['name']}")

selected_course = input("\nSelect a course ID: ")

for c in courses:
    if c['id'] == selected_course:
        course_found = True
        break
if course_found: 
    mark[selected_course] = {}
    print(f"Entering marks for course: {selected_course}")
    for s in students:
        student_mark = input(f"Enter mark for {s['Name']} (ID {s['id']}): ")
        mark[selected_course][s['id']] = student_mark
else:
    print("Error: That course ID does not exist.")
print("\n--- Student Directory ---")
for s in students:
    print(f"ID: {s['id']} | Name: {s['Name']} | DoB: {s['DoB']}")

print("\n--- View Course Marks ---")
check_course = input("Enter the course ID to view marks: ")

if check_course in mark:
    print(f"\nMarks for Course ID: {check_course}")
    for student_id, student_mark in mark[check_course].items():
        # Match the id
        student_name = "Unknown"
        for s in students:
            if s['id'] == student_id:
                student_name = s['Name']
                break
        print(f"Student: {student_name} (ID: {student_id}) | Mark: {student_mark}")
else:
    print("Error: No marks have been entered for that course ID yet.")