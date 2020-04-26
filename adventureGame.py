#This program uses inputs from the user to choose different paths in their own adventure game
#@author: Idara Umoren
#@course: ICS3UC
#@date: 2018/09/28
from random import randint

#Input: User's name
userName = input("Adventurer, please enter your name: ")

#Game Sprites and names
userSprite = "(         )"
enemyName = "Shrekling"
shreklingSprite = "( ͡° ͜ʖ ͡ °)"
brickSprite = "|͏͘ ͏̛͠ ̵ ̵ ̴ ̴̛͜ ͏|"

#Game Health Values
userHealth = 20
userMaxHealth = 20
userIsAlive = True
enemyHealth = 30
enemyMaxHealth = 30
bag = "None"

#Weapon Stat Values
weaponName = "Bare Fists"
weaponHealth = -1
weaponDamage = 5

#Function for Health Bars (CurrentHealth, MaxHealth)
def healthBar(health, maxHealth):
    healthPercentage = int(health / maxHealth * 10)
    healthEmptySpace = 10 - healthPercentage
    displayHealthBar = ("[" + ("/" * healthPercentage) + (" " * healthEmptySpace) + "]")
    return displayHealthBar;

#Function for Blank Space
def blankSpace():
    blankLines = ("\n")  * 5
    return blankLines;

#funtion for printing battle screen (userName, userSprite, userHealth, userHealthMax, enemyName, enemySprite, enemyHealth, enemyMaxHealth)
def battleScreen (protagName, protagSprite, protagHealth, protagHealthMax, villainName, villainSprite, villainHealth, villainMaxHealth):
    characterSpacing = "                           "
    enemyNameSpacing = characterSpacing + "          "
    blankLineSpacing = blankSpace()
    displayHealthBarVillain = healthBar(villainHealth, villainMaxHealth)
    displayHealthBarProtag = healthBar(protagHealth, protagHealthMax)
    displayBattleScreen = ("\n") + enemyNameSpacing + villainName + ("\n") + characterSpacing + villainSprite + displayHealthBarVillain + blankLineSpacing + protagName + ("\n") + displayHealthBarProtag + protagSprite
    return displayBattleScreen;

def enemyAttack():
    attackLuck = randint(0,5)
    return attackLuck;
    
#Story and Decision 0: Kill shrekling 0 or not?
print("Months?  Years?  You've been locked away so long you've lost track of time.  Ever since that one day when you were captured by Shreak and his minions.  During all of your time imprisoned, you've been scheming different ways to get out.  It's the only thing that can help you keep your sanity.  As a result of this, you've already thought of an escape plan.  Now's the time to put it into action.  You've been grinding the brick that fell out of the wall so that it can serve as a key to your prison cell.  You wait for the prison guard to fall asleep and place the make-shift key into the keyhole, then turn.  The cell opens.  Now your faced with choice, you can either sneek away from the slumbering prison guard or steal his sword and use it to kill him.")

storyChoice0 = input("Type 'y' to kill the guard or 'n' to sneak away: " )
battleChoice = "Nothing"
if (storyChoice0 == "y"):
    print()
    weaponName = "Rusty Sword"
    weaponHealth = 3
    weaponDamage = 30
    enemyName = "Shrekling"
    enemySprite = shreklingSprite
    print("You reached sneek up to the guard and reach for his sword you've equiped the rusty sword, you now deal " + str(weaponDamage) + " damage")
    input("Press 'Enter' to continue... ")
    
    #Initiate battle:
    while(enemyHealth > 0 and userHealth > 0):
        print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, enemySprite, enemyHealth, enemyMaxHealth))
        battleChoice = input("Type 'attack' to attack. Type 'stats' to see current stats: ")
        #If user attacks
        if (battleChoice == "attack"):
            print("You attacked " + enemyName + " with " + weaponName)
            enemyHealth = enemyHealth - weaponDamage
            weaponHealth = weaponHealth - 1
            if(weaponHealth == 0):
                print(userName + " 's " + weaponName + " has broken.")
                weaponName = "Bare Fists"
                weaponDamage = 5
            input("Press 'Enter' to continue... ")
        #If user checks stats
        elif (battleChoice == "stats"):
            print()
            print (userName + ": ")
            print ("Health: " + str(userHealth) + "/" + str(userMaxHealth))
            print ("Weapon Name: " + weaponName)
            print ("Weapon Damage: " + str(weaponDamage))
            input("Press 'Enter' to continue...")
    print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, shreklingSprite, enemyHealth, enemyMaxHealth))
    
    if (enemyHealth <= 0):
        print("You've defeated: " + enemyName)   
    if (userHealth <= 0):
        print ("You died")
        userIsAlive = False
    input("Press 'Enter' to continue... ")
        

