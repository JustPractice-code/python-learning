# # word frequency counter
# sentence = input("Write one sentence : ")
# words = sentence.split()
# freq = {}
# for word in words:
#     freq[word] = freq.get(word, 0) + 1
# for word, count in freq.items():
#     print(f"{word} -> {count}")

# #student scorecard
# students = [
#     {"name": "anuj", "marks": 81},
#     {"name": "jash", "marks": 90},
#     {"name": "parth", "marks": 63}
# ]
# s_students = sorted(students, key=lambda x: x["marks"], reverse=True)
# for s in s_students:
#     print(f"{s['name']} -> {s['marks']}")

# #detecting duplicates
# from collections import Counter
# n = int(input("How many elements do you want to enter: "))
# nums = [int(input("Enter number: ")) for _ in range(n)]
# count = Counter(nums)
# duplicates = [num for num, c in count.items() if c > 1]
# print("Duplicate numbers:", duplicates)

# #group words by first letter
# from collections import defaultdict
# words = defaultdict(list)
# u_words = ["apple", "cars", "bikes", "america", "bangkok", "carera"]
# for w in u_words:
#     words[w[0]].append(w)
# print(dict(words))

#unique words in sentence
# from collections import Counter
# sentence = input("Enter any sentence : ")
# s = sentence.split()
# d = []
# a = Counter(s)
# for i,e in a.items():
#     if e == 1:
#         d.append(i)
# print("Unique words are : ", d)

#character frequency counter
# from collections import Counter
# s = input("Enter any string : ")
# a = Counter(s)
# for k,v in a.items():
#     print(f"{k} appears {v} times.")

#student average calculator
# students = [
#     {"name":"jash",
#      "marks":[10,20,30]
#     },
#     {"name":"pratham",
#      "marks":[12,20,10]
#     },
#     {"name":"parth",
#      "marks":[10,10,30]
#     }
# ]
# avg = []
# total = 0
# for s in students:
#     for m in s["marks"]:
#         total += m
#         c = len(s["marks"])
#     a = round(total/c,2)
#     avg.append(a)
# for s,m in zip(students,avg):
#     print(f"{s["name"]} got an average of {m}.")

#grouping cities by first letter
# from collections import defaultdict
# c_name = ["ahmedabad","mehsana","surat","mumbai","delhi","capetown","Las vegas","goa"]
# city = defaultdict(list)
# for c in c_name:
#     city[c[0]].append(c)
# print(dict(city))

