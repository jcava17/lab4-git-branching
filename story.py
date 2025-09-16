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
)
def right_path():
    print("You walk right and encounter a talking squirrel who recommends taking a potion that will give you endless power.")
    print("The squirrel has a sinister look on its face which is enticing you to take the potion")
    print("The thought of endless power and domination presents vivid realizations of how you can take over the world and keep all the riches while others suffer in despair")
def center_path():
    print("You walk down the center and encounter a magic genie that will grant you three wishes.")

if __name__ == "__main__":
    intro():