elif (storyChoice0 == "n" and userIsAlive == True):
    print ("You sneek around the guard, and decide to run down the hallway. You don't know where you're going but it's better than being stuck in that cage.  As you run, you can hear something coming around the corner.  It's probably more guards, so you need to hide.  One of the bricks to your left looks cracked and maybe with enough force, you could break it.")
    input("Press 'Enter' to continue... ")
    
if (storyChoice0 == "y" and userIsAlive == True):
    print("You make your way around the dead guard and dart into the hallway.  You run and run.  You don't know where you're going, but anything is better than being stuck in that cage.  Along the way, you can hear footsteps coming from around the corner.  You need to hide.  There is a cracked brick to your left.  Maybe with enough force, you could break it and slip through.")
    input("Press 'Enter' to continue... ")
   
enemySprite = brickSprite
enemyName = "Cracked Brick"
enemyHealth = 10
enemyMaxHealth = 15
while(enemyHealth > 0 and userHealth > 0):
    print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, enemySprite, enemyHealth, enemyMaxHealth))
    battleChoice = input("Type 'attack' to attack. Type 'stats' to see current stats: ")
    #If user attacks
    if (battleChoice == "attack"):
        print("You attacked " + enemyName + " with " + weaponName)
        enemyHealth = enemyHealth - weaponDamage
        weaponHealth = weaponHealth - 1
        if(weaponHealth == 0):
            print(userName + " 's " + weaponName + " has broken.")
            weaponName = "Fists"
            weaponDamage
            input("Press 'Enter' to continue... ")
    #If user checks stats
    elif (battleChoice == "stats"):
        print()
        print (userName + ": ")
        print ("Health: " + str(userHealth) + "/" + str(userMaxHealth))
        print ("Weapon Name: " + weaponName)
        print ("Weapon Damage: " + str(weaponDamage))
        input("Press 'Enter' to continue...")
print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, enemySprite, enemyHealth, enemyMaxHealth))
print ("You've broken the wall!")

if(userIsAlive == True):
    print("You manage to slip through the cracks in the wall and you can see two more Shreklings pass by.  You could probably sneek attack them right now.")
storyChoice1 = input("Type 'y' to sneak attack and 'n' to stay where you are: ")

