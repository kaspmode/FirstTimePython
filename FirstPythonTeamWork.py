
# Sup Let's start learning Python!!!

#First Progrom By KAS.P =================================================>

#This is the MagicNumbers Finder Using a LOOP

magicNumber = 26 # 26 is the Magic number

#This loop going through 101 Numbers Once she finds the Magic number,It will print the number on the screen

for n in range(101):
    if n is magicNumber:
        print("This Magic Number Is :" , n )
        print("") #down a line in console 
        

#First Program By KAS.P =================================================>

#First Program By Weiss.S ,./--\.,  <-- this is ascii batman 

#This program generate a Lorem Ipsum paragraph from a random number for characters (0 to 651)
import random #random.randint wont work without it


def WeissRandLorem():#define functin name
    ipsumStrNum = random.randint(1,651)#this will hold the random int
    #this row is the lorem ipsum paragraph
    ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ut nisi consectetur, accumsan leo vel, efficitur risus. Aenean sit amet nisi nec tortor blandit scelerisque. Nulla scelerisque turpis vel leo hendrerit fringilla. Nullam tristique sem ac mauris sodales dictum. Suspendisse arcu metus, hendrerit pretium cursus non, eleifend at libero. Donec sed ullamcorper justo. Interdum et malesuada fames ac ante ipsum primis in faucibus. Maecenas ut ante velit. Nulla quis leo in lorem pretium ultrices. Quisque luctus porta metus eu mattis. Proin dictum tellus risus, vitae sagittis erat condimentum eu. Nullam posuere est nec justo dapibus consequat."
    ipsList = list(ipsum)#the list command break apart the string to a list a of characters ['L', 'o', ..etc]
    new = ''.join(ipsList[0:ipsumStrNum:1])
    #joining the list back together using brackets [x,y,z]
    #where x is the place to start from, y is the place to stop, z is the stepper
    #z = 1 meanning it will go one iter at a time
    print (new)
    print("")#down a line in console 

WeissRandLorem()#Calling the function

#(c)For personal use only (lol, rush B)  = hahaha LOL... 


# Program Number Two By KAS.P ===> By the way My D9 ascii Just run over your ascii batman ...

#                O
#        /~~~|#|]|=\|---\__
#      |-=_____________  |\\ ,              
#     I|_/,-.-.-.-.-,-.\_|='(   ,./--\.,            
#        ( o )( o )( o )     \              
#         `-'-'-'-'-`-'



# Program Name : BitCoin To Usd Calculator
#def BitCoin_To_USD(btc):# A simple Function Which receives int value
#    amount = btc * 5680 # Mathematical action
#    print("Your Bitcoin worth : ",amount , "$")# Print the The result
# FIXED - THE RIGHT WAY TO DO THIS
convRate = 5680
def BitCoin_To_USD(btc:int) -> int:
    """Return the value of USD from BTC"""
    return btc * convRate

# To use Just Call the Function Name and Give The Amount in BTC 

btcToUsd = BitCoin_To_USD(1)
print ("Your bitcoin worth is : ",btcToUsd, "$")
help(BitCoin_To_USD)## this will show the function arguments and return data

# Program Number Two By KAS.P =================================================>

#Second Program By Weiss.S ,./--\.,  

# \_\_    _/_/
#     \__/
#     (oo)\_______
#     (__)\       )\/\
#         ||-----||
#         ||     ||
#PLEASE DO NOT FEED THE DEER

#a simple program that get a sentence, then it run a loop looking for letters that match the ones in the []list
word = input("Give me a sentence and i will let you know how which and how many vowels it has :")
vowels =['a', 'e', 'i', 'o', 'u']#a simple list, nothing special
found = {}#this is called dictionary, or in short dict (how pythong programmers call it
          #it hols sets of keys and values like: color : green, size : big  (etc)
          #you can think of it as endless rows with 2 coloums
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)#set default is actually a command that replace this if sentence:
                        #if letter in found: found[letter] +=1 else found[letter] = 0.
                        #if we wont use it we'll get an error cause were trying to enter value to a missing key
        found[letter] += 1## too bad python doesnt have the ++ operator, we have to +=
print("")
for k, v in sorted(found.items()):#we use the function sorted which sort a dictionary data type, otherwise
                                #we wont have any order
    print (k, 'was found', v, 'times.')
    print("")



# Program Number Third By KAS.P =================================================>

#                           
#        .::::::::::.                         .::::::::::.
#      .::::''''''::::.                      .::::''''''::::.
#    .:::'          `::::....          ....::::'          `:::.
#   .::'             `:::::::|        |:::::::'             `::.
#  .::|               |::::::|_ ___ __|::::::|               |::.
#  `--'               |::::::|_()__()_|::::::|               `--'
#   :::               |::-o::|        |::o-::|               :::
#   `::.             .|::::::|        |::::::|.             .::'
#    `:::.          .::\-----'        `-----/::.          .:::'
#      `::::......::::'                      `::::......::::'
#        `::::::::::'                          `::::::::::'
#
# You're Under a Rest For DEER Pornagrfy

import random # you know this one
import urllib.request # module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world 

#This A cool Program that can Download Any image from the Internet! Using the link of the image

def download_web_imgae(url): # name of the Function
    name = random.randrange(1,100) # give a Random Number for the image name
    fulll_name = str(name) + ".jpg" # Take the Number and And converts it to a string
    urllib.request.urlretrieve(url,fulll_name)# this is the Download Function , you need to give it two parameters for it to work
    #First one : Url from the site your downloading the image , The second is the name of the file That you want to give the image

