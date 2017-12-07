"""
1. Write a program that prints out a statement of your choosing.
2. Write a program that asks a question, takes a response, and then prints out that response.
3. Write a program that gives a user a choice, takes in that choice, and then outputs a
statement based on that choice.
4. Write a program that contains a two if statements.
5. Write a program that contains a loop.
"""
import time
#1, 2, 3, and 4a
name = input("Hey! I'm Karel! What's your name?\n")
print("Well hello there, {}!  I'm gonna run you through a few basic things you can do with Python 3!  Beep!".format(name))
time.sleep(3)
print("Let's begin by giving you a choice and printing out a statement based on that choice.\n")
choice = input("Which flavor of ice cream do you prefer, chocolate or vanilla? c or v\n")
if choice == "c":
    print("Really?  Me too!  Chocolate is the best!  Beep boop!")
elif choice == "v":
    print("That's cool...but I'm more of a chocolate kind of person.  Beep beep.")
else:
    print("That wasn't really an option...")
time.sleep(3)
#4b
print("\nWasn't that fun?  Now, we're going to do something that requires the use of another if statement.  Beep!")
choice = input("Do you prefer dogs or cats? d or c\n")
if choice == "d":
    print("Hm...I guess that's alright.  I'm more of a robot kind of person.  Boop beep!")
if choice == "c":
    print("Yeah, cats are pretty cool, but robots are definitely cooler!  Boop!")
time.sleep(3)
#5
print("\nAlright, now for the final part!  We've gotta do something that involves a loop!")
print("So here's what's gonna happen.  I'm gonna spit out every number between 1 and 100.")
time.sleep(3)
print("But, if the number is a multiple of 3, I will say Fizz instead of the number.")
time.sleep(3)
print("Also, if the number is a multiple of 5, I will say Buzz instead of the number.")
time.sleep(3)
print("Finally, if the number is a multiple of both 3 and 5, I will say FizzBuzz instead of the number.  I'll start in 5 seconds!")
time.sleep(5)
n = 1
while n <= 100:
    if n % 3 == 0 and n % 5 == 0:
        msg = "FizzBuzz"
    elif n % 3 == 0:
        msg = "Fizz"
    elif n % 5 == 0:
        msg = "Buzz"
    else:
        msg = n
    print(msg)
    n = n + 1

print("\nMan...that was pretty exhausting...but you did great!")
print("Thanks for hanging out with me! Goodbye!  Beep boop beep!")
        
