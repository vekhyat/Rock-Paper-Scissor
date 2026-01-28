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
b=int(input('Choose rock(0),paper(1) or scissors(2)'))
print('You chose')
if b==0:
    print(rock)
elif b==1:
    print(paper)
elif b==2:
    print(scissors)

print("Computer chose")

if a==0:
    print(rock)
elif a==1:
    print(paper)
elif a==2:
    print(scissors)



if a==2 and b==0:
    print("You win")
elif b==2 and a==0:
    print('Computer wins')
elif a>b:
    print("Computer wins")
elif b>a:
    print("You win")
else:
    print("Its a draw")




