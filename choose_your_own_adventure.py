name = input("type your name: ")
print("welcom", name, "to this adventure!")

answer = input(
    "You are on a dirt road, there is a fork. you can go left or right, which do you choose?").lower()

if answer == "left":
    answer = input(
        "you come to a river, you can walk over the bridge or swim through").lower()

    if answer == "swim":
        print("you swam acrross and were eaten by an alligator.")
    elif answer == "walk":
        print("you walked fro miles and died of dehydration")
    else:
        print('not a valid option. you lose.')
elif answer == "right":
    answer = input(
        "there is a forest, do you want to go in or around?").lower()
    if answer == "in":
        print("you wander around and get lost in the dark")
    elif answer == "around":
        print("you walk for days and days... there is no way around")
    else:
        print('not a valid option. you lose.')

else:
    print("not a valid option")
