date = input("Enter date (dd-mm-yy): ")
title = input("Enter title : ")
description = input("Enter content : ")
with open("diary.txt","a") as d:
    d.write(f"\nDate : {date}")
    d.write(f"\nTitle : {title}")
    d.write(f"\nDescription : {description}\n")
    
with open("diary.txt","r") as d:
    a = d.readlines()
    for i in a:
        print(i)