if(storyChoice1 == "y" and userIsAlive):
    print("You quietly slip out of the hole in the wall, and pounce onto one of the Shreklings")
    enemySprite = "( ͡° ͜ʖ ͡ °)"
    enemyName = "Shrekling_1"
    enemyHealth = 20
    enemyMaxHealth = 20
    enemyDamage = 7
    while(enemyHealth > 0 and userHealth > 0):
        print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, enemySprite, enemyHealth, enemyMaxHealth))
        battleChoice = input("Type 'attack' to attack. Type 'stats' to see current stats: ")
        #If user attacks
        if (battleChoice == "attack"):
            print("You attacked " + enemyName + " with " + weaponName)
            enemyHealth = enemyHealth - weaponDamage
            weaponHealth = weaponHealth - 1
            if(weaponHealth == 0):
                print(userName + "'s " + weaponName + " has broken.")
                weaponName = "Bare Fists"
                weaponDamage = 5
            input("Press 'Enter' to continue... ")
            if(enemyHealth > 0):
                enemyLuck = enemyAttack()
                if(enemyLuck == 0):
                    print(enemyName + "'s attack missed'")
                elif(enemyLuck >= 1 and enemyLuck <= 4):
                    print(enemyName + " attacked you")
                    userHealth = userHealth - enemyDamage
                elif(enemyLuck == 5):
                    print(enemyName + " attacked you.  It was a critical hit!")
                    userHealth = userHealth - int(enemyDamage * 1.3)
                
        #If user checks stats
        elif (battleChoice == "stats"):
            print()
            print (userName + ": ")
            print ("Health: " + str(userHealth) + "/" + str(userMaxHealth))
            print ("Weapon Name: " + weaponName)
            print ("Weapon Damage: " + str(weaponDamage))
            input("Press 'Enter' to continue...")
    print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, shreklingSprite, enemyHealth, enemyMaxHealth))
    
    if (enemyHealth <= 0):
        print("You've defeated: " + enemyName)   
        bag = "Health Potion"
        print(enemyName + " dropped a " + bag + " you picked it up!")
        input("Press Enter to continue: ")
    
        print()
        enemySprite = "( ͡° ͜ʖ ͡ °)"
        enemyName = "Shrekling_2"
        enemyHealth = 20
        enemyMaxHealth = 20
        enemyDamage = 9
        print(enemyName + " saw you kill his comrade.  Filled with rage, he'll deal extra damage")
        while(enemyHealth > 0 and userHealth > 0):
            print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, enemySprite, enemyHealth, enemyMaxHealth))
            battleChoice = input("Type 'attack' to attack. Type 'stats' to see current stats.  Type 'bag' to use items: ")
            #If user attacks
            if (battleChoice == "attack"):
                print("You attacked " + enemyName + " with " + weaponName)
                enemyHealth = enemyHealth - weaponDamage
                weaponHealth = weaponHealth - 1
                if(weaponHealth == 0):
                    print(userName + "'s " + weaponName + " has broken.")
                    weaponName = "Bare Fists"
                    weaponDamage = 5
                input("Press 'Enter' to continue... ")
                if(enemyHealth > 0):
                    enemyLuck = enemyAttack()
                    if(enemyLuck == 0):
                        print(enemyName + "'s attack missed'")
                    elif(enemyLuck >= 1 and enemyLuck <= 4):
                        print(enemyName + " attacked you")
                        userHealth = userHealth - enemyDamage
                    elif(enemyLuck == 5):
                        print(enemyName + " attacked you.  It was a critical hit!")
                        userHealth = userHealth - int(enemyDamage * 1.3)
                    
            #If user checks stats
            elif (battleChoice == "stats"):
                print()
                print (userName + ": ")
                print ("Health: " + str(userHealth) + "/" + str(userMaxHealth))
                print ("Weapon Name: " + weaponName)
                print ("Weapon Damage: " + str(weaponDamage))
                print("Bag: " + bag)
                input("Press 'Enter' to continue...")
                
            #If user checks Bag
            elif(battleChoice == "bag"):
                print()
                print(userName + " used " + bag)
                if (bag == "Health Potion"):
                    userHealth = 20
                    print("Your health is now " + str(userHealth))
                    bag = "Nothing"
                    input("Press 'Enter' to continue...")
        print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, shreklingSprite, enemyHealth, enemyMaxHealth))
        if (enemyHealth <= 0):
            print("You've defeated: " + enemyName)   
        if (userHealth <= 0):
            print ("You died")
            userIsAlive = False
        input("Press 'Enter' to continue... ")
        weaponName = "Rusty Sword"
        weaponHealth = 3
        weaponDamage = 30
        print(enemyName + " dropped a " + weaponName  + " You've picked it up.")
    elif (userHealth <= 0):
        print ("You died")
        userIsAlive = False
        #garfield reid
    input("Press 'Enter' to continue... ")

if(storyChoice0 == "y" and storyChoice1 == "n" and userIsAlive == True):
    print("You stay hidden in the hole in the wall.  As the Skreklings approach, your heart skips.  They stayed near your position for a little bit, and then passed by you.  A couple seconds later, you hear a screaching sound.  They must've found the dead body of their comrade.  Now they're angry.  They'll deal extra damage now. You continue to follow down the pathway and out of nowhere a Shrekling jumps out at you.  He seems angerier than usual")
    input("Press Enter to continue...")
    enemySprite = "( ͡° ͜ʖ ͡ °)"
    enemyName = "Shrekling"
    enemyHealth = 20
    enemyMaxHealth = 20
    enemyDamage = 9
    #gethsemane reid
    while(enemyHealth > 0 and userHealth > 0):
        print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, enemySprite, enemyHealth, enemyMaxHealth))
        battleChoice = input("Type 'attack' to attack. Type 'stats' to see current stats.  Type 'bag' to use items: ")
        #If user attacks
        if (battleChoice == "attack"):
            print("You attacked " + enemyName + " with " + weaponName)
            enemyHealth = enemyHealth - weaponDamage
            weaponHealth = weaponHealth - 1
            if(weaponHealth == 0):
                print(userName + "'s " + weaponName + " has broken.")
                weaponName = "Bare Fists"
                weaponDamage = 5
            input("Press 'Enter' to continue... ")
            if(enemyHealth > 0):
            # get 70 reid
                enemyLuck = enemyAttack()
                if(enemyLuck == 0):
                    print(enemyName + "'s attack missed'")
                elif(enemyLuck >= 1 and enemyLuck <= 4):
                    print(enemyName + " attacked you")
                    userHealth = userHealth - enemyDamage
                elif(enemyLuck == 5):
                    print(enemyName + " attacked you.  It was a critical hit!")
                    userHealth = userHealth - int(enemyDamage * 1.3)
                
        #If user checks stats
        elif (battleChoice == "stats"):
            print()
            print (userName + ": ")
            print ("Health: " + str(userHealth) + "/" + str(userMaxHealth))
            print ("Weapon Name: " + weaponName)
            print ("Weapon Damage: " + str(weaponDamage))
            print("Bag: " + bag)
            input("Press 'Enter' to continue...")
            
        #If user checks Bag
        elif(battleChoice == "bag"):
            print()
            print(userName + " used " + bag)
            if (bag == "Health Potion"):
                userHealth = 20
                print("Your health is now " + str(userHealth))
                bag = "Nothing"
                input("Press 'Enter' to continue...")
    print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, shreklingSprite, enemyHealth, enemyMaxHealth))
    if (enemyHealth <= 0):
        print("You've defeated: " + enemyName)   
    if (userHealth <= 0):
        print ("You died")
        userIsAlive = False
    input("Press 'Enter' to continue... ")

