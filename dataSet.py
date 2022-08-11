# Veeru K. Senthil 


#This code uses pandas library to help give information and insight regarding dataset for fifa 22
#Fifa is a popular soccer/football video game
# I am creating simple code to display data from the dataset 

import pandas as pd

fifa = pd.read_csv('fifa22_data.csv')

#print('hi')

#print(fifa.head)

#This dataset is pretty messed up

# Now we are filtering for Manchester United's (my fav team) players
man_united = fifa[(fifa['club_name'] == 'Manchester United')]
print('Manchester United currently has ' +  str(len(man_united)) + ' players on the team')

# Printing Roster

unitedInfo = man_united
players = unitedInfo['short_name']

unitedInfo.to_csv('ManUnited.csv')
# creating new Man U csv
print()
print()
print()
print()
ManU = pd.read_csv('ManUnited.csv')

# Printing the starting man U striker on fifa
Strikers = ManU[(ManU['club_position'] == 'ST')].reset_index()
StrikersName = Strikers['short_name']
print('The starting striker (st) on Manchester United is ' + StrikersName)
print()
print()

#printing the names of the subs on fifa in Man U
Subs = ManU[(ManU['club_position'] == 'SUB')].reset_index()
SubName = Subs['short_name']
print('The subs on Manchester United are ' + SubName)
print()
print()


#printing the names of the Stars (Players above an overall of 85) in Man U

Stars = ManU[(ManU['overall']  > 85)].reset_index()
StarsName = Stars['short_name']
print('The star players on Man United on fifa (Overall above 85) are: ' + str(StarsName))

print()
print()

#printing the names of the Rising Stars (Potential over 86 and age less than 22) in Man U
rising_stars = ManU[(ManU['potential']  > 86) & (ManU['age'] < 22)].reset_index()
print("The rising stars on United are " + rising_stars['short_name'])

