# grocery = []
# while True:
#     print("Options : \n1. add an item\n2. Remove an item\n3. Show the list\n4. exit")
#     opt = int(input("Enter the choice number : "))
#     if opt == 1:
#         item = input("Enter item : ")
#         grocery.append(item)
#         print("Item added")
#     elif opt == 2:
#         item = input("Enter item : ")
#         if item in grocery:
#             grocery.remove(item)
#             print("Item removed")
#         else:
#             print("No such item found")
#     elif opt == 3:
#         for item in grocery:
#             print(item)
#     elif opt == 4:
#         break
#     else:
#         print("Wrong input!")

# s = input("Enter any string")
# i = len(s) - 1
# j = []
# while(i>=0):
#     j.append(s[i])
#     i -= 1
# a = ''.join(j)
# print(a)

# sent = input("Enter a long sentence : ")
# a = sent.split(' ')
# print(len(a))

# num = []
# for i in range(1,6):
#     a = int(input("Enter any number : "))
#     num.append(a)
# a = len(num) - 1
# for i in range(a):
#     if num[i] > num[i+1]:
#         temp = num[i]
#         num[i] = num[i+1]
#         num[i+1] = temp
# print(num[a])

#quiz app logic
score = 0
questions = [
    {
        'que':"What is Vijay Mallya best known for in the business world?",
        'option':[{'A': "A - Bollywood films",'B':"Software development",'C':"Liquor and airline industry",'D':"Real estate"}],
        'answer':'C'
    },
    {
        'que':"Which airline was founded by Vijay Mallya?",
        'option':[{'A': "A - SpiceJet",'B':"B - Kingfisher Airlines",'C':"C - GoAir",'D':"D - AirAsia India"}],
        'answer':'B'
    },
    {
        'que':"Vijay Mallya is often referred to by what nickname in the media?",
        'option':[{'A': "A - Tech Tycoon",'B':"B - Beer Baron",'C':"C - Oil King",'D':"D - Market Guru"}],
        'answer':'B'
    },
    {
        'que':"Which Indian company was Vijay Mallya the chairman of?",
        'option':[{'A': "A - Tata Group",'B':"B - Infosys",'C':"C - United Breweries Group",'D':"D - Larsen & Toubro"}],
        'answer':'C'
    },
    {
        'que':"Why is Vijay Mallya wanted by Indian authorities?",
        'option':[{'A': "A - Tax evasion",'B':"B - Insider trading",'C':"C - Bank fraud and money laundering",'D':"D - Environmental violations"}],
        'answer':'C'
    }
]
for que in questions:
    print(que['que'])
    print("Select any one option from given below : ")
    for opt in que['option']:
        print(opt['A'])
        print(opt['B'])
        print(opt['C'])
        print(opt['D'])
    ans = input("Enter your choice : ")
    if ans.upper() in que['answer']:
        score += 1
    
print("Your score is : ",score)