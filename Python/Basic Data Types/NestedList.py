"""Given the names and grades for each student in a Physics class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second 
lowest grade.

Note: If there are multiple students with the same grade, order their names 
alphabetically and print each name on a new line."""

if __name__ == '__main__':
    nested_list = []
    lowest_grade = 99999
    second_lowest_grade = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < lowest_grade :
            second_lowest_grade = lowest_grade
            lowest_grade = score 
        elif score > lowest_grade and score < second_lowest_grade:
            second_lowest_grade = score
        nested_list.append([name,score])
    nested_list = sorted(nested_list,reverse=True,key = lambda x:x[1])
    second_list = list(filter(lambda x: x[1] == second_lowest_grade, nested_list))
    second_list = sorted(second_list,key = lambda x: x[0])
    for i in second_list:
        print(i[0])