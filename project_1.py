# Make a adventure game with levels
# add a weapon dynamic to the game
# 10 levels

name = input("Hey type your name: ").strip().capitalize()
print("Hello", name, "welcome to my game!".title())

should_we_play = input("Do you want to play? (yes/no) ").strip().lower()
play = (should_we_play == "yes")

if play:
    print("Great lets start this fun adventure of mini quizzes!".title())

    # score & mistake tracking
    score = 0
    wrong = 0  # 3 mistakes = game over

    # ===== INTRO =====
    choice_1 = input("Do you want to enter the dark cave? (yes/no) ").strip().lower()
    if choice_1 == "no":
        print("Let's come back another day.".title())
        print("Final Score:", score)
        raise SystemExit()

    elif choice_1 == "yes":
        print("Let's go on a great adventure".title())
        print("You enter the cave".title())
        print("The cave is very dangerous. There are a lot of wild animals—be careful on your way down!".title())
        print("Based on the question: if you are wrong, you die; if you are right, your weapon deals damage.")

        # weapon state (exists even if chest ignored)
        weapon = None

        print("After a few minutes into the cave...")
        chest = input("You hear scratching inside a chest. Do you want to open it? (yes/no) ").strip().lower()
        if chest == "yes":
            print("WOW you just found 2 weapons!")
            weapon = input("Which weapon would you like to use? (gun/sword) ").strip().lower()
            if weapon == "gun":
                print("You chose the path of a marksman!")
            elif weapon == "sword":
                print("You chose the path of a warrior!")
            else:
                print("That's not a valid weapon. You move on without a weapon.")
                weapon = None
        elif chest == "no":
            print("You missed out on some valuable loot.".title())
        else:
            print("Not a valid response. You move on cautiously without a weapon.")
            weapon = None

        # =========================
        # Level 1 – BATS
        # =========================
        print("Lets go to the first level of the cave")
        print("There are a lot of bats coming your way!")
        print("Answer this simple Python question to deal damage with your chosen weapon")

        question_1 = input("Can a Python variable name start with a number? (yes/no) ").strip().lower()
        if question_1 == "no":  # correct
            score += 10
            if weapon == "gun":
                print("CORRECT! Your gun sprays the swarm—10/10 damage. The bats scatter! Move to the next level.")
            elif weapon == "sword":
                print("CORRECT! You slash through the swarm—10/10 damage. The bats flee! Move to the next level.")
            else:
                print("CORRECT! You dodge and clap loudly—they disperse. Move to the next level.")
        else:  # wrong or invalid
            wrong += 1
            print("Wrong! The bats attack you.")

        print("Score:", score, "| Mistakes:", wrong)
        if wrong == 3:
            print("You made 3 mistakes. Game Over!")
            print("Final Score:", score)
            raise SystemExit()

        # =========================
        # Level 2 – CAVE SPIDERS
        # =========================
        print("You go down to the next level.")
        print("Watch out! Cave spiders appear!")
        if weapon is None:
            print("You have no weapon. Answer correctly to escape!")

        question_2 = input("Is Python case-sensitive when it comes to variable names? (yes/no) ").strip().lower()
        if question_2 == "yes":  # correct
            score += 10
            if weapon == "gun":
                print("CORRECT! Your gun deals 10/10 damage. The cave spiders are shot down! Move to the next level.")
            elif weapon == "sword":
                print("CORRECT! Your sword deals 10/10 damage. The cave spiders are slashed down! Move to the next level.")
            else:
                print("CORRECT! You escape safely even without a weapon. Move on to the next level.")
        else:  # wrong or invalid
            wrong += 1
            print("Wrong! The spiders overwhelm you.")

        print("Score:", score, "| Mistakes:", wrong)
        if wrong == 3:
            print("You made 3 mistakes. Game Over!")
            print("Final Score:", score)
            raise SystemExit()

        # =========================
        # Level 3 – CAVEFISH
        # =========================
        print("You made it to the next level underground.")
        print("This floor is flooded. Watch out—there could be monsters in the pool.")
        print("As you look into the water you see some fish… they suddenly attack!")

        question_3 = input("Is indentation required in Python code blocks? (yes/no) ").strip().lower()
        if question_3 == "yes":  # correct
            score += 10
            if weapon == "gun":
                print("CORRECT! 10/10 damage. You shoot at the hostile fish and they flee! Move on to the next level.")
            elif weapon == "sword":
                print("CORRECT! 10/10 damage. You slash the hostile fish and they flee! Move on to the next level.")
            else:
                print("CORRECT! You dodge through the water and escape safely. Move on to the next level.")
        else:  # wrong or invalid
            wrong += 1
            print("Wrong! The hostile fish devour you.")

        print("Score:", score, "| Mistakes:", wrong)
        if wrong == 3:
            print("You made 3 mistakes. Game Over!")
            print("Final Score:", score)
            raise SystemExit()

        # =========================
        # Level 4 – CAVE CRAYFISH
        # =========================
        print("You reach a deeper part of the cave where the water is shallow.")
        print("Suddenly, pale crayfish crawl out and snap their claws at you!")

        question_4 = input("Does Python use '#' for comments? (yes/no) ").strip().lower()
        if question_4 == "yes":  # correct
            score += 10
            if weapon == "gun":
                print("CORRECT! You shoot the crayfish and they scatter! Move to the next level.")
            elif weapon == "sword":
                print("CORRECT! You slash the crayfish and they scuttle away! Move to the next level.")
            else:
                print("CORRECT! You stomp the crayfish and escape safely. Move on to the next level.")
        else:  # wrong or invalid
            wrong += 1
            print("Wrong! The crayfish swarm you.")

        print("Score:", score, "| Mistakes:", wrong)
        if wrong == 3:
            print("You made 3 mistakes. Game Over!")
            print("Final Score:", score)
            raise SystemExit()



        print("End of current demo levels.")
        print("Final Score:", score)

    else:
        print("Not a valid response. Re-enter choice next time. (yes/no)")

else:
    print("We are Not going to play!")
            

        
            
   
