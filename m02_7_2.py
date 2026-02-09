# 7.2 - while loop practice

# variable
guess_me = 7
number = 1

# while loop
while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
    number += 1