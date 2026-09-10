courses = ["Python", "Java", "Web Development"]

print("Learning Management System")

for i, course in enumerate(courses, 1):
    print(i, course)

choice = int(input("Choose a course: "))

print("You enrolled in:", courses[choice - 1])
