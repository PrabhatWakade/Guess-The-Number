import random
print("""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
""")
print("""Welcome To Number Guessing game..!!!
I am thinking of a number between 1 to 100.""")
diff=input("Choose the difficulty level from 'Easy' or 'high'\n")
def attempts():
  if diff == "easy":
    return 10
  else :
    return 5
num_at=attempts()

number=random.randint(1,100)
while num_at!=0:
 guess=int(input("Make a guess\n"))
 if guess==number:
    print("Congratulations, You win...!") 
    break
 elif guess < number:
    num_at-=1 
    print("Too Low\n")
 elif guess > number:
    num_at -=1
    print("Too High\n" )
 if num_at==0:
     print("You Lose..!!! try again")
 
