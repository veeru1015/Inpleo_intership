#Veeru Senthil
#Countdown

#Import time class
import time

#Function converts total seconds into 2 variables: 1 storing number of minutes and the other with remaining seconds
#fe: 68 seconds would be 1 minute and 8 secs
#Function then formats the timer to initiate countdown

def countdown(seconds):
    
    #Iterates through total seconds til the end of the timer
    for x in range(seconds):

        minutes = seconds // 60
        secs = seconds % 60
    
    #Formats the timer with the two variables extracted from total seconds
        timer = '{:02d}:{:02d}'.format(minutes, secs)     
    
    #Learned this super useful print override function on google
        print(timer, end = "\r")
    #Makes sure the timer actually waits a second before decrimenting
        time.sleep(1)
        seconds -= 1

    print("BEEP BEEP BEEP")

#Excuting code

#User input
sec_total = int(input('How long do you want the timer to be in seconds?'))

# Running function with user input
countdown(sec_total)