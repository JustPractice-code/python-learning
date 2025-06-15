def call_app(subjects):
    marks = []
    name = input("Enter your name : ")
    for i in subjects:
        try:
            mark = int(input(f"Enter your marks for {i} : "))
            marks.append(mark)
        except ValueError:
            print("Please enter correct marks.")
    print("Saved successfuly")
    save_to_file(name, marks, subjects)

def take_sub():
    subjects = []
    number = int(input("How many subjects do you want to enter : "))
    for i in range(number):
        subject = input("Enter subject name : ")
        subjects.append(subject)
    call_app(subjects)

def save_to_file(name, marks, subjects):
    with open("st_record.txt","a") as f:
        f.write("\nNew record : ")
        f.write(f"\nStudent name : {name}")
        f.write("\nMarks details with subject : ")
        for mark,subject in zip(marks,subjects):
            f.write(f"\n{mark} in {subject}")
        f.write("\n")
    read_file()

def read_file():
    try:
        with open("st_record.txt","r") as f:
            for line in f.readlines():
                print(line,end='')
    except FileNotFoundError:
        print("Your data is not recorded.")

take_sub()