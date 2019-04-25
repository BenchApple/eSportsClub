## Benjamin Chappell ##

import collections

def initNames():
    # Open the file that stores all of the names in order, and assign it to an array.
    nameFile = open("names.txt", "r+")
    names = nameFile.readlines()

    # Remove the \n from each of the strings.
    for i in range(0, len(names)):
        names[i] = names[i][:len(names[i])-1]

    return [names, nameFile]

def updateNames(nameFile, names):
    nameFile.truncate(0)


def initializeStorage():
    nameFile = open("names.txt", "r+")
    eloFile = open("elo.txt", "r+")

    elo = eloFile.readlines()
    names = nameFile.readlines()

initNames()