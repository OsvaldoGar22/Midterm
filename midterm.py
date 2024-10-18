
# Question 1 - File Processing and Data Analysis
#
# with open('grades.txt', 'r') as file:
#     grades = []
#     
#     for line in file:
#
#         line = line.strip()
#
#         if line == "":
#             continue
#
#         name, grade = line.split()
#         grades.append(int(grade))
#
# avg_grade = sum(grades) / len(grades)
#
# above_avg_grade = 0 
#
# for grade in grades:
#     if grade > avg_grade:
#         above_avg_grade += 1
#
#
# with open('results.txt', 'w') as result_file:
#     result_file.write(f"Average grade: {avg_grade:.2f}\n")
#     result_file.write(f"Number of students scoring above average: {above_avg_grade}\n")

# ---------------------------------------------------------

# Question 2 - Data Transformation 

num_list = [1, 2, 3, 4, 5, 6]


def transform_data(lst):
    squared_vals = []

    for val in lst:
        squared_vals.append(val ** 2)

    squares_sum = sum(squared_vals)

    return squared_vals, squares_sum


squared_vals, squares_sum = transform_data(num_list)

print(f"Squared List: {squared_vals}")
print(f"Sum of Squares: {squares_sum}")



