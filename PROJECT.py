student_list = ["Yüsra Kaya", "Sibel Erman", "Şevval Önder", "Nebo Genç","Elif Küçükkaya"]
lessons = ["Calculus", "Algorithm", "OPP", "Data Structure", "Electronic Circuits",
           "Psychology"]


def lesson_selection():
    lessons_input = input("\nPlease enter lessons do you want to choose: ")
    lessons_list = list(lessons_input.split(","))

    if len(lessons_list) < 3:

        return print("\nYou failed, you must take a minimum 3 and maximum 5 lessons.")
    else:




        lesson = input("Please enter the lesson's name you want to learn passed or not: ")

        if lesson in lessons_list:

            grades = {"midterm": 0, "final": 0, "project": 0}

            midterm = int(input("\nEnter your midterm grade: "))
            grades["midterm"] = midterm
            final = int(input("Enter your final grade: "))
            grades["final"] = final
            project = int(input("Enter your project grade: "))
            grades["project"] = project

            grade = (midterm * 30 + final * 50 + project * 20) / 100

            if grade >= 90:
                return print("\nYour grade is AA.", "you passed the lesson")
            if grade >= 70 and grade < 90:
                return print("\nYour grade is BB.", "you passed the lesson")
            if grade >= 50 and grade < 70:
                return print("\nYour grade is CC.", "you passed the lesson")
            if grade >= 30 and grade < 50:
                return print("\nYour grade is DD.", "you passed the lesson")
            else:
                return print("\nYour grade is FF.", 'You have failed')





for i in range(3):

    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")

    student = name + " " + surname

    if student in student_list:
        print("\n", student, ",", "Welcome")
        lesson_selection()
        break

    if i <= 2:

        print("İnvalid username, Try again.")

    else:

        print("Please try again later.")



