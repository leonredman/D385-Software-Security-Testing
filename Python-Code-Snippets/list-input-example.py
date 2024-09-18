def get_grades():
  grades = []

  # Loop to get 4 grades from the user as a float and stored in list grades
  for i in range(4):
    grade = float(input(f"Enter grade {i + 1}: "))
    grades.append(grade)

  return grades

if __name__ == '__main__':
  #Get the list of grades
  grades = get_grades()

  # Display the grades as a list after 4 grades entered
  print("The grades you entered are:", grades)

  