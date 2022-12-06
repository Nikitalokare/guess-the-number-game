from random import randint
num = randint(1,3)
print('''Please select the Number between 1 to 10
    You Have only Three Chances!!!
    All the Best!!!''')
for x in range (0,3):
    noFromUser = int(input("Enter a guess: "))
    if(num == noFromUser):
        print("Congratulation!!! You guess the right number")
        break
    else:
        print("oh no you guess a wrong number")
else:
    print("Three chances are over,Better luck next time")