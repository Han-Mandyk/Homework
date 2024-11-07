students = {'Настя', 'Владимир', 'Алексей', 'Михаил', 'Женя'}
sorted_students = sorted(students)
grades =  [[5, 3, 4, 5, 4], [2, 2, 2, 5, 3], [4, 5, 5, 2], [4, 4, 3, 2], [5, 3, 5, 4, 5]]
average = []
i = 0
while i < len(grades):
    average_1 = sum(grades[i]) / len(grades[i])
    average.append(average_1)
    print('Студенты: ', sorted_students[i], average[i])
    i += 1
    continue

