def study_schedule(permanence_period, target_time):
    students_in_time = 0
    if type(target_time) != int:
        return None
    else:
        for student in permanence_period:
            if type(student[0]) != int or type(student[1]) != int:
                return None
            if student[0] <= target_time <= student[1]:
                students_in_time += 1
        return students_in_time
