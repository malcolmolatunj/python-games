import time
import random
import sys


def play_again():
    print('Would you like to hear another joke? (y)es or (n)o')

    response = input('> ')
    while not is_valid(response):
        print("Sorry, I didn't catch that.")
        print("Please enter (y)es or (n)o.")
        response = input('> ')
        
    return response.lower().startswith('y')
    

def is_valid(response):
    return response.lower().startswith('y') or response.lower().startswith('n')

def snowman():
    print ('What do you get when you cross a snowman with a vampire?')
    input()
    print('Frostbite!')


def astronaut():
    print ('What do dentists call an astronaut\'s cavity?')
    input ()
    print ('A black hole!')


def interrupting_cow():
    print ('Knock knock.')
    input ()
    print ('Interrupting cow.')
    time.sleep(1.7)
    print ('MOOOOOO!')
    time.sleep(1.3)


def armies():
    print ('WWhere does the queen keep her armies?')
    input ()
    print ('In her sleevies!')


def dentist():
    print("When is the best time to go to the dentist?")
    input()
    print("Tooth-hurty!")


def switzerland():
    print("What's the best thing about Switzerland?")
    input()
    print("I don't know, but the flag is a big plus!")


def atoms():
    print("Why don't scientists trust atoms?")
    input()
    print("Because they make up everything!")


def nosy_pepper():
    print("What does a nosy pepper do?")
    input()
    print("It gets jalapeño business!")


def kleptos():
    print("Why can't you explain puns to kleptomaniacs?")
    input()
    print("They always take things literally.")


def bagel():
    print("How do you keep a bagel from getting away?")
    input()
    print("You put lox on it!")


def eyes():
    print("What did the left eye say to the right eye?")
    input()
    print("Between you and me, something smells.")


def hats():
    print("What did one hat say to the other?")
    input()
    print("You wait here, I'll go on a head.")

def duck():
    print("Why does a duck have tail feathers?")
    input()
    print("To cover its butt quack!")

def frog():
    print("What happens when a frog's car breaks down?")
    input()
    print("It gets toad.")

def shellfish():
    print("Why won't the shrimp share its treasure?")
    input()
    print("Because it's shellfish.")

def terminator():
    print("What did the Terminator say when he finished his latte?")
    input()
    print("Hasta la barista, Baby!")

def burrito():
    print("What did the taco say to the sad burrito?")
    input()
    print("We've all bean there.")

jokes = [
    snowman,
    astronaut,
    interrupting_cow,
    armies,
    dentist,
    switzerland,
    atoms,
    nosy_pepper,
    kleptos,
    bagel,
    eyes,
    hats,
    duck,
    frog,
    shellfish,
    terminator,
    burrito
]

random.shuffle(jokes)


def main():
    try:
        joke = jokes.pop()
    except IndexError:
        print("Sorry, we're all out of jokes :( Try again later...")
    else:
        joke()
        if play_again():
            main()
    sys.exit()


if __name__ == '__main__':
    main()
    
    

