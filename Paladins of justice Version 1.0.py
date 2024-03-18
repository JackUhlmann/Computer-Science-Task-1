#import my random number generator and my system exit functions
import random
import sys
#creating the variables so they are available to be used later
playerhealth = "grah"
yesorno = "blah"
playerpos = "0"
again = "rah"
masks = "mask"
distraction = "distract"
stealthdeath = "death"
ruccus = "ruccus"
sneaking = "sneakyboy"
foodpoison = "iboerf"
kitchen = "ibuwerbiu"
feast = "uhbwbitr"
timing = "uhbwefuiobvfewj vfrjni"
KO = "huh"
#setting hps and counters
totalhours = float(0)
workhours = float(0)
playerhp = float(8)
treedeath = float(0)
hp = float(0)
overwork = float(0)
commendation = float (0)
correct = float(0)
underwork = float(0)
#creatiing an array for the players classes
classes = []
#creating the achievements system
achievements = ["achievements"]
achpercent = int(0)
#creating the space function that seperates storyline and user choices to make it easier to read, Quality Of Life Fix
def inputspace():
    print()
#creating the space function to seperate different modules so that it is easier for the player to read, Quality Of Life Fix
def space():
    print()
    print()
    print()
#drawing the title screen for the game
def opening():
    space()
    print(" ░█░█░█▀▀░█░░░█▀▀░█▀█░█▄█░█▀▀░░░▀█▀░█▀█░░░░ ")
    print(" ░█▄█░█▀▀░█░░░█░░░█░█░█░█░█▀▀░░░░█░░█░█░░▀░ ")
    print(" ░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░░▀░░▀▀▀░░▀░ ")
    space()
    print(" ░█▀█░█▀█░█░░░█▀█░█▀▄░▀█▀░█▀█░█▀▀░░░█▀█░█▀▀░░░▀▀█░█░█░█▀▀░▀█▀░▀█▀░█▀▀░█▀▀ ")
    print(" ░█▀▀░█▀█░█░░░█▀█░█░█░░█░░█░█░▀▀█░░░█░█░█▀▀░░░░░█░█░█░▀▀█░░█░░░█░░█░░░█▀▀ ")
    print(" ░▀░░░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀░░░▀▀▀░▀░░░░░▀▀░░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀ ")
    space()
    input("press enter to continue")
    space()
    space()
#drawing the arrow for the arrow death
def arrow():
    space()
    print(str("'         |¯¯¯¯¯¯¯¯\                       |\          /¯¯¯¯¯¯¯¯\                                   '"))
    print(str("'         |_________\______________________| \      @ <  UH OH!  |                                    '"))
    print(str("'         |________________________________|  >    -|- \I'm Dead/                                   '"))
    print(str("'         |         /                      | /       /\   ¯¯¯¯¯¯¯¯                                    '"))
    print(str("'         |________/                       |/                                                       '"))
    space()
#drawing the log falling on you
def log():
    space()
    print(str("'                 _                                                                                   '"))
    print(str("'             ###//_#       _________________________                                                   '"))
    print(str("'             ###//_#      / Uh Oh, I think that tree\                                                  '"))
    print(str("'                //_     @ < Might be about to fall   |                                                 '"))
    print(str("'                //     -|- \  ON ME AAAAAH!!!!!!!!!   /                                                  '"))
    print(str("'                //      /\     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                                    '"))
    space()
#drawing the Injustices Bane Stabbing you to death
def stab():
    space()
    print(str("'                                    @          __________________________________________           '"))
    print(str("'                                   -|-!       /NO NO NO youve already chopped off my arms\          '"))
    print(str("'                                    /\    >-@ <    Please don't kill me i beg of you      |           '"))
    print(str("'                                              \  Come on we can be friends please  man   /          '"))
    print(str("'                                               ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯           '"))
    space()
#drawing the Injustices Bane dying to you
def kill():
    space()
    print(str("'                                    @          __________________________________________           '"))
    print(str("'                                   -|-!       /NO NO NO please don't kill me             \          '"))
    print(str("'                                    /\    >-@ < I'll let you rule the Abyssmal City please|           '"))
    print(str("'                                              \I'll actually bring justice, please dont  /          '"))
    print(str("'                                               ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯           '"))
    space()
#drawing the One-Shot ending
def oneshot():
    space()
    print(str("'                                       ________________________________________                  '"))
    print(str("'                                      /Dayum, I thought that guy was meant to  \                 '"))
    print(str("'                                  @  < be tough, And yet i just killed him in   |                  '"))
    print(str("'                                 -|-! \one strike, Easiest kill of my life!!!  /                 '"))
    print(str("'                              >-@  /\    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                  '"))
    space()
#drawing the phew that close ending
def phew():
    space()
    print(str("'                                            ______________________________                          '"))
    print(str("'                                           /Huph Huph Huph Huph Huph      \                         '"))
    print(str("'                                        @  < Phew That was close             |                          '"))
    print(str("'                                      /&   \ One more hit and I'd be dead /                         '"))
    print(str("'                                 >-@ /\     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                          '"))
    space()
#drawing the saviour ending
def save():
    space()
    print(str("'                     _______________________________                                                '"))
    print(str("'                    / Come On Guys we gotta hurry   \                          ___________________  '"))
    print(str("'                @  < We Gotta go before they find us |             @  @  @  @ < We're coming!!!!!!| '"))
    print(str("'               -|-  \ Otherwise they'll kill us all /             >| >| >| >|  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯  '"))
    print(str("'                 /\    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                /\ /\ /\ /\                       '"))
    space()
#drawing the guard catching you
def guard():
    space()
    print(str("'                                 ___________________________              _____      _____         '"))
    print(str("'                           @    < Hey no opening their cells|       @    /  @  \    /  @  \        '"))
    print(str("'                          -|-!   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯       -|-~#|  -|-  |  |  -|-   |        '"))
    print(str("'                           /\                                       /\    |   /\    |  |    /\  |        '"))
    space()
#drawing Injustice Bane laughing at you and killing you
def laugh():
    space()
    print(str("'                                              __________________________                           '"))
    print(str("'                                             /HAHAHAHAHAHAHAHAHAHAHAHAHA\                          '"))
    print(str("'                                         @  <   Look at that his head   |                            '"))
    print(str("'                                -|-    !-|-  \It's rolling on the ground/                          '"))
    print(str("'                                 /\  @   /\     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                           '"))
    space()
#drawing the immigration ending
def leaving():
    space()
    print(str("'                          __________________                                                     '"))
    print(str("'                         / Giddey Up Horsey \                                                    '"))
    print(str("'                        |  We are leaving    >      @     /¯¯¯¯¯¯\                               '"))
    print(str("'                         \   This Town      /     _#|__@ < NEIGH! |                              '"))
    print(str("'                          ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   #~|__\_|   \______/                               '"))
    print(str("'                                                //   \\                                          '"))
    space()
#drawing the selfish ending
def hiding():
    space()
    print(str("'                                              ________________                                   '"))
    print(str("'                               ##### ___     /  No way they   \                                  '"))
    print(str("'                              ######/ @ \   <   Find me in     |                                 '"))
    print(str("'                             ###||#| -|- |   \ this treehouse /                                  '"))
    print(str("'                            ####||#|  /\   |    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                   '"))
    print(str("'                           ###\\|| //¯¯¯¯                                                        '"))
    print(str("'                             ##\||//                                                             '"))
    print(str("'                                ||/                                                              '"))
    print(str("'                                ||                                                               '"))
    print(str("'                                || ##                                                            '"))
    print(str("'                             ## ||####                                                           '"))
    print(str("'                            ####||//##                                                           '"))
    print(str("'                            ##\\||/#                                                             '"))
    print(str("'                               \||                                                               '"))
    print(str("'                                ||                                                               '"))
    print(str("'                                ||                                                               '"))
    space()
#drawing the uppercut finisher
def uppercut():
    space()
    print(str("'                                        _____________                                          '"))
    print(str("'                                       / HELP!!!!!!! \                                         '"))
    print(str("'                                      < I'm STUCK IN |                                         '"))
    print(str("'                             \@/       \ THE ROOF!!! /                                         '"))
    print(str("'                     _________|_______  ¯¯¯¯¯¯¯¯¯¯¯¯¯                                          '"))
    print(str("'                              /\    _______________                                              '"))
    print(str("'                                 /   DAYUUMMMM   \                                             '"))
    print(str("'                             @  <   That was a   |                                             '"))
    print(str("'                            -|/  \ NICE UPPERCUT /                                             '"))
    print(str("'                             /\     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                              '"))
    space()
