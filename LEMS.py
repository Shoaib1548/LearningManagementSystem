courses = ["Python", "Java", "Web Development"]

name = input("Enter your name: ")

for i, course in enumerate(courses, 1):
    print(i, course)

choice = int(input("Choose a course: "))
course = courses[choice - 1]

progress = int(input("Enter progress (%): "))

print("\nStudent:", name)
print("Course:", course)
print("Progress:", progress, "%")

if progress == 100:
    print("Course Completed!")
else:
    print("Course In Progress")
