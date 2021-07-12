import time
import random
import math
import datetime
import baseballNames as names

innings = 0

score1 = 0
score2 = 0
pitches1 = 0
pitches2 = 0
hits1 = 0
hits2 = 0
so1 = 0
so2 = 0
walks1 = 0
walks2 = 0
batter1 = 0
batter2 = 0

bases = ["NA", "NA", "NA"]

def createTeam():
    team = []
    for x in range(9):
        playerName = random.choice(names.first_names) + " " + random.choice(names.last_names)
        team.append(playerName)
    return team

def assignPositions():
    positions = []
    positionsRef = names.positions[:]
    
    for x in range(9):
        randomPos = positionsRef.pop(random.randint(0,len(positionsRef)-1))
        positions.append(randomPos)
    return positions

def printRoster(team, positions):
    teamCopy = team[:]
    for x in range(9):
        if(len(team[x]) <= 13 ):
            while(len(teamCopy[x]) <= 13):
                teamCopy[x] = teamCopy[x] + " "
    for x in range(9):
        print("Player %s: " % (x + 1) + teamCopy[x] + "\t%s" % (positions[x]))

def printScore():
    global innings
    global score1
    global score2
    global hits1
    global hits2
    global so1
    global so2
    global walks1
    global walks2
    global pitches1
    global pitches2

    if(innings % 2 == 0):
        print("\n---Top of Inning %s---" % (int(innings / 2) + 1))
    else:
        print("\n---Bottom of Inning %s---" % (int(innings / 2) + 1))
    print("Team 1 | %sR | %sH | %sW | %sSO | %sPitches\n" % (score1, hits1, walks1, so1, pitches1))
    print("Team 2 | %sR | %sH | %sW | %sSO | %sPitches\n" % (score2, hits2, walks2, so2, pitches2))

def hit(player, result):
    global bases
    global innings
    global score1
    global score2
    global hits1
    global hits2
    copy = bases[:]

    if(innings % 2 == 0):
        team = 1
        if(result != "BB"):
            hits1 += 1
    else:
        team = 2
        if(result != "BB"):
            hits2 += 1

    if(result == "BB"):
        bases[0] = player
        if(copy[0] != "NA"):
            bases[1] = copy[0]
            if(copy[1] != "NA"):
                bases[2] = copy[1]
                if(copy[2] != "NA"):
                    bases[2]
                    if(team == 1):
                        score1 += 1
                    else:
                        score2 += 1
    elif(result == "single"):
        bases[0] = player
        bases[1] = copy[0]
        bases[2] = copy[1] 
        if(copy[2] != "NA"):
            if(team == 1):
                score1 += 1
            else:
                score2 += 1
    elif(result == "double"):
        bases[1] = player
        bases[0] = "NA"
        bases[2] = copy[0]
        if(copy[1] != "NA"):
            if(team == 1):
                score1 += 1
            else:
                score2 += 1
        if(copy[2] != "NA"):
            if(team == 1):
                score1 += 1
            else:
                score2 += 1
    elif(result == "triple"):
        bases[2] = player
        bases[0] = "NA"
        bases[1] = "NA"
        if(copy[0] != "NA"):
            if(team == 1):
                score1 += 1
            else:
                score2 += 1
        if(copy[1] != "NA"):
            if(team == 1):
                score1 += 1
            else:
                score2 += 1
        if(copy[2] != "NA"):
            if(team == 1):
                score1 += 1
            else:
                score2 += 1
    elif(result == "HR"):
        bases[2] = "NA"
        bases[0] = "NA"
        bases[1] = "NA"
        if(team == 1):
            score1 += 1
        else:
            score2 += 1
        if(copy[0] != "NA"):
            if(team == 1):
                score1 += 1
            else:
                score2 += 1
        if(copy[1] != "NA"):
            if(team == 1):
                score1 += 1
            else:
                score2 += 1
        if(copy[2] != "NA"):
            if(team == 1):
                score1 += 1
            else:
                score2 += 1

