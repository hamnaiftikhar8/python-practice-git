students = [
    {'name': "Alice", 'grade': '100'},
    {'name': "Bill", 'grade': '20'},
    {'name': "Tim", 'grade': '50'}

]

students_sort_grade = sorted(students, key = lambda student : student['grade'] , reverse = False)

print(students_sort_grade)

numbers = [1,2,3,4,5,6,7,8,9,22]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)