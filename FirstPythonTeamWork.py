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

def BitCoin_To_USD(btc):# A simple Function Which receives int value
    amount = btc * 5680 # Mathematical action
    print("Your Bitcoin worth : ",amount , "$")# Print the The result

# To use Just Call the Function Name and Give The Amount in BTC 

BitCoin_To_USD(5)


# Program Number Two By KAS.P =================================================>

#First Program By Weiss.S ,./--\.,  

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