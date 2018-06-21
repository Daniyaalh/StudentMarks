def get_info(file):
    all_marks = {}
    line = file.readlines()
    if line == "":
        print("Nothing in file")

    else:
        for i in range(len(line)):
            splitted = line[i].strip().split("|")
            all_marks[splitted[0]] = splitted[1:-1]
            #line[i] = splitted[0:-1]

        all_marks.pop("")
        print(all_marks)
        return all_marks

def add_course(all_marks, course_code):
    if course_code not in all_marks:  # What if it already exists?
        all_marks[code] = []

def delete_course(all_marks):
    delete = "csc2122"
    ret = all_marks.pop(delete, None)

    #if ret == None


def delete_mark(all_marks, course_code, name): # Not tested
    if course_code in all_marks:
        for marks in range(len(all_courses[course_code])):
            splitted = marks.split(" ")
            if splitted[0] == name:
                all_courses[course_code].pop(marks)
                
            
def add_mark(all_marks): #Find out where to put the course code, check if exists
    course = "csc263"
    all_marks[course].append("a4 54 54 45")
    print(all_marks)

def save(all_courses): # Need to test
    for course in all_courses:
        file.write(course + "|")

        for marks in all_courses[course]:
            file.write(marks + "|")

        file.write("\n")

def calc_avg(all_marks):
    course = "csc263"
    total_worth = 0
    total_num = 0
    to_calc = all_marks[course]

    for mark in to_calc:
        mark = mark.split(" ")
        total_num += (int(mark[1]) / (int(mark[2]))*  int(mark[3]))
        print(total_num)
        total_worth += int(mark[3])

    print("avg is " + str((total_num/total_worth) * 100))

    
                   
file = open("marksfilenew.txt")
all_marks = get_info(file)
#add_course(all_marks)
add_mark(all_marks)
calc_avg(all_marks)
#delete_course(all_marks)
        
    
