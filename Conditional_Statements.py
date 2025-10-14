# if condition
#elif condition
#else condition


# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# if a > b:
#     print(f"a is greater than b: {a}")
# elif a == b:
#     print(f"a is equal to b: {a}")
# else:
#     print(f"b is greater than a: {b}")



# a=int(input("enter a number 1:"))
# b=int(input("enter a number 2:"))
# c=int(input("enter a number 3:"))
# if a > b and a > c:#check if a is greater than b and c
#     print(f"a is the greatest: {a}")
# elif b > a and b > c:#check if b is greater than a and c
#     print(f"b is the greatest: {b}")
# else:
#     print(f"c is the greatest: {c}")

# a=100
# if a<10:
#     print("a is above 10")
#     if a>200:
#         pass # we can't empty a condition so we use 'pass'
#     else:
#         print(" 200 is big")
# else:
#     print("sorry")

# a=1
# if a<10:
#     print("a is above 10")
#     if a>200:
#         pass 
#     else:
#         print(" 200 is big")
# else:
#     print("sorry")


coursework = "English"
score_theory = 53
score_practical = 35

if coursework == "Science" or coursework == "science":
    if score_theory > 50:
        print("Please check the input score for 'Science: Theory'.")
    elif score_practical > 50:
        print("Please check the input score for 'Science: Practical'.")
    else:
        print("Score validated for Science. Your total is:", score_theory + score_practical)

elif coursework == "English" or coursework == "english":
    if score_theory > 60:
        print("Please check the input score for 'English: Theory'.")
    elif score_practical > 40:
        print("Please check the input score for 'English: Practical'.")
    else:
        print("Score validated for English. Your total is:", score_theory + score_practical)

else:
    print("Coursework not recognised. please enter score for either science or english.")

