# Loops statements - Python includes break, continue and pass
# break - when the loop end will go to the next statement (out of the loop)
# continue - skips corrent part of the loop
# Pass - skips any part of the loop that contains pass


number = 6

while number < 10:
    if number < 10:
        print("The number is {} !".format(number))
        number += 1
    if number == 7:
       # print("Skipping number 7")
        number += 1
        continue
    if number >= 10:
        print("The number is bigger or equal than 10 => {} => Break !".format(number))
        break
