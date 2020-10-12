data_valid=False

while data_valid==False:

    grade1=input("Type the grade of the first test: ")
    try:
        grade1=float(grade1)
    except:
        print("Invalid number")
        continue
    
    if grade1<0 or grade1>10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid=True
data_valid=False

while data_valid==False:

    grade2=input("Type the grade of the second test: ")
    try:
        grade2=float(grade2)
    except:
        print("Invalid number")
        continue
    if grade2<0 or grade2>10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid=True

data_valid=False

while data_valid==False:

    total_classes=input("Type the total number of classes: ")
    try:
        total_classes=float(total_classes)
    except:
        print("Invalid number")
        continue
        
    if total_classes<=0:
        print("The number of classes can't be zero or less")
        continue
    else:
        data_valid=True

data_valid=False

while data_valid==False:

    absences=input("Type the number of absences: ")
    try:
        absences=float(absences)
    except:
        print("Invalid number")
        continue
    
    if absences<0 or absences>total_classes:
        print("The number of absences can't be less than zero or greater than the number of total classes.")
        continue
    else:
        data_valid=True

        


average_grade=(grade1+grade2)/2
attendance=(total_classes-absences)/total_classes

print("Average grade: ", round(average_grade,2))
print("attendance: ", str(round((attendance*100),2))+"%")

if(average_grade>=6):
    if(attendance>=0.8):
        print("The student has been approved")
    else:
        print("The student has failed due to an attendance rate lower than 80%")

elif(attendance>=0.8):
    print("The student has failed due to an average grade lower than 6.0")

else:
    print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%")
    