#drawing the beheading finisher
def behead():
    space()
    print(str("'                         ____________________                                                     '"))
    print(str("'                        / LOOK AT THAT, I    \                                                    '"))
    print(str("'                       | CHOPPED HIS HEAD OFF >  @               |                                '"))
    print(str("'                       | AND THE SWORD GOT   |   |-     -|-     -|                                '"))
    print(str("'                        \ STUCK IN THE WALL /    /\       /\  @    |                                '"))
    print(str("'                         ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                                      '"))
    space()
#drawing the halved ending
def halved():
    space()
    print(str("'                                          _________                                                 '"))
    print(str("'                                         / OOPS I   \                                                 '"))
    print(str("'                                 @     @ < SPLIT HIM|                                                 '"))
    print(str("'                                 | |   !-|- \ IN TWO    /                                                 '"))
    print(str("'                                / \   /\   ¯¯¯¯¯¯¯¯¯                                                  '"))
    space()
#drawing the chandelier ending
def chandelier():
    space()
    print(str("'                                  __________________                                          '"))
    print(str("'                     ! !         / OOP SNAP CRACKLE \                                         '"))
    print(str("'                     ! !     @  < AND OR POP HE IS  |                                         '"))
    print(str("'                    /!#!\   -|-  \  DEAD AND STUCK  /                                         '"))
    print(str("'                   \#####/   /\     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                          '"))
    print(str("'                     >V@                                                                      '"))
    space()
#drawing the WWE ending
def WWE():
    space()
    print(str("'                                         /¯¯¯¯¯¯¯¯¯¯¯¯\                                              '"))
    print(str("'                                  @+-<  <  RKO OUTTA  |                                              '"))
    print(str("'                                         \ NOWHERE!!! /                                              '"))
    print(str("'                                   @        ¯¯¯¯¯¯¯¯¯¯¯¯                                               '"))
    print(str("'                                 -\-      *INSERT WWE.MP3*                                           '"))
    print(str("'                                  /\                                                                 '"))
    space()
#drawing the twister ending
def twist():
    space()
    print(str("'                            @               _________________                                        '"))
    print(str("'                           -|-             / HEY YOU CANT    \                                       '"))
    print(str("'                           /\         >&@ <  LEAVE ME WITH A |                                       '"))
    print(str("'                                           \ KNOT IT MY BODY /                                       '"))
    print(str("'                                            ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                        '"))
    space()
#drawing the parry ending
def parry():
    space()
    print(str("'                      _____________________                                                        '"))
    print(str("'                     /  You really think   \                                                       '"))
    print(str("'                     | an attack like that  >   @  @                                               '"))
    print(str("'                     \    can hit me ?!    /    |%-|                                               '"))
    print(str("'                      ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯     /\  /\                                               '"))
    space()
#drawing the juggling ending
def juggle():
    space()
    print(str("'                               _____________________                                                '"))
    print(str("'                              / Can You Please Stop \                                               '"))
    print(str("'                        @ &  < Playing Keepy Uppies  |                                              '"))
    print(str("'                        |_    \   With My Body!!!   /                                               '"))
    print(str("'                         \     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                                '"))
    space()
#drawing the horse ending
def horse():
    space()
    print(str("'                                  _____@        ___________________                                  '"))
    print(str("'            @ *WHISTLES*       #~|____|      /  NO WAY I DIED     \                                  '"))
    print(str("'           -|-                    //   \\ >-@ < BECAUSE THIS HORSE |                                 '"))
    print(str("'             /\                                 \  TRAMPLED ON ME     /                                  '"))
    print(str("'                                                       ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                   '"))
    space()
#drawing the dunked on ending
def dunk():
    space()
    print(str("'                            _____                                                                   '"))
    print(str("'                           |     |                                                                  '"))
    print(str("'                           |_[ ]_|  ____________                                                    '"))
    print(str("'                            @/  #    / NO WAY HE  \                                                   '"))
    print(str("'                            |    @  < DUNKED ON ME |                                                    '"))
    print(str("'                           /\ -|-  \ AND I DIED /                                                   '"))
    print(str("'                                /\   ¯¯¯¯¯¯¯¯¯¯¯¯                                                     '"))
    space()
#drawing the backstabbing ending
def backstabbing():
    space()
    print(str("'                                   ________________________            ______                        '"))
    print(str("'                            ___   /  PSST Hey help me get   \          / Okie \                        '"))
    print(str("'                           / @ \ <  outta here I mean your  |    @   <  Dokie |                      '"))
    print(str("'                          | -|- |  \ boss is terrible right /    -|-   \______/                        '"))
    print(str("'                          | /\  |   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯      /\                                                   '"))
    space()
#drawing the intimidator ending
def intimidator():
    space()
    print(str("'                                               _____________________________                        '"))
    print(str("'                                              /  AYO little man You better  \                       '"))
    print(str("'                                    @    @   <  Believe what I say or else   |                        '"))
    print(str("'                                   -|-  /|\   \  I might beat you to a pulp /                       '"))
    print(str("'                                      /\   /\     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                          '"))
    space()
#drawing the persuader ending
def persuader():
    space()
    print(str("'               ___________                   _____________________________                          '"))
    print(str("'              /   Uh Huh  \                 / Hey man there are some guys \                         '"))
    print(str("'              |  I believe  >       @    @   <  who want to kill you in the  |                          '"))
    print(str("'              \ You 100%  /      -|-  -|-   \  the paladins its not good  /                         '"))
    print(str("'               ¯¯¯¯¯¯¯¯¯¯¯          /\   /\     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                            '"))
    space()
#drawing the promotion ending
def promotion():
    space()
    print(str("'               ______________                   _____________________________                        '"))
    print(str("'              / Yeah I'd like\                 / I'd Like to give a toast to \                       '"))
    print(str("'              | Like to thank  >       @    @   <   my new second in command    |                      '"))
    print(str("'              \ To thank mum /      -|-  -|-   \  and his effort towards us  /                       '"))
    print(str("'               ¯¯¯¯¯¯¯¯¯¯¯¯¯¯          /\   /\      ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                        '"))
    space()
#drawing the demotion ending
def demotion():
    space()
    print(str("'               ______________                   _____________________________                        '"))
    print(str("'              / I promise to \                 / And that my paladins is why \                       '"))
    print(str("'              |work a lot more >            @   <   you never ever ever should  |                      '"))
    print(str("'              \ fr...        /      -|-  -|-   \  want to be demoted by me   /                       '"))
    print(str("'               ¯¯¯¯¯¯¯¯¯¯¯¯¯¯       @  /\   /\      ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                        '"))
    space()
#drawing the mutiny ending
def mutiny():
    space()
    print(str("'                                        ______________________                                        '"))
    print(str("'                                       / Alright boys how are \                                       '"))
    print(str("'                    @   @   @   @   @  < we going to kill the    |                                      '"))
    print(str("'                   -|- -|- -|- -|- -|-   \   Injustices Bane?     /                                       '"))
    print(str("'                   /\  /\  /\  /\  /\   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                        '"))
    space()
#drawing the caughtlying ending
def caughtlying():
    space()
    print(str("'               ______________                   _____________________________                        '"))
    print(str("'              /  You have to \                 / And that my paladins is why \                       '"))
    print(str("'              | believe me or  >            @   <  you never ever decide to lie |                      '"))
    print(str("'              \ else th...   /      -|-  -|-   \ to me about anything at all /                       '"))
    print(str("'               ¯¯¯¯¯¯¯¯¯¯¯¯¯¯       @  /\   /\      ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                        '"))
    space()
#drawing the exhaustion ending
def exhaustion():
    space()
    print(str("'                               _________________________                                              '"))
    print(str("'                             / Ya know, huph, all this   \                                            '"))
    print(str("'                           @  < work Ive been doing has   |                                             '"))
    print(str("'                          /!  \ been making me exhaus... /                                            '"))
    print(str("'                        /\     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                             '"))
    space()
#drawing the stupidity ending
def stupidity():
    space()
    print(str("'                  _____                   ___________________________                                 '"))
    print(str("'                 / My  \                 / Are you dumb? There Arent   \                                '"))
    print(str("'                  | Bad  >     @     @    <  even that many hours in a  |                               '"))
    print(str("'                 \ G.../        -|-   -|-    \ week. Guards!!! Seize him /                                '"))
    print(str("'                  ¯¯¯¯¯     /\    /\      ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                 '"))
    space()
