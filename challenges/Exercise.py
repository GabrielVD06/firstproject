if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
students.sort(key=lambda x: x[1], reverse=True)
count = -2
delete = -1
newStudents = []

while students[count][1] == students[-1][1]:
    count -= 1
    delete -= 1
students = students[:delete]
count = -1
while students[count][1] == students[-1][1]:
    newStudents.append(students[count][0])
    newStudents.sort()
    count -= 1
    if count < -len(students):
        break
count = 0
while count < len(newStudents):
    print(newStudents[count])
    count += 1