
import time  # for delays

# ======================
# Game Intro Header
# ======================
print("===================================")
print("    WELCOME TO THE CAVE QUEST   ")
print("===================================")
print("A mysterious cave lies before you...")
print("Legends say it holds strange creatures, hidden treasures,")
print("and a dragon deep within. Few who enter ever return.")
print()
print("Your goal: Survive 10 levels of danger,")
print("defeat the beasts, and conquer the dragon.")
print("Answer Python questions to strike your foes!")
print("Three wrong answers, and your journey ends...")
print("===================================")
time.sleep(3)

name = input("Type your name to get started!: ").strip().capitalize()
print("Hello", name, "welcome to CAVE QUEST!".title())

should_we_play = input("Do you want to play? (yes/no) ").strip().lower()
play = (should_we_play == "yes")

if not play:
    print("ok lets come back another day!".title())
    exit()

print("Great lets start this fun adventure of mini quizzes!".title())

# score & mistake tracking
score = 0          # +10 on correct
wrong = 0          # +1 on wrong; 3 = Game Over

# ===== INTRO =====
choice_1 = input("Do you want to enter the dark cave? (yes/no) ").strip().lower()
if choice_1 == "no":
    print("Let's come back another day.".title())
    print("Final Score:", score)
    exit()
elif choice_1 != "yes":
    print("Not a valid response. Game Over.")
    print("Final Score:", score)
    exit()

print("Let's go on a great adventure".title())
print("You enter the cave".title())
print("The cave is very dangerous. There are a lot of wild animals—be careful on your way down!".title())
print("If you are wrong, you die; if you are right, your weapon deals damage.")

# weapon state (exists even if chest ignored)
weapon = None

print("After a few minutes into the cave...")
chest = input("You hear scratching inside a chest. Do you want to open it? (yes/no) ").strip().lower()
if chest == "yes":
    print("WOW you just found 2 weapons!")
    w = input("Which weapon would you like to use? (gun/sword) ").strip().lower()
    if w in ("gun", "sword"):
        weapon = w
        print("You equipped:", weapon)
    else:
        print("That's not a valid weapon. You move on without a weapon.")
elif chest == "no":
    print("You missed out on some valuable loot.".title())
else:
    print("Not a valid response. You move on cautiously without a weapon.")

# helper to show status and check strikes
def status_check():
    print("Score:", score, " | Mistakes:", wrong)
    if wrong >= 3:
        print("You made 3 mistakes. Game Over!")
        print("Final Score:", score)
        exit()

# =========================
# Level 1 – BATS
# =========================
print("\n== Level 1: Bats ==")
print("A swarm of bats rushes toward you!")
q1 = input("Can a Python variable name start with a number? (yes/no) ").strip().lower()
if q1 == "no":
    score += 10
    if weapon == "gun":
        print("CORRECT! Your gun sprays the swarm—10/10 damage. The bats scatter! Move to the next level.")
    elif weapon == "sword":
        print("CORRECT! You slash through the swarm—10/10 damage. The bats flee! Move to the next level.")
    else:
        print("CORRECT! You dodge and clap loudly—they disperse. Move to the next level.")
else:
    wrong += 1
    print("Wrong! The bats attack you.")
status_check()
time.sleep(3)

# =========================
# Level 2 – CAVE SPIDERS
# =========================
print("\n== Level 2: Cave Spiders ==")
print("Watch out! Cave spiders appear!")
if weapon is None:
    print("You have no weapon. Answer correctly to escape!")
q2 = input("Is Python case-sensitive when it comes to variable names? (yes/no) ").strip().lower()
if q2 == "yes":
    score += 10
    if weapon == "gun":
        print("CORRECT! Your gun deals 10/10 damage. The cave spiders are shot down! Move to the next level.")
    elif weapon == "sword":
        print("CORRECT! Your sword deals 10/10 damage. The cave spiders are slashed down! Move to the next level.")
    else:
        print("CORRECT! You escape safely even without a weapon. Move on to the next level.")
else:
    wrong += 1
    print("Wrong! The spiders overwhelm you.")
status_check()
time.sleep(3)

# =========================
# Level 3 – CAVEFISH
# =========================
print("\n== Level 3: Cavefish ==")
print("This floor is flooded. Fish suddenly attack from the pool!")
q3 = input("Is indentation required in Python code blocks? (yes/no) ").strip().lower()
if q3 == "yes":
    score += 10
    if weapon == "gun":
        print("CORRECT! 10/10 damage. You shoot at the hostile fish and they flee! Move on to the next level.")
    elif weapon == "sword":
        print("CORRECT! 10/10 damage. You slash the hostile fish and they flee! Move on to the next level.")
    else:
        print("CORRECT! You dodge through the water and escape safely. Move on to the next level.")
else:
    wrong += 1
    print("Wrong! The hostile fish bite you.")
status_check()
time.sleep(3)

# =========================
# Level 4 – CAVE CRAYFISH
# =========================
print("\n== Level 4: Cave Crayfish ==")
print("Pale crayfish crawl out and snap their claws at you!")
q4 = input("Does Python use '#' for comments? (yes/no) ").strip().lower()
if q4 == "yes":
    score += 10
    if weapon == "gun":
        print("CORRECT! You shoot the crayfish and they scatter! Move to the next level.")
    elif weapon == "sword":
        print("CORRECT! You sweep your sword and clear them! Move to the next level.")
    else:
        print("CORRECT! You stomp them aside and pass! Move to the next level.")
else:
    wrong += 1
    print("Wrong! The crayfish swarm you.")
status_check()
time.sleep(3)