#Just Insert Any image Link you want (Type Jpg) , The image will be downloaded to the Program Directory
download_web_imgae("https://images.homedepot-static.com/productImages/5713319d-93ec-4bee-ac0f-5899086e2666/svn/gilmour-garden-hoses-1609728035-64_1000.jpg")

# Program Number Third By KAS.P =================================================>

#Program number three by Weiss.S ================================================>

#   _/\____________________________,,,'
#   '               ------------------fi
#    \/__/ / / / ____|----------------fi
#   /___/ / / / __---------'''''''''
#   \_ )-------)  =     ---,,
#     / /      /      ----,,
#    / / O    / --    .
#   / /___   / __--((__/
#  / / ---  //
# /  --__  /
# \@______//
#fUCK DA POL1CE


def searchForLetters(phrase:str, letters:str) -> set:
    """Function will return a set of letters which is common to the phrase and the letters given"""
    return set(letters).intersection(set(phrase))
#set command turn create a set object out of string,
#intersection command return common values between two data structure

print ('I will TRY to find letters which present in your first AND second sentences')
input1 = input ('Give me the First sentence: ')
input2 = input ('Give me the Second sentence: ')
result = searchForLetters(input1, input2)
print (result)

#Program number three by Weiss.S ================================================>


# Program Number Four By KAS.P =================================================>
#    _..._
#     .'     '.
#    /`\     /`\    |\
#   (__|     |__)|\  \\  /|
#   (     "     ) \\ || //
#    \         /   \\||//
#     \   _   /  |\|`  /
#      '.___.'   \____/
#       (___)    (___)
#     /`     `\  / /
#    |         \/ /
#    | |     |\  /
#    | |     | "`
#    | |     |
#    | |     |
#    |_|_____|
#   (___)_____)
#   /    \   |
#  /   |\|   |
# //||\\  Y  |
#|| || \\ |  |
#|/ \\ |\||  |
#    \||__|__|
#     (___|___)
#     /   A   \
#    /   / \   \
#   \___/   \___/
#
#I come in peace


#How to Use Default Values for Arguments 

def OLDgetGender(sex='Unknown'): # simple Function to test Default Values for Arguments (Using the ='Set Default Values')
    if sex is 'm':
        sex = "Male"
        elif sex is 'f':
        sex = "Feamle"
        print(sex)
        
#Checking all possible scenarios
OLDgetGender('m')
OLDgetGender('f')
OLDgetGender()

# Program Number Four By KAS.P =================================================>
# Program number five by Weiss.S + fix to program 4 ============================>

#                   /|
#                  / |,
#             ,,,  o    \_
#               "(    o   /
#                 | \.
#                 |      \
#                 |';    )  )
#                 W W F )___/
#  MEWO...MEWO

#Your elif was inside the if statement, another thing to keep in mind, is that a function should do as less as possible.
#Meanning it should probably never print anything, the main code should print stuff based on functions return values
#So i added another code getGender2 which does exactly that, we invoke it and we assign the funtion return value to a variable
#then we can print whatever we want.

def getGender(sex='Unknown'): # simple Function to test Default Values for Arguments (Using the ='Set Default Values')
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Feamle"
    print(sex)
        
#Checking all possible scenarios
getGender('m')
getGender('f')
getGender()

def getGender2(sex='Unknown'):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Feamle"
    return sex
        
test1 = getGender2('m')
test2 = getGender2('f')
test3 = getGender2()

print ("Using argument 'm' gives us: ",test1)
print ("Using argument 'f' gives us: ",test2)
print ("Using no argument gives us: ",test3)
##################################################
#Now, FOR THE MAIN EVENT OF THE EVENING..... MY... C0DE!

import random

#make a list of 20 random numbers from 0 to 100
numbers = []
for i in range (0,20):
    numbers.append (random.randint(0,100))#Simple loop to append random number from 0 to 100 to the list
numbers.sort(key=int)#sort the list from small the big
print ("This is the generated random list : ")
print (numbers)
keyNumber= 65
print ("This code will generate a new list made from the original list \n Appending only numbers smaller than: ",keyNumber)
#I've added a BUG ;) the BUG will make this work but wont handle the list like we want when a special case occure
#can you FIX IT?!?!?!
def newListMaker (numbers:list, keyNumber:int) -> list:
    #WILL ONLY WORK WITH A SORTED LIST! #WILL ONLY WORK WITH LIST OF 20 ITEMS! return a new list with numbers smaller than argument number
    newList = []
    flag = True#as long as flag is true, the loop will run, we first set it to true so it runs at least once
    i = 0#counter, based on list with 20 items
    while flag and i < 20:
        flag = numbers[i] < keyNumber#if the list item is smaller than the keynumber we want flag to stay true so the while loop will
                                    #run again, when we get to an item which is bigger than our number we want to stop the loop
                                    #we are basing that fact given the list is ordered, the flag will turn false and this will be
                                    #the last time the loop will run, but this time there will be another value eneter into the new list
                                    #which is bigger than our keynumber, so we need to pop him out.
        newList.append (numbers[i])
        i += 1
    newList.pop()
    return newList
            
mylist = newListMaker (numbers, keyNumber)
print (mylist)
#ask user for input, integer between 0 and 100
#create a new list with numbers from the first list who are less than the user input
#print the list



# Program number five by Weiss.S + fix to program 4 ============================>








