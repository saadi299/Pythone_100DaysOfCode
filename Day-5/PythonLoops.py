
# fruits=['Apple','Banana','Mango']
# for fruit in fruits:
#     print(fruit)

#Average Height Calculation------------------------------------------

# student_heights = [180, 124, 165, 173, 189, 169, 146]
# # total_heights=0
# # total_students=0
# # for height in student_heights:
# #     total_heights+=height
# # print(total_heights)
# #
# # for student in student_heights:
# #     total_students+=1
# # print(total_students)
# # average_height=round(total_heights/total_students)
# # print(average_height)


#Highest-Score Calculation---------------------------------

# student_scores = [78, 65, 89, 186, 55, 91, 64, 89]
# highest_score=0
#
# for student_score in student_scores:
#     if student_score>highest_score:
#         highest_score=student_score
# print(f"Highest Score= {highest_score}")


# For in Range (Sum 1 to 100)----------------------------
# total=0
# for number in range(1,101):
#     total+=number
# print(total)

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100----------------------------

# total=0
# for number in range(2,101,2):
#     print(number)
#     total+=number
# print(total)


#The Fizz Buzz Problem--------------------------------------
for number in range(1,101):
    if (number%3==0) and (number%5==0):
        print("fizzBuzz")
    elif(number%5==0):
        print("buzz")
    elif (number%3==0):
        print("fizz")
    else:
        print(number)