#drawing the picture for if you get all achievements
#the two initial variables are to engrave the players initials onto the trophy
def trophy():
    space()
    print(str("'                           _______                                                                    '"))
    print(str("'                           [|       |]                                                                  '"))
    print(str("'                           \ {1} /                                                                    '"))
    print(str("'                             \     /                                                                    '"))
    print(str("'                          __|   |__                                                                   '"))
    print(str("'                           /   WIN   \                                                                  '"))
    print(str(f"'                         /     {initial1}.{initial2}     \                                                                '"))
    print(str("'                        ¯¯¯¯¯¯¯¯¯¯¯¯¯                                                                 '"))
    space()
def instructions():
    print("First things first, how do you play the game?")
    print("The game is very simple, you'll be asked to type answers which correspond to actions so you can progress.")
    print("When typing your answer make sure you include only the answer, no spaces, no capitals, just the answer.")
    print("If you die or beat the game, a picture will appear corresponding to what happened.")
    print("When you're done looking at the image, press enter to continue with the game, don't just quit.")
    print("Furthermore if the game seems to stop asking for your input, just press enter, I only do that to space out text.")
    print("Almost every action's outcome is chance based so picking the same path can cause different story.")
    print("These chance based outcomes are effected by the class you pick at the start so choose wisely!")
    print("When you beat the game you'll be allowed to play again, and pick an extra class.")
    print("This allows you to have multiple classes at once, however if you die you lose them all.")
    print("The game has a total of 18 achievements and you only get a few of them from choosing your class.")
    print("That leaves a plethora of achievements for beating the game differently so go catch 'em all.")
    print("Once you understand these instructions just type enter to continue to the game.")
    input("Good Luck!!!")