if((storyChoice0 == "y" or storyChoice1 == "y") and userIsAlive == True):
    print("You continue down your path.  You keep on going, and after a while, you see a light at the end of the tunnel.  It's then that out of no where, SHREK pops out of nowhere!  This is it. The Final Fight")
    input("Press Enter to continue...")
    enemySprite = "o={0 <_> 0}=o"
    enemyName = "SHREK"
    enemyHealth = 100
    enemyMaxHealth = 100
    enemyDamage = 5
    #garret reid
    while(enemyHealth > 0 and userHealth > 0):
        print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, enemySprite, enemyHealth, enemyMaxHealth))
        battleChoice = input("Type 'attack' to attack. Type 'stats' to see current stats.  Type 'bag' to use items: ")
        #If user attacks
        if (battleChoice == "attack"):
            print("You attacked " + enemyName + " with " + weaponName)
            enemyHealth = enemyHealth - weaponDamage
            weaponHealth = weaponHealth - 1
            if(weaponHealth == 0):
                print(userName + "'s " + weaponName + " has broken.")
                weaponName = "Bare Fists"
                weaponDamage = 5
            input("Press 'Enter' to continue... ")
            if(enemyHealth > 0):
                enemyLuck = enemyAttack()
                if(enemyLuck == 0):
                    print(enemyName + "'s attack missed'")
                elif(enemyLuck >= 1 and enemyLuck <= 4):
                    print(enemyName + " attacked you")
                    userHealth = userHealth - enemyDamage
                elif(enemyLuck == 5):
                    print(enemyName + " attacked you.  It was a critical hit!")
                    userHealth = userHealth - int(enemyDamage * 1.3)
                
        #If user checks stats
        elif (battleChoice == "stats"):
            print()
            print (userName + ": ")
            print ("Health: " + str(userHealth) + "/" + str(userMaxHealth))
            print ("Weapon Name: " + weaponName)
            print ("Weapon Damage: " + str(weaponDamage))
            print("Bag: " + bag)
            input("Press 'Enter' to continue...")
            
        #If user checks Bag
        elif(battleChoice == "bag"):
            print()
            print(userName + " used " + bag)
            if (bag == "Health Potion"):
                userHealth = 20
                print("Your health is now " + str(userHealth))
                bag = "Nothing"
                input("Press 'Enter' to continue...")
    print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, enemySprite, enemyHealth, enemyMaxHealth))
    if (enemyHealth <= 0):
        print("You've defeated: " + enemyName)   
    if (userHealth <= 0):
        print ("You died")
        userIsAlive = False
    input("Press 'Enter' to continue... ")

if (storyChoice0 == "n" and storyChoice1 == "n"):
    print("As the Shreklings passed by you, it stopped to look around.  When it thought the coast was clear, it left.  You continue to traverse the path and after a while, you see a bright light.  You follow it and it leads outside.  Congratulations " + userName + " You've escaped Shrek's swamp without harming anyone!")

if(userIsAlive == True and storyChoice0 != "n" and storyChoice1 != "y"):
    print("You continue down the path and into the Day light.  Congratulations " + userName + " You've escaped Shrek's Swamp!")















#print (battleScreen(userName, userSprite, userHealth, userMaxHealth, enemyName, shreklingSprite, enemyHealth, enemyMaxHealth))


    
