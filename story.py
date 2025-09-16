def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("As you approach the stone you are able to pull the sword and defeat the evil dragon")
    print("Once you defeat the dragon you become the hero of the village and are praised by all")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

def center_path():
    print("You walk down the center and encounter a magic genie that will grant you three wishes.")

if __name__ == "__main__":
    intro():
