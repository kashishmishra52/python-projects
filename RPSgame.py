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

#Write your code below this line 
import random
choose=int (input("type 0 for rock, 1 for paper , 2 for scissors"))
if choose==0:
    print(rock)
elif choose==1:
    print(paper)
elif choose==2:
    print(scissors)
else:
    print("you have entered a wrong choice")
print("computer choose")
computer=random.randint(0,2)
if computer==0:
    print(rock)
elif computer==1:
    print(paper)
elif computer==2:
    print(scissors)
else:
    print("you have entered a wrong choice")
if computer == choose :
    print("its an draw")
elif choose == 0 and computer==1:
    print ("computer wins")
elif choose == 1 and computer == 2:
    print("computer wins")
elif choose ==2 and computer == 0:
    print("computer wins")
else :
    print("you win")