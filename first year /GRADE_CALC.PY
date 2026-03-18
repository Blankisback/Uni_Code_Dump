student_id = input("Enter student ID: ")
task_result = float(input("Enter task result (%): "))
task_weight = float(input("Enter task weighting (%): "))


def calculate_weighted_average(task_result, task_weight):
    weighted_grade = (task_result * task_weight) / 100
    return weighted_grade


final_grade = calculate_weighted_average(task_result, task_weight)


def output_gradebook(student_id, final_grade):
    print("hello {}, your final grade is {}".format(student_id,final_grade))


output_gradebook(student_id, final_grade)