def atBat(batter, pitcher, outs):
    global innings
    global bases
    global score1
    global score2
    global hits1
    global hits2
    global so1
    global so2
    global walks1
    global walks2
    global pitches1
    global pitches2
    
    strikes = 0
    balls = 0

    print("\nP: %s" % pitcher + "\t|\tAt Bat: %s\n" % batter)
    #time.sleep(.5)
    while(strikes < 3 and balls < 4):
        #time.sleep(.25)
        if(innings % 2 == 0):
            print("\tPitches: %s" % pitches2 + "\tS: %s\tB: %s\tOuts: %s" % (strikes, balls, outs))

            pitch = float(random.randint(750, 1000)) / 10.0
            print("\t\tThrowing Pitch: %s" % str(pitch))
            pitches2 += 1
            strike = random.randint(0, 10)

            battingAvg = float(random.randint(100, 350)) / 1000.0
            hitP = int(battingAvg / pitch * 10000.0)
            if( float(random.randint(hitP, 100) / 10.0) >= 8.0):
                hit = random.randint(0, 100)
                if(hit <= 5):
                    print("\t\tHome Run!")
                    pitches2 += 1
                    return "HR"
                elif(hit <= 12):
                    print("\t\tTriple!")
                    pitches2 += 1
                    return "triple"
                elif(hit <= 20):
                    print("\t\tDouble!")
                    pitches2 += 1
                    return "double"
                elif(hit <= 35):
                    print("\t\tSingle!")
                    pitches2 += 1
                    return "single"
                elif(hit <= 50):
                    print("\t\tFoul Ball!")
                    if(strikes < 2):
                        strikes += 1
                else:
                    print("\t\tOut!")
                    return "out"
            else:
                if(strike <= 4):
                    print("\t\tStrike!")
                    strikes += 1
                else:
                    print("\t\tBall!")
                    balls += 1
        else:
            print("\tPitches: %s" % pitches1 + "\tS: %s\tB: %s\tOuts: %s" % (strikes, balls, outs))

            pitch = float(random.randint(750, 1000)) / 10.0
            print("\t\tThrowing Pitch: %s" % str(pitch))
            pitches1 += 1
            strike = random.randint(0, 10)

            battingAvg = float(random.randint(100, 350)) / 1000.0
            hitP = int(battingAvg / pitch * 10000.0)
            if( float(random.randint(hitP, 100) / 10.0) >= 8.0):
                hit = random.randint(0, 100)
                if(hit <= 5):
                    print("\t\tHome Run!")
                    pitches1 += 1
                    return "HR"
                elif(hit <= 7):
                    print("\t\tTriple!")
                    pitches1 += 1
                    return "triple"
                elif(hit <= 12):
                    print("\t\tDouble!")
                    pitches1 += 1
                    return "double"
                elif(hit <= 25):
                    print("\t\tSingle!")
                    pitches1 += 1
                    return "single"
                elif(hit <= 40):
                    print("\t\tFoul Ball!")
                    if(strikes < 2):
                        strikes += 1
                else:
                    print("\t\tOut!")
                    return "out"
            else:
                if(strike <= 4):
                    print("\t\tStrike!")
                    strikes += 1
                else:
                    print("\t\tBall!")
                    balls += 1
    if(balls == 4):
        print("\t\tWalk!")
        if(innings % 2 == 0):
            walks1 += 1
        else:
            walks2 += 1
        return "BB"
    elif(strikes == 3):
        print("\t\tStrike Out!")
        if(innings % 2 == 0):
            so1 += 1
        else:
            so2 += 1
        return "SO"

def findPitcher(roster):
    pitcherIndex = roster.index("P")
    return pitcherIndex

def halfInning(team1, team2, pos1, pos2):
    global innings
    global batter1
    global batter2
    global bases

    outs = 0
    printScore()

    while(outs < 3):
        if(innings % 2 == 0):
            result = atBat(team1[batter1], team2[findPitcher(pos2)], outs)
            batter1 = batter1 + 1
            if(batter1 > 8):
                batter1 = 0
        else:
            result = atBat(team2[batter2], team1[findPitcher(pos1)], outs)
            batter2 = batter2 + 1
            if(batter2 > 8):
                batter2 = 0
        
        if(result == "SO" or result == "out"):
            outs = outs + 1
        else:
            if(innings % 2 == 0):
                hit(team1[batter1 - 1], result)
            else:
                hit(team2[batter2 - 1], result)
        print("\nBases\t | 1B: %s > 2B: %s > 3B: %s" % (bases[0], bases[1], bases[2]))
    innings += 1
    
    bases = ["NA", "NA", "NA"]

def playGame(team1, team2, pos1, pos2):
    global innings
    date = datetime.datetime.now()
    print("\n---Play Ball! [Date: %s/%s/%s]---\n" % (date.month, date.day, date.year))

    while(score1 == score2 or innings <= 17):
        halfInning(team1, team2, pos1, pos2)
    
    print("---GAME OVER---")
    print("Team 1 | %sR | %sH | %sW | %sSO | %sPitches\n" % (score1, hits1, walks1, so1, pitches1))
    print("Team 2 | %sR | %sH | %sW | %sSO | %sPitches\n" % (score2, hits2, walks2, so2, pitches2))

def main():
    print("\n---Welcome to Baseball Simulator!---\n")

    team1 = createTeam()
    pos1 = assignPositions()
    team2 = createTeam()
    pos2 = assignPositions()

    print("Team 1:\n")
    printRoster(team1, pos1)
    print("\nTeam 2:\n")
    printRoster(team2, pos2)
    
    playGame(team1, team2, pos1, pos2)

main()

