if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_grades = list(student_marks[query_name])
    grades_sum = 0
    for i in student_grades:
        grades_sum += i
    print("%.2f" % round(grades_sum/len(student_grades),2))
