college_courses = {
    "History": "Mr Washington",
    "Maths": "Mr Newton",
    "Science": "Mr Einstein"
}

for key, value in college_courses.items():
    print(f"The course {key} is being taught by {value}")


for _, professor in college_courses.items():
    print(f"the next professor is {professor}")