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
    print()
else:
    print("not a valid option")