# =========================
# Level 5 – OLM
# =========================
print("\n== Level 5: Olm ==")
print("A pale blind salamander slithers across your path!")
q5 = input("Can Python strings be written with both single quotes and double quotes? (yes/no) ").strip().lower()
if q5 == "yes":
    score += 10
    if weapon == "gun":
        print("CORRECT! You fire a warning shot and the Olm retreats. Move to the next level.")
    elif weapon == "sword":
        print("CORRECT! You slash the ground and the Olm slips away. Move to the next level.")
    else:
        print("CORRECT! You stomp loudly and it retreats into the water. Move to the next level.")
else:
    wrong += 1
    print("Wrong! The Olm lashes at you with its tail.")
status_check()
time.sleep(3)

# =========================
# Level 6 – CAVE BEETLES
# =========================
print("\n== Level 6: Cave Beetles ==")
print("Beetles swarm along the walls.")
q6 = input("Does `list = (1,2,3)` create a list in Python? (yes/no) ").strip().lower()
if q6 == "no":
    score += 10
    if weapon == "gun":
        print("CORRECT! You blast the swarm off the walls. Move to the next level.")
    elif weapon == "sword":
        print("CORRECT! You sweep your sword and clear the path. Move to the next level.")
    else:
        print("CORRECT! You scrape through and push past them. Move to the next level.")
else:
    wrong += 1
    print("Wrong! The beetles bite at your boots.")
status_check()
time.sleep(3)

# =========================
# Level 7 – CAVE SALAMANDERS
# =========================
print("\n== Level 7: Cave Salamanders ==")
print("Slippery salamanders cover the floor!")
q7 = input("Is `3 // 2` equal to 1 in Python? (yes/no) ").strip().lower()
if q7 == "yes":
    score += 10
    if weapon == "gun":
        print("CORRECT! You keep distance and pass safely. Move to the next level.")
    elif weapon == "sword":
        print("CORRECT! You carefully clear a path. Move to the next level.")
    else:
        print("CORRECT! You tiptoe through without falling. Move to the next level.")
else:
    wrong += 1
    print("Wrong! You slip and get hurt.")
status_check()
time.sleep(3)

# =========================
# Level 8 – CAVE HARVESTMEN
# =========================
print("\n== Level 8: Cave Harvestmen ==")
print("Long-legged creatures drop from the ceiling!")
q8 = input("Is `def` used to define a function in Python? (yes/no) ").strip().lower()
if q8 == "yes":
    score += 10
    if weapon == "gun":
        print("CORRECT! Quick shots scatter them. Move to the next level.")
    elif weapon == "sword":
        print("CORRECT! You slice them down as they fall. Move to the next level.")
    else:
        print("CORRECT! You duck and sprint through. Move to the next level.")
else:
    wrong += 1
    print("Wrong! They entangle you in their legs.")
status_check()
time.sleep(3)

# =========================
# Level 9 – CAVE MILLIPEDES
# =========================
print("\n== Level 9: Cave Millipedes ==")
print("A carpet of pale millipedes curls around your boots.")
q9 = input("Will `print(2 == '2')` output True in Python? (yes/no) ").strip().lower()
if q9 == "no":
    score += 10
    if weapon == "gun":
        print("CORRECT! You fire to scare them off. Move to the next level.")
    elif weapon == "sword":
        print("CORRECT! You clear a path with careful swings. Move to the next level.")
    else:
        print("CORRECT! You shake them off and continue. Move to the next level.")
else:
    wrong += 1
    print("Wrong! They crawl up your legs.")
status_check()
time.sleep(3)

# =========================
# Level 10 – DRAGON (FINAL, 5 questions)
# =========================
print("\n== Level 10: Dragon ==")
print("The cavern opens into a vast chamber. A DRAGON awakens and roars!")
print("Answer 5 Python questions to defeat it. Three total mistakes = instant defeat.")

# 10.1
q10_1 = input("Does len('abc') return 3? (yes/no) ").strip().lower()
if q10_1 == "yes":
    score += 10
    print("CORRECT! The dragon staggers!")
else:
    wrong += 1
    print("Wrong! The dragon breathes fire at you.")
status_check()
time.sleep(3)

# 10.2
q10_2 = input("Is None equal to 0 in Python? (yes/no) ").strip().lower()
if q10_2 == "no":
    score += 10
    print("CORRECT! The dragon recoils!")
else:
    wrong += 1
    print("Wrong! Its tail slams you.")
status_check()
time.sleep(3)

# 10.3
q10_3 = input("Can a for-loop iterate over a list in Python? (yes/no) ").strip().lower()
if q10_3 == "yes":
    score += 10
    print("CORRECT! You land a critical hit!")
else:
    wrong += 1
    print("Wrong! The dragon’s roar stuns you.")
status_check()
time.sleep(3)

# 10.4
q10_4 = input("Does True and False evaluate to True in Python? (yes/no) ").strip().lower()
if q10_4 == "no":
    score += 10
    print("CORRECT! Its armor shatters!")
else:
    wrong += 1
    print("Wrong! A blast of fire burns you.")
status_check()
time.sleep(3)

# 10.5
q10_5 = input("Is input() used to read user input in Python? (yes/no) ").strip().lower()
if q10_5 == "yes":
    score += 10
    print("CORRECT! The dragon collapses. YOU WIN!")
else:
    wrong += 1
    print("Wrong! The dragon’s last strike hits you.")
status_check()

# Victory wrap-up
print("\n The cavern is silent. The dragon is defeated!")
print("Final Score:", score)
exit()


            

        
            
   
