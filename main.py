
#DDD
#19/03/16

#Program for text based game

from tkinter import *
from tkinter import messagebox
import datetime
import os
pathname = "usernames.txt"
currentMap = "level 1.txt"
window=Tk()
window.geometry("400x200")
window.title("DDD Login")
global playerLocation
playerLocation = [1,1]
playerLocationTemp = [1,1]
#=======================Language========

MoveForward = "Moved Forward"
MoveBack = "Moved Back"
MoveLeft = "Moved Left"
MoveRight = "Moved Right"


#=======================ARRAYS==========


currentLevelArray=[]
validCommandArray=["Forward","Back","Right","Left","Log"]
logArray=[]



#=======================Canvas'==========

#========Startup Canvas===


openCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
openCanvas.pack(expand=True)

Label(openCanvas,text="Username").grid(row=0,column=0)

userNameEntry=Entry(openCanvas)
userNameEntry.grid(row=0,column=1)



#================================================================START OF FUNCTIONS========================    

def getMapLocation(currentMap,x,y):
    lines = list(map(str.split, open(currentMap)))
    return lines[y][x]

def askMessage(pre,message):
    try:
        messagebox.showinfo(pre,message)
    except:
        print(messsage)

def askError(pre,message):
    try:
        messagebox.showerror(pre,message)
    except:
        print(message)

def clearScreen():
    os.system("cls")
        
#Function that checks the user's credentials in database
def checkCredentials(event):

    #Gets the credentials from Entry
    userNameString=userNameEntry.get()

    content=getReadlines("usernames.txt")
    userNameArray=[]
    if content != None:
        for line in content:
            userNameArray.append(line)
        

    #If the userName is valid do this
    if userNameString in userNameArray:
        askMessage("Valid","User name valid")

        window.destroy()
        
        return userNameString

    #If the username is not recognised do this
    else:
        askError("Invalid","Unknown user")
        addToLog("Unknown User")
        if messagebox.askyesno("Unknown user.", "Create new user?"):
            with open(pathname, "a") as f:
                addToLog("Created new user")
                f.write("\n")
                f.write(userNameString)
                f.close()
#Function to get array from info from .txt file  
def getReadlines(pathname):
    try:
        file=open(pathname,"r")
    except:
        askError("Not Found","File Not Found")
        addToLog("File Not Found")
    else:
        content=file.readlines()
        newContent=[]
        for line in content:
            line=line.rstrip()
            newContent.append(line)
            
        file.close()
        return newContent
class battle:
    def boss1(sword = 0):
        print("Not yet implemented")

#Function to load a txt file into the current level array
def importLevel(fileName):


    #Read in line by line
    global currentLevelArray
    content=getReadlines(fileName)

    #Validation
    if content != None:
        currentLevelArray=[]
        for line in content:
            currentLevelArray.append(line)

    addToLog("Map loaded")
        
#=============Initital setup funtions=========

#This function runs when enter key is pressed.
def checkUser(playerLocation):
    userName=checkCredentials("")

    #Only if userName is valid will the game launch
    if userName != None:
        addToLog("Starting new game")
        startNewGame(userName, playerLocation)
        

def viewLog():
    for item in logArray:
        print(item)
def printAndLog(data):
    print(data)
    addToLog(data)

def addToLog(data):
    temp=""
    currentTime=str(datetime.datetime.now().time())
    temp+=currentTime
    temp+="  "
    temp+=data
    logArray.append(temp)
#================================================================END OF FUNCTIONS========================    


#============================ACTUAL GAME FUNCTION=============
"""
Start new game function
In future updates take argument to determine which level to load
"""



def startNewGame(playername, playerLocation):
    
    
    hp = 80

    #Initialises a class for the player

    #While loop that runs until the player is dead
    while hp > 0:
        print(" You are at ({0}, {1}), and facing -->".format(playerLocation[0], playerLocation[1]))
        lines = list(map(str.split, open(currentMap)))
        for y in range(0, len(lines)):
            for x in range(0, len(lines[y])):
                if(x == playerLocation[0] and y == playerLocation[1]):
                    print("@", end='')
                else:
                    print(lines[y][x], end='')
            print('')

            
        print("\n"*21)
        cmd = input(">")
        clearScreen()
        #Converts input into capital
        cmd=cmd.capitalize()

        #Indexes The array to find a mathcing function
        
        if cmd in ["Forward", "E", "F"]:
            playerLocation = move(playerLocation, 1, 0)
        elif cmd in ["Back", "W", "B"]:
            playerLocation = move(playerLocation, -1, 0)
        elif cmd == ["Left", "N", "L"]:
            playerLocation = move(playerLocation, 0, -1)
        elif cmd in ["Right", "S", "R"]:
            playerLocation = move(playerLocation, 0, 1)
        elif cmd == "Log":
            viewLog()
        else:
            print("Invalid command")
            addToLog("User tried an invalid command")
        

        
#=============Initital setup funtions=========



#====================================================================CLASSES==========================

def move(playerLocation, deltaX, deltaY):
    if getMapLocation(currentMap, playerLocation[0] + deltaX, playerLocation[1] + deltaY) in ["#", "0"]:
        print("You can't go that way")
        addToLog("Harry potter tried to run himself into a wall but dobby had closed Platform 9 3/4 ")
        return playerLocation

    playerLocation[0] += deltaX
    playerLocation[1] += deltaY
    
    if getMapLocation(currentMap, playerLocation[0], playerLocation[1]) == "B":
        print("The boss lives there. You have awoken him, therefore it is your task to slay him.")
        addToLog("Awoken Boss")
        battle.boss1()

    printAndLog("New location: " + str(playerLocation[0]) + ", " + str(playerLocation[1]))
    return playerLocation
        
#=============RETURN FUNCTIONS=======
importLevel("level 1.txt")
    

#=============BINDINGS============
userNameEntry.bind("<Return>",lambda event: checkUser(playerLocation))

window.mainloop()
