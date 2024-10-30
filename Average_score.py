students = {'Настя', 'Владимир', 'Алексей', 'Михаил', 'Женя'}
sorted_students = sorted(students)
grades =  [[5, 3, 4, 5, 4], [2, 2, 2, 5, 3], [4, 5, 5, 2], [4, 4, 3, 2], [5, 3, 5, 4, 5]]

average = sum(grades[0]) / len(grades[0])
print('Студенты: ', sorted_students[0], average)

average_1 = sum(grades[1]) / len(grades[1])
print('Студенты: ', sorted_students[1], average_1)

average_2 = sum(grades[2]) / len(grades[2])
print('Студенты: ', sorted_students[2], average_2)

average_3 = sum(grades[3]) / len(grades[3])
print('Студенты: ', sorted_students[3], average_3)

average_4 = sum(grades[4]) / len(grades[4])
print('Студенты: ', sorted_students[4], average_4)

