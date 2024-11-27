def calculate_gpa(grade_table):
    f_gpa=[], ch=[]
    for i in range(len(grade_table)):
        for j in range(len(grade_table)):
            i_gpa=grade_table[i]*grade_table[j]
            f_gpa.append(i_gpa)
            ch.append(grade_table[i])
    s_gpa=sum(f_gpa)
    t_credit_hours = sum(ch)
    gpa = s_gpa / t_credit_hours
    return gpa

grades=[60,70,75,80,55]
credit_hours=[3,3,3,4]
grades_table = [grades][credit_hours]
gpa = calculate_gpa(grades_table)
print("GPA=", gpa)