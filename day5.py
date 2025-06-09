# def _3sum(a,b,c):
#     return a+b+c
# print(_3sum(10,20,30))

# def check_num(a):
#     if a%2==0:
#         print("Even")
#     else:
#         print("Odd")
# check_num(10)

# def check_palindrome(word):
#     a = []
#     for i in range(len(word)-1,-1,-1):
#         a.append(word[i])
#     b = ''.join(a)
#     if b == word:
#         print("Yes")
#     else:
#         print("No")
# check_palindrome("jash")

#student result analyzer logic
name = input("Enter your name : ")
sub_list = ["Maths","Physics","Chemistry","Biology","Computer"]
marks = []
for sub in sub_list:
    mark = int(input(f"Enter your marks for {sub} : "))
    marks.append(mark)

def total_marks(mark_list):
    sum = 0
    for i in mark_list:
        sum += i
    return sum

tm = total_marks(marks)

def percentage(total_marks, sub_list):
    a = len(sub_list)
    full_marks = a * 100
    per = (total_marks/full_marks) * 100
    return per

percent = percentage(tm, sub_list)

def grade(percent):
    if percent >=80 and percent <= 100:
        return 'a'
    elif percent >=60 and percent <=79:
        return 'b'
    elif percent >=40 and percent <= 59:
        return 'c'
    elif percent >=34 and percent <= 39:
        return 'd'
    else:
        return 'f'

gr = grade(percent)

def result(gr):
    if gr == 'f':
        return "Fail"
    else:
        return "Pass"

res = result(gr)

print("Your report Card : ")
print(f"Your name : {name}")
print(f"Your Total marks : {tm}")
print(f"Your percentage : {percent}")
print(f"Your Grade : {gr}")
print(f"Your Final Result : {res}")
