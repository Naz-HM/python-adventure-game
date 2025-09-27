#Make a adventure game with levels
#add questions
#use if/elif/else 
#add a weapon dynamic to the game 
# level added (2)
# goal 10 levels 


name = input("Hey type your name: ").capitalize()

print("Hello" , name, "welcome to my game!") 

should_we_play = input("Do you want to play? ").lower()

play = should_we_play == 'yes'


if play:
    print("Great lets start this fun adventure of mini quizes!")




    #Level 1-
    choice_1 = input('Do you want to enter the dark cave? ').lower()
    if choice_1 ==  'no':
        print('Lets come back another day.')
    elif choice_1 == 'yes':
        print('Nice! I see that you are very brave')



        #Level 2-
        choice_2 = input('Do you want to open the mysterious chest? ').strip().lower()
        if choice_2 == 'yes':
            print('WOW you just found 2 weapos!')
            weapon = input("What would you like to play with (gun/sword)? ").strip().lower()
            if weapon == 'gun':
                print("You picked the gun. Good range!")
            elif weapon == 'sword':
                print("You picked the sword. Strong up close!")
            else:
                print("That's not a valid weapon. You move on without a weapon.")
                weapon = None
        elif choice_2 == 'no':
            print('. There might be danger ahead')

            #Level 3- 


            #print('Welecome to the next level. Now that you have a weapon be aware of the beasts!')
                
            
            

        
            
    else:
        print('Not a Valid response. Re-enter choice.(left/right)')

else:
    print("We are Not going to play!")
            

        
            
   
