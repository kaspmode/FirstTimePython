# Sup Let's start learning Python!!!

#First Progrom By KAS.P =================================================>

#This is the MagicNumbers Finder Using a LOOP

magicNumber = 26 # 26 is the Magic number

#This loop going through 101 Numbers Once she finds the Magic number,It will print the number on the screen

for n in range(101):
    if n is magicNumber:
        print("This Magic Number Is :" , n )
        print("") #down a line in console 
        

#First Progrom By KAS.P =================================================>

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


# Progrom Number Two By KAS.P ===> By the way My D9 ascii Just run over your ascii batman ...

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


# Progrom Number Two By KAS.P =================================================>  


