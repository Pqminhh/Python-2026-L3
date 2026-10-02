import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  
        self.gpa = 0.0

    def calculate_gpa(self, courses):
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