opening()
space()
space()
space()
instructions()
#creating a while true loop that continuesly checks the players position and puts them in the right scenario
while True:
    #checking if the player has died
    if (playerhp == 0):
        space()
        print("You died.")
        playerpos = "7"
        stab()
    #creating start point position
    if (playerpos == "0"):
        space()
        space()
        space()
        space()
        totalhours = float(0)
        workhours = float(0)
        overwork = float(0)
        commendation = float (0)
        correct = float(0)
        treedeath = float(0)
        hp = float(0)
        playerhp = float(8)
        underwork = float(0)
        #displaying the classes available and allowing the player to pick one
        print("Pick a class from the following options:")
        if ("b" not in classes):
            print("Bodybuilder: You have extreme strength (type b)")
        if ("g" not in classes):
            print("Gymnast: You have extreme flexibility and agility (type g)")
        if ("t" not in classes):
            print("Tank: You are abnormally pain tolerant and very thickskinned (type t)")
        if ("m" not in classes):
            print("Martial Artist: You find it easy to strike others however your hits might not be that powerful (type m)")
        if ("r" not in classes):
            print("Robber: You are very good at stealing things and distracting others (type r)")
        if ("c" not in classes):
            print("Chatterbox: You are very charismatic and have a fun aura about you (type c)")
        if("b" in classes and "g" in classes and "t" in classes and "m" in classes and "r" in classes and "c" in classes and "f" not in classes):
            print("The Fabled Hero: You are an extremely powerful superhero renowned throughout the lands for being able to do everything (type f)")
        if("h" not in classes):
            print("Make Belief Hero: You 'think' you are some superhero and can do everything, however your probably just schizophrenic (type h)")
        print("If you type anything other then what I've said to type you will go classless.")
        #adding the class the player picked to the game
        inputspace()
        classes.append(input("Type your answer here: "))
        inputspace()
        firstname = input("What is your first name: ")
        lastname = input("What is your last name: ")
        initial1 = firstname[0]
        initial2 = lastname[0]
        initial1 = initial1.upper()
        initial2 = initial2.upper()

        space()
        print("Now then, " + firstname + " " + lastname + ", Welcome to the Abyssmal City where no dreams come true and the Paladins of 'justice' always bring 'justice' to the lands")
        print("The Paladins are led by the Injustices Bane, an abnormally large person who captures innocent people for fun and is the cruel dictator of the Abyssmal City")
        print("Now that we have the backstory out the way, let us start your story.")
        input()
        playerpos = "2"
        if ("t" in classes):
            playerhp = float(11)
    #checking for achievements and then displaying that you got it if you have it
    if ("c" in classes and "c" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("Unlock the Chatterbox class")
        achpercent = achpercent + 1
        achievements.append("c")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("b" in classes and "b" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("Unlock the Bodybuilder class")
        achpercent = achpercent + 1
        achievements.append("b")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("r" in classes and "r" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("Unlock the Robber class")
        achpercent = achpercent + 1
        achievements.append("r")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("g" in classes and "g" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("Unlock the Gymnast class")
        achpercent = achpercent + 1
        achievements.append("g")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("m" in classes and "m" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("Unlock the Martial Artist class")
        achpercent = achpercent + 1
        achievements.append("m")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("t" in classes and "t" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("Unlock the Tank class")
        achpercent = achpercent + 1
        achievements.append("t")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("b" in classes and "g" in classes and "t" in classes and "m" in classes and "r" in classes and "f" in classes and "f" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("Unlock the Fabled Hero class")
        achpercent = achpercent + 1
        achievements.append("f")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("h" in classes and "h" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("Unlock the Make-Belief Hero class")
        achpercent = achpercent + 1
        achievements.append("h")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("KO1" in achievements and "KO2" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("Kill the Injustices Bane with Style Points")
        achpercent = achpercent + 1
        achievements.append("KO2")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("hide1" in achievements and "hide2" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("Hide in the treehouse")
        achpercent = achpercent + 1
        achievements.append("hide2")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("immigrate1" in achievements and "immigrate2" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("Leave with your horse")
        achpercent = achpercent + 1
        achievements.append("immigrate2")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("duelist1" in achievements and "duelist2" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("Kill the Injustices Bane regularly")
        achpercent = achpercent + 1
        achievements.append("duelist2")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("onetap1" in achievements and "onetap2" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("You killed the Injustices bane in one hit")
        achpercent = achpercent + 1
        achievements.append("onetap2")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("phew1" in achievements and "phew2" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("You killed the Injustices Bane with one 1HP left")
        achpercent = achpercent + 1
        achievements.append("phew2")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("first1" in achievements and "first2" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("You Beat the game for your first time")
        achpercent = achpercent + 1
        achievements.append("first2")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("mutiny1" in achievements and "mutiny2" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("You led a mutiny among the paladins")
        achpercent = achpercent + 1
        achievements.append("mutiny2")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("snitch1" in achievements and "snitch2" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("You snitched on the traitorous paladins")
        achpercent = achpercent + 1
        achievements.append("snitch2")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if ("fakeletter1" in achievements and "fakeletter2" not in achievements):
        space()
        print("Congratulations on your achievement: ")
        print("You tricked a paladin into backstabbing")
        achpercent = achpercent + 1
        achievements.append("fakeletter2")
        print("You have acquired: " + str(achpercent) + " of the 18 achievements")
        space()
    if (achpercent == 18):
        space()
        print("Congratulations on getting every achievement in the game")
        trophy()
        achpercent = achpercent + 1
        space()
    #setting all the random dice rolls based off class
    selfish = random.randint(1,2)
    if ("c" in classes):
        talk = random.randint(1,2)
        fakeletter = random.randint(1,2)
        persuade = random.randint(1,2)
    else:
        talk = random.randint(1,3)
        fakeletter = random.randint(1,4)
        persuade = random.randint(1,3)
    if("b" in classes):
        onetap = random.randint(1,2)
        if (hp > 8):
            finisher = 8
        else:
            finisher = random.randint(hp,8)
        damage = float(2)
        intimidate = random.randint(1,2)
    else:
        onetap = random.randint(1,5)
        if (hp > 8):
            finisher = random.randint(8,9)
        else:
            finisher = random.randint(hp,9)
        damage = float(1)
        intimidate = random.randint(1,3)
    if ("m" in classes):
        attack = random.randint (2,4)
        fight = random.randint(1,2)
    else:
        attack = random.randint (2,5)
        fight = random.randint(1,3)
    if("g" in classes):
        dodge = random.randint(2,5)
        hide = random.randint(1,3)
    else:
        dodge = random.randint(1,5)
        hide = random.randint(2,3)
    if("r" in classes):
        escape = random.randint(1,2)
        lockpick = 1
    else:
        escape = random.randint(1,3)
        lockpick = random.randint(1,2)
    if("h" in classes):
        damage = float(1)
        finisher = random.randint(hp,13)
        attack = random.randint(2,6)
        fight = random.randint(1,4)
        dodge = random.randint(1,6)
        hide = 3
        escape = random.randint(1,4)
        lockpick = random.randint(1,3)
    if("b" in classes and "g" in classes and "t" in classes and "m" in classes and "r" in classes and "f" in classes and "c" in classes):
        damage = float(3)
        finisher = 8
        attack = 4
        fight = 1
        hide = 2
        dodge = 4
        escape = 1
        lockpick = 1
        onetap = 1
        fakeletter = 1
        talk = 1
        persuade = 1
        intimidate = 1
    if("armour1" in classes and "armour2" not in classes):
        playerhp = playerhp + 2
        damage = damage + 1
        classes.append("armour2")
    #placing the player in the first position in the game (Start point)
    if (playerpos == "2"):
        space()
        #creating the secret ending for when you have every class
        if("b" in classes and "g" in classes and "t" in classes and "m" in classes and "r" in classes and "f" in classes):
            #asking where they want to go
            print("You wake up on a new day after a long day of chopping trees yesterday.")
            yesorno = input("Today you can either go to town(type t), stay chopping trees (type c) or rush Injustice Bane's Castle (type r): ")
        else:
            #regular start point for those without all classes and asking them what their first choice is
            print("You wake up on a new day after a long day of chopping trees yesterday.")
            yesorno = input("Today you can either go to town(type t) or stay chopping trees (type c): ")
        #outcome of choosing "t"
        if (yesorno == "t"):
            playerpos = "1"
        #outcome of choosing "c"
        elif (yesorno == "c"):
            treedeath = treedeath + 1
            if (treedeath > 4):
                #creating a secret death that happens if you chop trees too much
                space()
                print("A tree falls on your head whilst you're chopping down trees and you die.")
                playerpos = "7"
                #printing the tree death cutscene
                log()
        #outcome of picking the secret ending "r"
        elif("b" in classes and "g" in classes and "t" in classes and "m" in classes and "r" in classes and "f" in classes and yesorno == "r"):
            print("You rush the castle doing your regular superhero activities.")
            playerpos = "10"
    #checking if the players position is in town
    if (playerpos == "1"):
        space()
        print("You have arrived in town and go to the bar to grab a drink.")
        print("After a good catch up with some mates in the bar you walk out and see some paladins of 'justice' in the distance coming towards you.")
        #asking them what they are gonna do in town
        inputspace()
        yesorno = input("What do you do, run and hide (type h), stay for a chat (type c), or try and fight (type f): ")
        #outcome of picking "f"
        if (yesorno == "f"):
            space()
            print("You pull out a sword and...")
            #checking the players dice roll based on class and deciding outcome
            if (fight == 1):
                print("You kill the paladins. On your way home you spot a bounty poster with your face on it.")
                print("The poster says Wanted for the killing of multiple paladins.")
                playerpos = "3"
                input()
            else:
                print("The fight seems to be going well and you knock one of the paladins out.")
                print("Whilst you're fighting the final two one of them disappears.")
                print("As you're turning around to find him he appears behind you.")
                print("He hits you on the top of your head with the hilt of his sword.")
                print("You are knocked out.")
                playerpos = "4"
                input()
        #outcome of picking "h"
        elif (yesorno == "h"):
            space()
            print("You run and hide and...")
            #checking the players dice roll based on class and deciding outcome
            if (hide == 3):
                print("Unfortunately for you, you suck at hiding.")
                print("You attempted to hide around the back of the tavern hugging the wall hoping no one would find you.")
                print("A paladin finds you instantly and before you can say a word he knocks you out.")
                playerpos = "4"
                input()
            else:
                print("Your hiding skills are unmatched and no paladin is able to find you")
                print("You decided to hop inside one of the crates behind the tavern.")
                print("You hear one of the paladins roaming around your crate, but they never check it.")
                print("Once the coast is clear you hop out of the crate and head home.")
                print("On your way home you see a wanted sign with your name on it.")
                print("The sign reads: Wanted for not showing up to roll call.")
                playerpos = "3"
                input()
        #outcome of picking "c"
        elif (yesorno == "c"):
            space()
            print("You stay for a chat.")
            print("One of the paladins asks why you aren't at work right now.")
            inputspace()
            yesorno = input("Do you say you're quitting your job to join them (type q), or Do you say you were on your way to work (type w): ")
            #outcome of picking "q"
            if (yesorno == "q"):
                print("You tell them you want to enlist for the paladins of justice.")
                if(talk == 1):
                    print("They seem happy with your answer and tell you that you have to go to the castle to enlist.")
                    print("You begin walking towards the castle.")
                    playerpos = "11"
                    input()
                else:
                    print("They claim your lying and say the punishment for that is jail before knocking you out")
                    playerpos = "4"
                    input()
            #outcome of picking "w"
            if (yesorno == "w"):
                print("You tell them you're on your way to work.")
                if(talk == 1):
                    print("They seem confused by your answer but say it's alright and let you go on your way back home.")
                    if(treedeath < 3):
                        print("When you get home you find a letter at your door saying you didn't meet the Injustices Bane Quota of wood chopped.")
                        playerpos = "3"
                        input()
                    else:
                        print("When you get home you find a letter at your door saying the Injustices Bane wishes to reward you for your amazing tree chopping efforts")
                        print("You have been invited to the Injustice Bane Castle to apply for the paladin job")
                        playerpos = "11"
                        input()
                else:
                    print("They claim you're lying and say the punishment for lying is solitary confinement before knocking you out.")
                    playerpos = "4"
                    input()
    #checking if the player is at home after disobeying the Injustices Bane
    if (playerpos == "3"):
        space()
        print("You wake up the next morning and whilst you're eating breakfast you hear a knock at your door.")
        print("You open the door to find the Injustices Bane standing face to face with you.")
        print("He claims you've done him wrong and that now you must duel")
        #asking the player if they accept or decline his duel
        inputspace()
        yesorno = input("Do you accept the duel (type a) or do you decline (type d): ")
        #outcome of accepting
        if (yesorno == "a"):
            print("")
            print("You accept the duel and you both take out your swords.")
            input()
            playerpos = "5"
        #outcome of declining
        elif (yesorno == "d"):
            print("")
            print("You decline his duel and in a fit of rage he knocks you out.")
            playerpos = "4"
            input()
    #checkiing if the player is in The Injustice Bane's dungeon
    if (playerpos == "4"):
        space()
        print("You wake up in a dungeon that is dimly lit with many others in seperate cells as well.")
        print("You look at the guard and he seems unfocused, like he is hating his job right now.")
        print("You consider this for a bit and come to the conclusion that there is a chance at escape.")
        #asking them what they wanna do in the dungeon
        inputspace()
        yesorno = input("Do you try and distract the guard and escape (type e), do you try and talk the guard into mutiny (type m) or do you wait in your cell (type w): ")
        #outcome of trying to escape
        if (yesorno == "e"):
            space()
            print("You throw a rock to try and distract the guard and...")
            #outcome of dice roll based on class
            if (escape == 1):
                print("The distraction works!!!")
                print("The guard walks towards your cell and bends over to pick up the rock.")
                print("As he is picking up the rock you reach through the iron bars and knock him out.")
                print("You grab the keys off his unconscious body and escape your cell.")
                print("You start leaving when the other inmates start pleading that you save them.")
                #asking the player if they want to save the others or themself
                inputspace()
                yesorno = input("Do you try and save the other inmates (type i), or do you go and save yourself (type y): ")
                #outcome of trying to save the inmates
                if (yesorno == "i"):
                    space()
                    print("You go to save the inmates however the keys aren't working.")
                    #asking them if they want to continue trying to save the inmates or save themself
                    inputspace()
                    yesorno = input("Do you try and lockpick their cells open (type p), or do you try and save yourself (type y): ")
                    #outcome of trying to further save the inmates
                    if (yesorno == "p"):
                        space()
                        print("You begin lockpicking their cells open and...")
                        #random dice roll based on class to decide outcome
                        if (lockpick == 1):
                            print("You manage to open everyones cells.")
                            print("You all run up the stairs out of the dungeon and escape through a side door in the castle.")
                            print("You're now the peoples hero of the Abyssmal City and everyone loves you.")
                            print("You won the saviour way.")
                            playerpos = "6"
                            #printing the saviour win cutscene
                            save()
                        else:
                            print("After you open the first inmates cell a guards spots you.")
                            print("He charges at you before chopping your head off.")
                            print("You Died.")
                            playerpos = "7"
                            #printing the guard death cutscene
                            guard()
                    #outcome of saving yourself
                    elif (yesorno == "y"):
                        space()
                        print("You start running for your life and...")
                        #random dice roll based on class to decide outcome
                        if (selfish == 1):
                            print("As your running you're shot in the back by many arrows.")
                            print("You died.")
                            playerpos = "7"
                            #printing the arrow death cutscene
                            arrow()
                        else:
                            print("You run all the way back to your lodge leaving the other inmates behind to die before you go into hiding.")
                            print("You won the selfish way.")
                            achievements.append("hide1")
                            playerpos = "6"
                            #printing the hiding win cutscene
                            hiding()
                #outcome of deciding to save yourself
                elif (yesorno == "y"):
                    space()
                    print("You start running for your life and...")
                    #random dice roll based on class to decide outcome
                    if (selfish == 1):
                        print("As your running you're shot in the back by many arrows.")
                        print("You died.")
                        playerpos = "7"
                        #printing the arrow death cutscene
                        arrow()
                    else:
                        print("You run all the way back to your lodge pack your things and leave to another 'safer' city.")
                        print("You won the immigration way.")
                        achievements.append("immigrate1")
                        playerpos = "6"
                        #printing the leaving win cutscene
                        leaving()
            else:
                print("Clearly you don't know how to distract someone as that distraction was terrible.")
                print("The guard doesn't flinch.")
                print("After a few minutes some guards come to escort you to the throne room.")
                print("They drag you up the stairs towards the throne room.")
                playerpos = "9"
                input()
        #outcome of choosing to wait
        elif (yesorno == "w"):
            space()
            print("You wait for roughly 20 minutes keeping to yourself and meditating.")
            print("A group of guards come to escort you to the throne room.")
            print("They grab you vigorously and drag you up the stairs towards the throne room.")
            playerpos = "9"
            input()
        elif (yesorno == "m"):
            print("You whisper to the guard and try and persuade him to let you out.")
            if(fakeletter == 1):
                print("After gaslighting him into thinking that the Injustices Bane is a terrible person he lets you out")
                print("He gives you a broadsword and armour set to look like a guard as well before you head up to throne room")
                print("As you're going up the stairs to the throne room a prisoner asks you if you'll come back for them.")
                print("You ask the guard if we can let them all out before you go up stairs and he nods.")
                print("He hands you the keys and you open everyones cells, they all instantly run to the other end of the dungeon.")
                print("They open a hatch at the other end and begin climbing through it one by one.")
                print("As the final one is leaving he thanks you for saving him and then hops out closing the hatch behind himself.")
                print("You take a moment for sentiment before following the the guard towards the throne room.")
                input()
                space()
                print("In the throne room you find the Injustices Bane sat down and watching a Jester perform for him")
                print("The guard who helped you tells the Injustices Bane that he has recieved a letter for him")
                print("The Injustices Bane asks for the letter and as he is handing him the letter")
                print("He whispers something in the Injustices Bane before pulling out a sword and stabbing the Injustices Bane straight in the heart")
                input()
                print("You won the fake letter way")
                achievements.append("fakeletter1")
                backstabbing()
                playerpos = "6"
            else:
                print("The guard tells you that mutiny is completely against the law and the punishment is death.")
                print("He chops your head off and you die.")
                failedmutiny()
                playerpos = "7"
    #checking if the player accepted the duel and is in the duel area
    if (playerpos == "5"):
        space()
        print("After going through the formal procedures before the start of a fight he starts laughing at you.")
        print("Spontaneously in the middle of his laugh he quickly takes a stab at you.")
        print("How do you react?")
        #asking the player for their first move in the duel
        inputspace()
        yesorno = input("Do you try and stab him before he stabs you (type s), do you try and dodge his attack (type r) or do you go for a finishing blow (type b): ")
        #outcome of deciding to try and stab him
        if (yesorno == "s"):
            space()
            print("You go for a stab at him before he can stab you and...")
            #random dice roll based on class to decide outcome
            if (attack == 4):
                print("You manage to land a hit!")
                hp = hp + damage
                playerpos = "8"
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
            elif (attack == 3):
                print("You trade blows with each other!")
                playerhp = playerhp - 1
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
                playerpos = "8"
                hp = hp + damage
            else:
                print("You miss and he manages to stab you!")
                playerhp = playerhp - 1
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
                playerpos = "8"
        #outcome of deciding to try and dodge roll
        elif (yesorno == "r"):
            space()
            print("You try and roll out the way of his attack and...")
            #random dice roll based on class to decide outcome
            if (dodge == 4):
                print("You roll out the way and somehow hit him in the process!")
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
                hp = hp + damage
                playerpos = "8"
            elif (dodge == 3):
                print("You manage to dodge but you completely miss the attack!")
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
                playerpos = "8"
            else:
                print("You completely miss the dodge and he hits you!")
                playerhp = playerhp - 1
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
                playerpos = "8"
        #outcome of deciding to try and kill him straight away
        elif (yesorno == "b"):
            space()
            print("You attempt to go for a finishing blow and...")
            #random dice roll based off class to decide outcome
            if (onetap == 2):
                print("You kill him easily and have now freed the lands from injustice's banes wrath!")
                print("You won the 'one shots all i need' way.")
                playerpos = "6"
                oneshot()
            else:
                print("You completely miss your attack and take a hit!")
                playerhp = playerhp - 1
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
                playerpos = "8"
    #checking if the player has beat the game and is now in the win area
    if (playerpos == "6"):
        inputspace()
        input("Welcome to the hall of winners =>")
        space()
        print("Congratulations on completing Paladins of Justice!!!")
        print("Here is your medal:")
        space()
        print("'          \   /                                     '")
        print("'           \_/                                      '")
        print("'           |$|                                      '")
        space()
        achievements.append("first1")
        #asking if the player wants to play again or not
        again = input("Would you like to play again? (type y for yes and n for no): ")
        #outcome of deciding to play again
        if (again == "y"):
            print("Good luck in your next adventure then!!!")
            space()
            space()
            space()
            playerpos = "0"
            #outcome of deciding to stop playing
        elif (again == "n"):
            print("Bye Bye")
            sys.exit()
    #checking if the player has died and is in the death area
    if (playerpos == "7"):
        inputspace()
        input("Welcome to valley of death => ")
        input()
        space()
        print("A tall, bodyless figure stands before wearing a dark robe that covers his face.")
        print("Suddenly a voice comes from inside the robe, Ah Great another dead fellow it says sounding annoyed by you.")
        print("Guess I gotta ask the same stupid question again it groans begrudgingly.")
        inputspace()
        #asking if the player wants to try again or quit the game
        again = input("Would you like to be reincarnated? (type y for yes and n for no): ")
        #outcome of wanting to try again
        if (again == "y"):
            print("Alrighty 1 serve of reincarnation coming right up.")
            input()
            space()
            space()
            space()
            space()
            playerpos = "0"
            playerhp = float(5)
            classes.clear()
            classes.append("player")
        #outcome of quiting the game
        elif (again == "n"):
            print("I think you might be the only person I've met that would like to stay here.")
            print("Well I'm sending you elsewhere, Bye Bye!!!")
            sys.exit()
    #checking if the player is in the fight scene area
    if (playerpos == "8"):
        space()
        print("He starts charging you, how do you proceed?")
        inputspace()
        #asking the player how they want to respond in the fight
        yesorno = input("Do you try and stab him before he stabs you (type s), do you try and dodge his attack (type r), or do you go for a finishing blow (type b): ")
        #outcome of trying and stab him
        if (yesorno == "s"):
            space()
            print("You go for a stab at him before he can stab you and...")
            #random dice roll based on class for deciding outcome
            if (attack == 4):
                print("You manage to land a hit!")
                hp = hp + damage
                playerpos = "8"
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
            elif (attack == 3):
                print("You trade blows with each other!")
                playerhp = playerhp - 1
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
                playerpos = "8"
                hp = hp + damage
            else:
                print("You miss and he manages to stab you!")
                playerhp = playerhp - 1
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
                playerpos = "8"
        #outcome of trying to dodge his attack
        elif (yesorno == "r"):
            space()
            print("You try and roll out the way of his attack and...")
            #random dice roll based off class for deciding outcome
            if (dodge == 4):
                print("You roll out the way and somehow hit him in the process!")
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
                hp = hp + damage
                playerpos = "8"
            elif (dodge == 2 or dodge == 3):
                print("You manage to dodge out the way!")
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
                playerpos = "8"
            else:
                print("You completely miss the dodge and he hits you!")
                playerhp = playerhp - 1
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
                playerpos = "8"
        #outcome of deciding to try and kill him
        elif (yesorno == "b"):
            space()
            print("You attempt to go for a finishing blow and...")
            #random dice roll based off class to decide outcome
            if (finisher == 8):
                if (playerhp == 1):
                    print("You kill him and have now freed the lands from injustice's banes wrath!")
                    print("You won the 'phew that was close' way!")
                    playerpos = "6"
                    phew()
                    achievements.append("phew1")
                else:
                    print("You kill him and have now freed the lands from injustice's banes wrath!")
                    print("You won the duelists way!")
                    kill()
                    playerpos = "6"
                    achievements.append("duelist1")
            else:
                print("You completely miss your attack and take a hit!")
                playerhp = playerhp - 1
                playerhealth = str(playerhp)
                print("Your current hp is: " + playerhealth)
                playerpos = "8"
    #checking if the player is in the throne room
    if (playerpos == "9"):
        space()
        print("You are chucked into the throne room and the doors are slammed behind you.")
        print("You are left at the foot of the Injustice Bane's chair with only you two in the room.")
        inputspace()
        #asking the player what they want to do in the throne room
        yesorno = input("Do you wait and see what he has to say (type u) or do you seize the opportunity to attack him (type o): ")
        #checking if the player decided to wait
        if (yesorno == "u"):
            space()
            print("You wait for what he has too say and after a moments pause he...")
            print("Starts laughing at you very loudly until he chops your head off in a swift blow!")
            print("You died.")
            playerpos = "7"
            laugh()
        #checking if the player is going to use the opportunity for an attack
        elif (yesorno == "o"):
            space()
            print("You catch him off guard and land a punch straight at his chin.")
            print("You quickly grab one of the swords from his waist before he can react.")
            print("You step away as he pulls out his other sword and you begin fighting.")
            hp = hp + damage
            playerpos = "8"
            input()
    #checking if the player has chosen to rush the castle
    if (playerpos == "10"):
        space()
        achievements.append("KO1")
        print("You rush the castle and jump straight through the window of the throne room.")
        print("Instantly 8 paladins swarm you pulling out swords.")
        print("With little to no effort you spin once with your sword and kill them all.")
        print("The Injustice Bane, pissed off now, starts charging you.")
        print("You start to think which way of killing him would be the best.")
        print("Pick a finishing move:")
        print("Uppercut (type u)")
        print("Beheading (type b)")
        print("Halved (type h)")
        print("Chandelier (type c)")
        print("WWE (type w)")
        print("Twister (type t)")
        print("Parry (type p)")
        print("Juggling (type j)")
        print("Horse??? (type h)")
        print("Dunked On (type d)")
        inputspace()
        KO = input("Answer Here: ")
        space()
        if (KO == "u"):
            inputspace()
            print("You dash directly in front of him and wind up an uppercut.")
            print("The uppercut sends him straight into the roof with his legs sticking out the bottom.")
            uppercut()
            playerpos = "6"
        elif (KO == "b"):
            inputspace()
            print("You throw your sword at his neck and in one swift cut his head falls off.")
            playerpos = "6"
            behead()
        elif (KO == "h"):
            inputspace()
            print("He walks over to you and just before he strikes you chop him in half straight down the middle.")
            playerpos = "6"
            halved()
        elif (KO == "c"):
            inputspace()
            print("You throw your sword up at the chandelier on the roof chopping the chain that holds it in the air.")
            print("The chandelier falls on the unsuspecting Injustices Bane impaling him and pinning him to the ground.")
            playerpos = "6"
            chandelier()
        elif (KO == "w"):
            inputspace()
            print("You grab him and throw him on the floor before proceeding to jump up and hang on the chandelier.")
            print("As he starts getting up from the ground you drop from the chandelier and body slam him 6ft under the ground.")
            playerpos = "6"
            WWE()
        elif (KO == "t"):
            inputspace()
            print("You walk over to him and knock the sword out of his hand.")
            print("As he tries to get another sword out you grab and restrain him holding him in your hands like a barbell.")
            print("After using him as weights to do some curls you twist his body into a knot and leave him there looking like a pretzel.")
            playerpos = "6"
            twist()
        elif (KO == "p"):
            inputspace()
            print("You drop your sword and tell him to try and hit you.")
            print("Pissed off by your cocky remark he starts charging you with a new anger.")
            print("He takes a large swing with his sword at you but you grab the sword with your bare hands.")
            print("You rip it out of his hands and stab him countless times with it.")
            playerpos = "6"
            parry()
        elif (KO == "j"):
            inputspace()
            print("You knock his sword out of his hand before picking him up and scrunching him into a ball.")
            print("You begin play keepy uppies with him and practice your juggling skills for soccer.")
            print("Eventually he manages to ask you to stop so you kick him into the throne leaving a massive indent in it.")
            print("And the crowd goes wild!!!! You scream, taunting him even further.")
            playerpos = "6"
            juggle()
        elif (KO == "h"):
            inputspace()
            print("You perform a special whistling call to summon your trusty sidekick HORSE.")
            print("HORSE crashes through the window and stampedes over the Injustices Bane leaving him as a flat rug on the ground.")
            playerpos = "6"
            horse()
        elif(KO == "d"):
            inputspace()
            print("You transform the throne room into a basketball court and summon all the citizens of the Abyssmal City into the stands using your magic.")
            print("A basketball hoop appears above the Injustices Bane and you jump in the air performing a 360 tomohawk dunk.")
            print("The ball goes straight through the basket and hits the top of the Injustice Bane's head.")
            print("The force of the impact caused the his head to be flattened and him to die.")
            playerpos = "6"
            dunk()
    #checking if the player is at the interview place for paladins
    if (playerpos == "11"):
        space()
        print("You arrive at the castle and find a queue of 3 people leading into a room with a big sign above it.")
        print("The sign reads 'Paladin Applicants here'.")
        print("You join the end of queue and wait your turn.")
        print("After a 30 minute wait a guard invites you into the room.")
        print("The room is dimly lit with a table in the room and two chairs.")
        print("A door leads into the castle on the otherside of the room.")
        print("The guard starts your interview and says you must answer 5 questions.")
        inputspace()
        #asking the player questions to see if they belong in the paladins of justice
        yesorno = input("Do you believe that justice is needed in this city? (type y for yes and n for no): ")
        if (yesorno == "y"):
            correct = correct + 1
        space()
        yesorno = input("Are you committed to justice? (type y for yes and n for no): ")
        if (yesorno == "y"):
            correct = correct + 1
        space()
        yesorno = input("Do you believe that everyone is equal? (type y for yes and n for no): ")
        if (yesorno == "n"):
            correct = correct + 1
        space()
        yesorno = input("What is a worthy punishment for a thief? (type b for beheading, h for hanging, w for whipping, and s for solitary confinement): ")
        if (yesorno == "b" or yesorno == "s"):
            correct = correct + 1
        space()
        yesorno = input("What is the minimum amount of hours that a citizen should work a week? (type 0, 10, 20, 30, 40, 100 or 'a' for as many as possible): ")
        if (yesorno == "a" or yesorno == "100"):
            correct = correct + 1
        space()
        if (correct == 5):
            print("Welcome to the paladins of justice! He exclaims in excitement.")
            print("Go through that door there and you will find your set of uniform, weapon, shield, horse and all the equipment you'll need as a paladin.")
            playerpos = "12"
            input()
        else:
            print("Citizens like you should who don't know the laws or share the same beliefs as the Injustices Bane should not be allowed in this city")
            print("He kills you for not following the Injustice Banes beliefs.")
            playerpos = "7"
    #checking if the player made it through the interview and into the paladins
    if (playerpos == "12"):
        space()
        print("You walk through the door and grab your new equipment before suiting up.")
        classes.append("armour1")
        print("Inside the locker room where your equipment is are two groups of Paladins seperated from one another.")
        print("Both groups of paladins are beckoning you over to them.")
        print("The group on the left seems very secretive and more introverted whereas the group on the right seems more public and extroverted.")
        inputspace()
        #asking the player which paladins "pathway" they wish to go down
        yesorno = input("Do you go to the group on the right (type r), or the group on the left (type l)?: ")
        if (yesorno == "l"):
            space()
            print("You walk to the group on the left and they instantly tell you to be quiet before asking you one question?")
            inputspace()
            #continuing to ask the player which paladins "pathway" they wish to go down
            yesorno = input("Do you like (type l), or dislike (type d) The Injustice Bane?: ")
            if (yesorno == "l"):
                space()
                print("They seem dissapointed by your answer and quickly disperse leaving you by yourself with the other group in the locker room.")
                print("The other group approaches you and gets straight to the point.")
                print("They tell you that the other group is trying to start a mutiny against the Injustices Bane and that your decision to leave them was justified.")
                print("They are trying to find a way to snitch on them but The Injustices Bane won't listen to them.")
                inputspace()
                yesorno = input("Do you tell them you can try and talk to him (type t), or do you ask for your first shift (type f)?: ")
                #continuing to ask the player which paladins "pathway" they wish to go down
                if (yesorno == "t"):
                    print("You see a glimmer of hope spark in their eyes as they instantly direct you to the Injustice Banes throne room.")
                    print("You enter the throne room.")
                    playerpos = "13"
                    input()
                elif (yesorno == "f"):
                    print("The guards seem dissapointed by your unwillingness to help them.")
                    print("One of the guards tells you to come with him for your first shift.")
                    print("You hop on your horses and go to town to perform roll call.")
                    print("You're told that you have to do roll call for the rest of the week.")
                    playerpos = "14"
                    input()
            elif (yesorno == "d"):
                space()
                print("Their expressions quickly change as they seem very pleased with your answer.")
                print("They scurry off beckoning you to follow them into this secret room.")
                print("Inside the secret room is a table surrounded by enough chairs for the lot of you.")
                print("On one wall you see a plan devised to kill the Injustices Bane.")
                print("Everyone sits down and they begin to tell you their entire plan to kill the Injustice Bane.")
                print("They ask you for your thoughts on the plan.")
                inputspace()
                #asking the player how they want to kill the injustices bane
                yesorno = input("Do you think it should be done at breakfast (type t), or at night (type a): ")
                if (yesorno == "a"):
                    space()
                    print("They all seem to agree with your idea and decide to enact it tonight.")
                    playerpos = "15"
                    input()
                elif (yesorno == "t"):
                    space()
                    print("They all seem to agree with your idea and decide to enact it tommorow during breakfast.")
                    playerpos = "16"
                    input()
        elif (yesorno == "r"):
            print("You walk over to the group on the right.")
            print("They ask one singular question in unison.")
            inputspace()
            #continuing to ask the player which paladins "pathway" they wish to go down
            yesorno = input("Do you like (type l), or dislike (type d) The Injustice Bane?: ")
            if (yesorno == "l"):
                space()
                print("They seem pleased by your answer and one says thank god your not one of them.")
                print("They explain to you that the other group is trying to kill the Injustices Bane.")
                print("Unfortunately though they have no definitive proof and so their efforts have been fruitless.")
                inputspace()
                #continuing to ask the player which paladins "pathway" they wish to go down
                yesorno = input("Do you tell them you can try and talk to him (type t), or do you ask for your first shift (type f)?: ")
                if (yesorno == "t"):
                    space()
                    print("You see a glimmer of hope spark in their eyes as they instantly direct you to the Injustice Bane's throne room.")
                    playerpos = "13"
                    input()
                elif (yesorno == "f"):
                    space()
                    print("The guards seem dissapointed by your answer.")
                    print("One of the guards tells you to come with him for your first shift as you to are together.")
                    print("You hop on your horses and go to town to perform roll call.")
                    print("You complete your first week of being a paladin")
                    playerpos = "14"
                    input()
            elif (yesorno == "d"):
                space()
                print("They seem dissapointed by your answer and quickly disperse leaving you by yourself with the other group in the locker room.")
                print("The other group approaches you and get straight to the point.")
                print("They tell you of their plans to kill the Injustices Bane and that you not liking him is justified.")
                print("They scurry off beckoning you to follow them into this secret room.")
                print("Inside the secret room is a table surrounded by enough chairs for the lot of you.")
                print("On one wall you see a plan devised to kill the Injustices Bane.")
                print("Everyone sits down at a seat and they begin to tell you their entire plan to kill the Injustices Bane and put an end to his fake justice.")
                print("They ask you for your thoughts on the plan.")
                inputspace()
                #asking the player how they want to kill the injustices bane
                yesorno = input("Do you think it should be done at breakfast (type t), or at night (type a)?: ")
                if (yesorno == "a"):
                    space()
                    print("They all seem to agree with your idea and decide to enact it tonight.")
                    playerpos = "15"
                    input()
                elif (yesorno == "t"):
                    space()
                    print("They all seem to agree with your idea and decide to enact it tommorow during morning tea.")
                    playerpos = "16"
                    input()
    #checking if the player is in the throne room and trying to snitch on the mutineers
    if (playerpos == "13"):
        print("You walk up to him and he asks you what you want.")
        inputspace()
        #asking the player how they want to try and snitch on the mutineers
        yesorno = input("Do you try and intimidate him (type i), or persuade him (type p)?: ")
        space()
        if (yesorno == "i"):
            print("You try and intimidate him and...")
            #random dice roll based off class to decide outcome
            if (intimidate == 1):
                print("The Injustices Bane seems to shrivel in his chair and your intimidation works!")
                print("He completely believes you and calls all the guards that aren't taking part in the mutiny up to the throne room.")
                print("He tells you all to ambush the people doing the mutiny.")
                print()
                print("You kill all the mutineers and are awarded a promotion from the Injustices Bane for your efforts.")
                print("The Injustices Bane makes you his right hand man in the promotion.")
                print("Congratulations on beating the game the intimidators way.")
                intimidator()
                playerpos = "6"
                achievements.append("snitch1")
            else:
                print("The Injustices Bane stands up straight in his chair and accuses you of trying to intimidate him.")
                print("He begins fighting you to prove he is stronger and cant be intimidated.")
                playerpos = "8"
                input()
        if (yesorno == "p"):
            print("You try and persuade him and...")
            #random dice roll based off class to decide outcome
            if (persuade == 1):
                print("The Injustices Bane is easily persuaded and hanging off every word you say.")
                print("He calls up all the guards that aren't taking part in the mutiny to the throne room.")
                print("He tells you all to ambush the people doing the mutiny.")
                print()
                print("You kill all the mutineers and are made the Injustice Banes chief advisor.")
                print("A ceremony is held in your honour for the promotion.")
                print("Congratulations on beating the game the persuasive way.")
                persuader()
                playerpos = "6"
                achievements.append("snitch1")
            else:
                print("The Injustices Bane accuses you of lying and heresy.")
                print("He states that the punishment for spreading false information to your ruler is death.")
                print("He chops your head off and you die.")
                caughtlying()
                playerpos = "7"
    #Checking if the player is working for the paladins
    if (playerpos == "14"):
        space()
        #checking if the player has done enough hours to be promoted
        if (workhours > 300):
            print("You have been rewarded for your efforts to the paladins and will now undergo promotion to general.")
            print("A ceremony is held in your honor.")
            print("You won the office workers way.")
            promotion()
            playerpos = "6"
            achievements.append("promotion1")
        print("After completing a week of being a paladin one of the office ladies at the castle asks you how many hours you wish to work for the next week.")
        inputspace()
        #asking the player how many hours they wish to work
        workhours = float(input("Type any number of hours greater than 0 to work for this week (can be a decimal): "))
        totalhours = totalhours + workhours
        space()
        #checking how well the players work hours align with the paladins work hours
        if (workhours > 168):
            print("In an outburst she says: Are you stupid there aren't even that many hours in a week!")
            print("The Injustices Bane will not have people this stupid working for him as a paladin.")
            print("I sentence you to execution for being stupid whilst working as a paladin.")
            print("Two guards grab you from behind and apprehend you.")
            print("Your taken to the throne room where the Injustices Bane sits there and waits.")
            print("He walks over to you and chops your head off.")
            print("You died")
            playerpos = "7"
            stupidity()
        elif (169 > workhours > 128):
            print("The office lady seems perplexed by your answer and says:")
            print("Look if you don't want sleep this week that's up to you but you'll be regretful in a week.")
            if (overwork > 2):
                print("In the middle of the week you start feeling really light headed due to lack of sleep.")
                print("You collapse to the floor and don't wake up.")
                print("Your long hours and lack of sleep cause you to die of exhaustion.")
                exhaustion()
                playerpos = "7"
                overwork = 0
            else:
                overwork = overwork + 1
        elif (129 > workhours > 80):
            print("Seemingly happy she says: You really love work huh, well good luck with your busy week.")
            print("Your efforts to the paladins of justice this week have been noticed and many people have been commending you.")
        elif (81 > workours > 39):
            print("She seems dissapointed by your answer and says:")
            print("Another person just wanting to be average, well have fun.")
        elif (workhours < 40):
            print("She seems upset by your answer before saying:")
            print("You know the Injustices Bane is not going to be very happy with you putting in such little hours.")
            if (underwork > 0):
                print("At the end of the week you are called to the throne room by the Injustices Bane.")
                print("He tells you that you are going to be demoted for putting in such little effort into our cause.")
                print("Before you can speak a guard from behind chops your head off.")
                print("You died.")
                demotion()
                playerpos = "7"
            else:
                underwork = underwork + 1
    #checking if the player is inside the dorm planning how they will kill the injustices bane at night
    if (playerpos == "15"):
        space()
        print("You all stay up until midnight in your dorms waiting for the right time to strike.")
        print("Whilst you wait you all discuss plans to make sure everyone knows what they are doing.")
        print("What is your plan?")
        inputspace()
        #asking the player questions to decide how they end up killing the Injustices Bane
        stealthdeath = input("Do you wish to suffocate him (type s), kill him via blood loss (type b), or by chopping him up (type c): ")
        inputspace()
        distraction = input("Do you want to create a large distraction (type l), or be as sneaky as possible (type s): ")
        inputspace()
        if (distraction == "l"):
            print("What kind of distraction would you like to use?")
            inputspace()
            ruccus = input("Do you want to start a fire in the kitchen (type f), sound the invasion alarm (type i), release the horses (type h), or just scream (type s): ")
        elif (distraction == "s"):
            print("How do you want to sneak into the Injustice Banes bedroom?")
            inputspace()
            sneaking = input("Do you want to climb in through the window (type w), sneak down the hallway to his bedroom (type h), or use the secret passage in the Injustice Bane closet (type s): ")
        inputspace()
        print("What mask do you want to use to disguise yourself whilst performing the operation?")
        inputspace()
        masks = input("A bunny mask (type b), a horse mask (type h), use your guard helmet (type g), an orangutan mask (type o): ")
        print("Your plan is chosen to be enacted.")
        print("As the suspense heightens and the sweat of anticipation pours down your skin the time ticks to midnight and the fun begins.")
        space()
        #printing the way they killed the injustices bane by checking what answers they picked
        if (masks == "b"):
            print("You all put on your bunny masks and leave the dorm")
        elif (masks == "h"):
            print("You all put on your horse masks and leave the dorm")
        elif (masks == "g"):
            print("You all get dressed in your guard uniform and leave the dorm")
        elif (masks == "o"):
            print("You all put on your orangutan masks and leave the dorm")
        if (distraction == "l"):
            if (ruccus == "f"):
                print("The other paladins go to start a fire in the kitchen leaving you by yourself to commit the crime.")
            elif (ruccus == "i"):
                print("The other paladins go to sound the alarm for an invasion leaving you by yourself to commit the crime.")
            elif (ruccus == "h"):
                print("The other paladins go to open all the horse cages and let the horse free leaving you by yourself to commit the crime.")
            elif (ruccus == "s"):
                print("The other paladins go to the courtyard to begin their screaming leaving you by yourself to commit the crime.")
        if (distraction == "s"):
            if (sneaking == "w"):
                print("The other paladins lead you into the courtyard to the wall where his window is and you start climbing.")
                print("You reach his window and take a peek inside, sleeping inside is the Injustices Bane.")
                print("You begin slowly opening the window and creep inside.")
            elif (sneaking == "h"):
                print("The other paladins lead you to the hallway and keep watch for you so that you aren't caught.")
                print("You begin creeping down the hallway and every creek of the floor boards leaves you worried that he might wake up.")
                print("You get to his room and creek the door open taking a peek, inside is the Injustices Bane fast asleep.")
                print("You enter the room.")
            elif (sneaking == "s"):
                print("The other paladins lead you to the throne room.")
                print("They take you behind the throne where a hidden hatch on the floor is.")
                print("You open the hatch and hop in leaving the rest of the paladins circled around the hatch to keep guard.")
                print("The passage is windy and you have to duck the whole way through it.")
                print("You end up in his walk in closet and peek through the cracks of the closet doors to see the Injustice Bane sleeping.")
                print("You come out of the closet.")
        if (stealthdeath == "s"):
            print("You creep over to his bed and grab one of the pillows he isn't using.")
            print("You shove the pillow on his face and suffocate him.")
            print("He kicks his legs trying to fight it but after a couple more seconds he flops lifeless.")
            print("You hold it on his face for a minute after for good measure.")
        elif (stealthdeath == "b"):
            print("You creep over to his bed.")
            print("You pull out your knife and cut holes in the Injustice Banes Arteries.")
            print("He tries to scream but is too weak to do so.")
            print("He bleeds out and dies as you stand there and watch.")
        elif (stealthdeath == "c"):
            print("You creep over to his bed and pull out a sword.")
            print("You tap him on the shoulder to wake him up and as he opens his eyes you chop his head off in one clean slice.")
            print("His head rolls off the bed and you use his blanket to clean your sword.")
        print("You leave the room the way you came and alert the paladins of your success.")
        print("Congratulations you won the mutineers way.")
        mutiny()
        achievements.append("mutiny1")
        playerpos = "6"
    #checking if the player is in the dorm planning how they will kill the injustices bane during the feast
    if (playerpos == "16"):
        print("You all stay up all night planning out how the events of the day will go.")
        print("Your input is required for the plans to help make them.")
        print("Which item do you wish to poison during morning tea?")
        inputspace()
        foodpoison = input("His tea (type t), his bread (type b), or his bacon (type h): ")
        inputspace()
        timing = input("Do you wish to spike the item during cooking (type c), or during the feast (type f): ")
        if (timing == "c"):
            print("What kitchen distraction do you want to use so you can sneak the poison into the food?")
            inputspace()
            kitchen = input("Do you want to: Set the fire alarm off (type f), Bump a massive soup pot onto the ground (type s), or unleash a rat into the kitchen (type r): ")
        elif (timing == "f"):
            print("What distraction are you going to use to spike his food.")
            inputspace()
            feast = input("Do you want to: Set the fire alarm off type f, trip and fall onto the dining table type t, or spill tea on the Injustices Bane type i?")
        print("The other paladins decide your idea is brilliant and go along with it.")
        print("You all get some good sleep and wake up in time for the feast.")
        print("The feast starts so let the fun begin.")
        #printing the ending based off the options you picked to kill him
        if (timing == "c"):
            print("You go into the kitchen and get ready for your distraction.")
            if (kitchen == "f"):
                print("you calmly walk over to the fire alarm before pulling it and quickly dispersing yourself among the crowd so no one knows it was you.")
            elif (kitchen == "s"):
                print("You carefully weave your way between the cooking aisles before accidentally bumping a massive soup pot.")
                print("You quickly disperse among the crowd so no one knows who did it.")
            elif (kitchen == "r"):
                print("You bring a rat cage into the kitchen before unleashing it and leaving the kitchen.")
                print("After a minute one of the chefs notices it and screams there head off, your queue to go back in and spike the item.")
        elif (timing == "f"):
            print("You take a seat at one of the long dining tables in the feast hall and begin eating.")
            if (feast == "f"):
                print("You calmly hop up in the middle of the feast and walk over to the fire alarm.")
                print("You pull the fire alarm and calmly disperse yourself amongs the crowd of chaos so no one knows you did it.")
            elif (feast == "t"):
                print("In the middle of the feast you get up and start walking towards the toilet down the aisle of seats.")
                print("Like you planned one of the guards sticks their foot out behind themself so you can trip over it and cause a distraction.")
                print("You trip and fall on the table sliding all the way down to the other end.")
                print("After that everyone starts getting at eachothers throats and a brawl is started in the dining hall.")
            elif (feast == "i"):
                print("In the middle of the feast you get up and begin walking over towards the injustice bane.")
                print("Like you planned a guard sticks their foot out into the aisle and you trip with a glass in hand spilling it over the injustice bane.")
                print("After that everyone gets at eachothers throats and start attacking eachother.")
        if (foodpoison == "t"):
            print("Amongst the chaos of the distraction you walk over to his tea and drop the poison in it.")
        elif (foodpoison == "b"):
            print("Amongst the chaos of the distraction you walk over to his bread and drop the poison in it.")
        elif (foodpoison == "h"):
            print("Amongst the chaos of the distraction you walk over to his bacon and drop the poison in it.")
        print("Once the chaos dies down and everyone is sitted you start eating breakfast.")
        print("After a moment or two you see the Injustice Bane's Mouth start to froth up and massive amounts of bubbles are coming out.")
        print("A moment or two later he dies and you and all the other guards in on it give each other a silenet look of celebration.")
        print("Congratulations on beating the game the mutineers way.")
        achievements.append("mutiny1")
        mutiny()
        playerpos = "6"
#end of code
