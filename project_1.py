

name = input("Hey type your name: ").capitalize()

print("Hello" , name, "welcome to my game!") 

should_we_play = input("Do you want to play? ").lower()

play = should_we_play == 'yes'


if play:
    print("We are gonna play")

    direction = input('Do you want to go left or right?(left/right)? ').lower()
    weapon = input('sword/gun').lower
    if direction ==  'left':
        print('OOPS! wrong choice retry')
    elif direction == 'right':
        print('Nice choice. Now choose again')
        new_choice = input('left/right')
        if new_choice == 'left':
            print('Nice you found the way out')
            print('Next level!')
            new_direction = input('left/right?')
            if new_direction == 'right':
                print('Nice you made the correct choice again')
                print('Congrats. you have leveled up and unlocked new feature.')
                print('Choose a weapon now, sword/gun?')
                  
                if weapon == 'sword':
                     print('It seems like you like the sword. With this your path sahll get more diffcult!')
                elif weapon == 'gun':
                     print("Nice choice a mag of a gun can take you far")
        elif new_choice == 'right':
            print('OOPS! wrong choice you fell off the cliff!')    
            

        
            
    else:
        print('Not a Valid response. Re-enter choice.(left/right)')

else:
    print("We are Not going to play!")