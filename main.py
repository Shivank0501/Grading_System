while True:
    Total_subjects=int(input("Total subjects = "))
    #print("Total Subjects =" , Total_subjects)

    Add=0

    for x in range (Total_subjects):
        a  = int(input("Marks = "))
        Add+=a

    print("Your obtained marks = ",Add)

    Total_marks = Total_subjects*100

    y= Add * 100 / Total_marks

    if y>=90:
        print("Your percent = ",y,"%")
        print("Grade = A+")

    elif 90>y>=80:
        print("Your percent = ", y, "%")
        print("Grade = A")

    elif 80>y>=70:
        print("Your percent = ", y, "%")
        print("Grade = B+")

    elif 70>y>=60:
        print("Your percent = ", y, "%")
        print("Grade = B")

    elif 60>y>=50:
        print("Your percent = ", y, "%")
        print("Grade = C")

    elif 50>y>=33:
        print("Your percent = ", y, "%")
        print("Grade = D")

    else:
        print("Your percent = ", y, "%")
        print("Sorry, You are fail")


    w= input("Want to calculate again = yes/no ")
    if w=="no":
        print("Thank You for using Me")
        break











