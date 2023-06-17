def gather_credits(needed_credits, *args):
    courses = {}
    credits = 0
    needed_credits = int(needed_credits)
    for course_name, course_credits in args:
        if credits >= needed_credits:
            break
        if course_name not in courses.keys():
            credits += course_credits
            courses[course_name] = [course_credits]
    credits_shortage = needed_credits - credits
    if credits >= needed_credits:
        sorted_courses = sorted(courses.items(), key=lambda x: (-len(x[1]), x[0]))
        result = ''
        for k, v in sorted_courses:
            result += f"Enrollment finished! Maximum credits: {credits}.\n"
            result += f"Courses: {', '.join(dict(sorted_courses).keys())}"
            return result

    else:
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."



print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
print(gather_credits(
    80,
    ("Basics", 27),
))
