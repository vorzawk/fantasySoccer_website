#!/usr/bin/env python3

''' Split the input relation to form the attack, defence, passing, ball control relations '''
import csv
# using with so that the file is automaticall closed
with open('FullData.csv', newline='') as csvFile:
    # The reader object will iterate over the lines in the csv file
    csvReader = csv.reader(csvFile)
    # The next function returns the line pointed to by the reader object as a list of all the fields in the line
    # The first line is the list of attribute names, store this in list_attr
    list_attr = next(csvReader)
    # Create a list of dictionaries listing the attributes and their values for each player
    players = []
    for row in csvReader:
        i = 0
        dict_attrVals = {}
        for attr in list_attr:
            dict_attrVals[attr] = row[i]
            i = i + 1
        players.append(dict_attrVals)

general_attr = ['Name','Nationality','Club','Position']
attack_attr = ['Name', 'Club','Jumping','Heading','Shot_Power','Finishing','Long_Shots','Curve','Acceleration', 'Speed']
ballSkills_attr = ['Name', 'Club','Ball_Control','Dribbling','Balance']
passing_attr = ['Name','Club','Short_Pass','Crossing','Long_Pass']
defense_attr =['Name','Club','Marking','Sliding_Tackle','Standing_Tackle','Interceptions','Strength']
goalKeeping_attr = ['Name','Club','Positioning','Diving','Kicking','Handling','Reflexes']
general_data = [general_attr]
attack_data = [attack_attr]
ballSkills_data = [ballSkills_attr]
passing_data = [passing_attr]
defense_data = [defense_attr]
goalKeeping_data = [goalKeeping_attr]
# players is a list of dictionaries each corresponding to a player, read the required values into a list of lists 
# which can later be used to write into the appropriate csv files for the relations.
for player in players:
    # For each player, look up the value of the required attribute and store it in the appropriate list
    generalInfo_player = []
    for attr in general_attr:
        if attr == 'Position':
            # Some players play in multiple positions, however for the purpose of fantasy soccer, it is sufficient to 
            # classify players as Forwards, Midfielders, Defenders or Goal Keepers.
            (opt1,sep,opt2) = player['Position'].partition('/')
            if opt1 == 'ST' or opt2 == 'ST':
                player['Position'] = 'ST'
            else:
                player['Position'] = opt1
            if player['Position'] == 'ST' or player['Position'] == 'LS' or player['Position'] == 'CF':
                player['Position'] = 'Forward'
            elif player['Position'] == 'CM' or player['Position'] == 'RM' or player['Position'] == 'LM' \
                    or player['Position'] == 'CAM' or player['Position'] == 'CDM' or player['Position'] == 'RWB' \
                    or player['Position'] == 'LWB' or player['Position'] == 'LW' or player['Position'] == 'RW':
                player['Position'] = 'Midfielder'
            elif player['Position'] == 'CB' or player['Position'] == 'RB' \
                    or player['Position'] == 'LB' or player['Position'] == 'RWB' \
                    or player['Position'] == 'LWB':
                player['Position'] = 'Defender'
            elif player['Position'] == 'GK':
                player['Position'] = 'Goal Keeper'
            else:
                print("Error: unknown position \"{}\"".format(player['Position']))
        generalInfo_player.append(player[attr])
        # Store the list of relevant attributes in the list to be used later to write to the csv file.
    general_data.append(generalInfo_player)

    attack_player = []
    for attr in attack_attr:
        attack_player.append(player[attr])
    attack_data.append(attack_player)

    ballSkills_player = []
    for attr in ballSkills_attr:
        ballSkills_player.append(player[attr])
    ballSkills_data.append(ballSkills_player)

    passing_player = []
    for attr in passing_attr:
        passing_player.append(player[attr])
    passing_data.append(passing_player)

    defence_player = []
    for attr in defense_attr:
        defence_player.append(player[attr])
    defense_data.append(defence_player)

    goalKeeping_player = []
    for attr in goalKeeping_attr:
        if attr != 'Name' and attr != 'Club':
            attr = 'GK_'+attr
        goalKeeping_player.append(player[attr])
    goalKeeping_data.append(goalKeeping_player)

with open('general_info.csv', 'w') as csvFile:
    csvWriter = csv.writer(csvFile)
    # *_data is a list of lists, each list corresponds to one line of the csv file
    for line in general_data:
        csvWriter.writerow(line)

with open('attack_all.csv', 'w') as csvFile:
    csvWriter = csv.writer(csvFile)
    # *_data is a list of lists, each list corresponds to one line of the csv file
    for line in attack_data:
        csvWriter.writerow(line)

with open('ball_skills_all.csv', 'w') as csvFile:
    csvWriter = csv.writer(csvFile)
    # *_data is a list of lists, each list corresponds to one line of the csv file
    for line in ballSkills_data:
        csvWriter.writerow(line)

with open('passing_all.csv', 'w') as csvFile:
    csvWriter = csv.writer(csvFile)
    # *_data is a list of lists, each list corresponds to one line of the csv file
    for line in passing_data:
        csvWriter.writerow(line)

with open('defence_all.csv', 'w') as csvFile:
    csvWriter = csv.writer(csvFile)
    # *_data is a list of lists, each list corresponds to one line of the csv file
    for line in defense_data:
        csvWriter.writerow(line)

with open('goal_keeping_all.csv', 'w') as csvFile:
    csvWriter = csv.writer(csvFile)
    # *_data is a list of lists, each list corresponds to one line of the csv file
    for line in goalKeeping_data:
        csvWriter.writerow(line)
