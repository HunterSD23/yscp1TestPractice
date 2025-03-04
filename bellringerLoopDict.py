grade1 = int(input("Please Input Jeff's grade: "))
grade2 = int(input("Please Input George's grade: "))
grade3 = int(input("Please Input Paul's grade: "))
grade4 = int(input("Please Input Kayla's grade: "))
grade5 = int(input("Please Input Bob's grade: "))
grade6 = int(input("Please Input Hunter's grade: "))
grade7 = int(input("Please Input Eva's grade: "))
grade8 = int(input("Please Input Hannah's grade: "))
grade9 = int(input("Please Input Gavin's grade: "))
grade10 = int(input("Please Input Cameron's grade: "))


grades = {"Jeff": grade1, "George": grade2, "Paul": grade3, "Kayla": grade4, "Bob": grade5, "Hunter": grade6, "Eva": grade7, "Hannah": grade8, "Gavin": grade9, "Cameron": grade10}

for student, grade in grades.items():
    print(f'{student}: {grade}')