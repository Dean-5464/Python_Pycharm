def calculate_average():
    first_score = float(input("Please Input Your First Test Score >>> "))
    second_score = float(input("Please Input Your Second Test Score >>> "))
    third_score = float(input("Please Input Your Third Test Score >>> "))
    fourth_score = float(input("Please Input Your Fourth Test Score >>> "))
    fifth_score = float(input("Please Input Your Fifth Test Score >>> "))

    average_score = (first_score + second_score + third_score + fourth_score + fifth_score) / 5

    print("Your average Score Is:", average_score)


def determine_grade():

    score = float(input("Please Enter The Score That You Want Graded >>> "))

    if score >= 90:
        grade = "A"
    elif 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    elif 60 <= score < 70:
        grade = "D"
    elif score < 60:
        grade = "F"

    print("Your Letter Grade is:", grade)


calculate_average()

determine_grade()
