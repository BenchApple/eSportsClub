## Benjamin Chappell ##

import collections

# Initializes the list of names.
def initNames():
    # Open the file that stores all of the names in order, and assign it to an array.
    nameFile = open("names.txt", "r+")
    names = nameFile.readlines()

    # Remove the \n from each of the strings.
    for i in range(0, len(names)):
        names[i] = names[i][:len(names[i])-1]

    # Return the list of names as well as the file object that accesses the names.
    return [names, nameFile]

# Initializes the list of ELOs
def initElo():
    eloFile = open("elo.txt", "r+")
    elos = eloFile.readlines()

    # Remove the \n from each of the elos (stored as strings) and convert it to an integer.
    for i in range(0, len(elos)):
        elos[i] = int(elos[i][:len(elos[i])-1])

    # Return the list of elos as well as the file object that accesses the elos.
    return[elos, eloFile]

# Creates a matrix of the matches that happened in a given tourney. Make sure to enter the matches in chronological order. 
# The first number entered is the winner of the match. Reference the list of names to see the indices of each person.
# If I can figure out a better way to do this in the future I most certainly will use that.
# The matches are read in as a collection, aka a point, where the first one is known as winner and the second one is known as loser.
def createMatchesMatrix(matches, names):
    # Create a matrix of zeros to store the matches
    matchMatrix = [[0 for j in range(0,len(names))] for i in range(0, len(names))]

    for match in matches:
        matchMatrix[match.winner][match.loser] += 1

    return matchMatrix

def getMatches():
    matches = []
    Point = collections.namedtuple("Point", ["winner", "loser"])

def main():
    # Get initialized name stuff.
    name = initNames()
    names = name[0]
    nameFile = name[1]

    # Get initialized elo stuff.
    elo = initElo()
    elos = elo[0]
    eloFile = elo[1]

