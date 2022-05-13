student_name=[]
student_grade=[]


def add():
    while (1):
        name=input("Please enter student's name: ")
        student_name.append(name)
        grade=int(input("Please enter student's grade: "))
        student_grade.append(grade)
        print(student_name)
        print(student_grade)
        a=input("Do you want to keep adding grades for students? (Y/N): ")
        if a=="Y":
            continue
        else:
            break
add()

data={student_name[i]:student_grade[i] for i in range(len(student_name))}
print(data)
    
def search_function():
  while(1):
    name=input("Please enter the name of the student: ")
    if name not in data:
      print("Not available. Please try again!")
    else:
      print("The grade received by", name, "is", data[name], "\n\nThank you for using my program!")
      break
    
Choice=input("Do you want to search a grade of a student?(Y/N): ")
if Choice=="Y":
  search_function()
else:
  print("Thank you for using my program!")
    