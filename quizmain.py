
import random as rd
print("----Greeting project----")
list="Hello","Hi","Hey","Howdy","Greetings","Salutations","Good day",
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
def greeting(first_name, last_name):
  if(len(first_name)+len(last_name)>10):
    print("Name is too long")
  else:
    print(rd.choice(list), first_name, last_name,"You just developed into python.")

greeting(first_name, last_name)


# task 2
print("\n")
print("----Runner up score project----")
no_of_participants=int(input("Enter no of participants: "))
def runner_up_score():
  score_list=[]
  for i in range(no_of_participants):
    score=int(input("Enter score for " + str(i+1) + " runner up: "))
    score_list.append(score)
  print("runner up score is ",5)
runner_up_score()
