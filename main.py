from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.extend([left_stack,middle_stack,right_stack])




#Set up the Game
game_ready = False
num_disks = int(input("\nHow many disks do you want to play with?\n"))
if num_disks >= 3:
  game_ready = True
while not game_ready:
  num_disks = int(input("Please enter a number greater than or equal 3\n"))
  if num_disks >= 3:
    game_ready = True

for i in range(num_disks,0, -1):
  left_stack.push(i)

num_optimal_moves = 2 ** num_disks -1

print("\nThe fastests you can solve this game is in {turns} moves".format(turns = num_optimal_moves))


#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  input_ready = False
  while not input_ready:
    print("Please select a stack from the following characters")
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      #print("name", name)
      #print("Letter", letter)
      print("Enter {char} for {name}.".format(char = letter, name = name))
    user_choice = input("")
    user_choice = user_choice.upper()
    if user_choice not in choices:
      input_ready = False
    else:
      for i in range(len(choices)):
        if choices[i] == user_choice:
          return stacks[i]


# Alt Version for get_input()
def get_input_B():
    choices = {'L': left_stack, 'M': middle_stack, 'R': right_stack}
    while True:
        print("Please select a stack from the following characters")
        for key, stack in choices.items():
            print(f"Enter {key} for {stack.get_name()}.")
        user_choice = input("").upper()
        if user_choice in choices:
            return choices[user_choice]
        else:
            print("Invalid choice. Try again.")




#Play the Game
num_user_moves = 0
while (right_stack.get_size() != num_disks):
    print("\n\n\n... Current Stacks...")
    for stack in stacks:
        stack.print_items()
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input_B()
        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again")
            continue
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input_B()
        if to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves = num_user_moves + 1
            break
        else:
            print("\n\nInvalid Move. Try Again")
            continue
print("\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}.".format(num_user_moves=num_user_moves, num_optimal_moves=num_optimal_moves))
