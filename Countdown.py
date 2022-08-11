#Veeru Senthil
#Timer Fixed

#Import time class
import time

#Function converts total seconds to into 2 variables: 1 storing number of minutes and the other with seconds
#fe: 68 seconds would be 1 minute and 8 secs
#Function then formats timers then initiates timer to count down

def countdown(seconds):
    if seconds >= 60:
        minutes = seconds // 60
        secs = seconds % 60
    else: 
        minutes = 0
        secs = seconds 
    
    #Formats the timer with two created variables extracted from total seconds
    timer = '{:02d}:{:02d}'.format(minutes, secs)     
    
    #Iterates through total seconds to go down until the end of the timer

    for x in range(seconds):

    #Learned this super useful print override function on google
        print(timer, end = "\r")
    #Makes sure the timer actually waits a second before decrimenting
        time.sleep(1)
        seconds -= 1

    print("BEEP BEEP BEEP")

#Excuting code

clock = int(input('How long do you want the timer to be in seconds?'))

countdown(clock)