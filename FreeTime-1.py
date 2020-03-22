#Anthony Stephens JR
import random
import time
def Restart():
    name = input("Enter your name Luminary:")
    Intro(name)
def Intro(name=None):
    if name == None:
        name = input("Enter your name Luminary:")
    print("In the land of Yggradsil evil has ran wild.")
    print("Monsters claim the lives of the innocent and are becoming more powerful by each passing day.")
    print("Only the Luminary is strong enough to take down the center of all this corruption.")
    print("The Darkspawn.... It is his destiny to bring back the world to light.")
    print("Hello", name)
    time.sleep(2)
    print("Are you prepared to stop chaos and defeat the Darkspawn?")
    decision = input("Enter Y/N:", )
    time.sleep(2)
    if decision == ("Y"):
        time.sleep(1)
        print("May your quest begin")
        MainStory1(name)
        time.sleep(1)
    elif decision == "N":
        time.sleep(2)
        print ("Come back when you're ready Hero...")
        time.sleep(2)
        Restart()
    else:
        print("Invalid Answer")
        Restart()
def MeetingErik(name):
    print ("Stranger: Hey there mate! What are you doing here in a place like?")
    time.sleep(1)
    print ("Narrator: You tell them who you are and what your quest is.")
    time.sleep(1)
    print ("Stranger: HAHAHA! Seriously!")
    seriously = input("Quick what's 9 + 10?")
    if seriously == "19":
        print ("Stranger: Well, I guess you aren't a complete idiot")
        print("Erik: Well, my name's Erik and my quest was to find the Luminary.")
        time.sleep(2) 
        print("Erik: To be honest, thought he'd look older and you know not pathetic.")
        time.sleep(2)
        print("Erik: Well begger can't be chooser is what they say")
        ErikChose = input("Well, mind if I tag along? Y/N?")
        if ErikChose == ("Y"):
            print("Narrator: Erik has joined the party")
            CityTrip(name)
        elif ErikChose == ("N"):
            print("Erik: Well, looks like you're  a goner")
            print("Narrator: Erik got a cheap shot with his dagger")
            print("Narrator: You bleed out within an hour")
            RETRY = input("Try Again? Y/N")
            if RETRY == "Y":
                Restart()
            elif RETRY == "N":
                print("Narrator: Way to let us down", name)
            else:
                print("Invalid Answer")
                Restart()   
    elif seriously == ("21") or ("69") or ("420"):
        print ("......")
        time.sleep(1)
        print ("You died! Don't ask how though!")
        Restart() 
    elif ErikChose == ("N"):
        print("Erik: Well, looks like you're  a goner")
        print("Narrator: Erik got a cheap shot with his dagger")
        print("Narrator: You bleed out within an hour")
        RETRY = input("Try Again? Y/N")
        if RETRY == "Y":
            Restart()
        elif RETRY == "N":
             print("Narrator: Way to let us down", name)
        else:
            print("Invalid Answer")
            Restart()   
def MainStory1(name):
    print ("As you start your journey, you the road splits into two.")
    time.sleep(2)
    choose = input("Do you want to take the left or right past. Enter L/R:")
    time.sleep(1)
    if choose == "L":
        print("As you walk down the path you see a group of goblins.")
        time.sleep(1)
        print("Narrator: They find you and murder you with sticks and stones but their words never hurt you.")
        time.sleep(1)
        print("Narrator: Mostly because you didn't understand them.")
        RETRY = input("Try Again? Y/N")
        if RETRY == "Y":
            Restart()
        elif RETRY == "N":
            print("Narrator: Way to let us down", name)
        else:
            RETRY = input("Try Again? Y/N")
            print(Restart())
    elif choose == "R":
        print("Narrator: The path looks safe and you run into a young man around your age.")
        MeetingErik(name)
    else:
        print ("Error")
        time.sleep(2)
        MainStory1(name)

def CityTrip(name):
    print("Narrator:" + name + " and Erik begin traveling to Hoenn City until they approach a chest")
    for gold in range (10,100,10):
        print("you found " + str(gold) + " pieces of gold")
        time.sleep(1)
Intro()

            
          

    
        
