import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options = [rock, paper, scissors]

user_choice = int(input("what do you choose 0 for rock, 1, for paper,2 for scissors"))
if 3>user_choice>=0:
  print("your choice "+options[user_choice])
  random = random.randint(0,2)
  print("computer choice"+options[random])

  if user_choice == 0 and random ==0:
    print("match drawn")
  elif user_choice == 0 and random ==1:
    print("computer wins")
  elif user_choice == 0 and random ==2:
    print("person wins")



  if user_choice == 1 and random ==0:
    print("user wins")
  elif user_choice == 1 and random ==1:
    print("match drawn")
  elif user_choice == 1 and random ==2:
    print("computer wins")
else:
  print("incorrect number")
  

