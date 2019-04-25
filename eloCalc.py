## Benjamin Chappell ##

import collections

def initNames():
    # Open the file that stores all of the names in order, and assign it to an array.
    nameFile = open("names.txt", "r+")
    names = nameFile.readlines()

    # Remove the \n from each of the strings.
    for i in range(0, len(names)):
        names[i] = names[i][:len(names[i])-1]

    # Return the list of names as well as the file object that accesses the names.
    return [names, nameFile]

def updateNames(nameFile, names):
    nameFile.truncate(0)

def initElo():
    eloFile = open("elo.txt", "r+")
    elos = eloFile.readlines()

    # Remove the \n from each of the elos (stored as strings) and convert it to an integer.
    for i in range(0, len(elos)):
        elos[i] = int(elos[i][:len(elos[i])-1])

    # Return the list of elos as well as the file object that accesses the elos.
    return[elos, eloFile]

def initializeStorage():
    nameFile = open("names.txt", "r+")
    eloFile = open("elo.txt", "r+")

    elo = eloFile.readlines()
    names = nameFile.readlines()

initElo()