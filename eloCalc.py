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

def updateElo(elos, eloFile):
    # Remove all of the old elos from the file.
    eloFile.truncate(0)

    for elo in elos:
        eloFile.write(str(elo) + "\n")

def initMatches():
    # Open the file that stores all of the matches. Matches are stored across pairs of lines, where the first line is the winner of the match, and the second is the loser of the match.
    matchFile = open("matches.txt", "r+")
    matches = matchFile.readlines()

    # Remove the \n from each of the names in the match.
    for i in range(0, len(matches)):
        matches[i] = int(matches[i][:len(matches[i])-1])

    return [matches, matchFile]

def getMatches(matches, names):
    matchList = []
    # Create a point object type to store the matches, where x is the winner and y is the loser.
    Point = collections.namedtuple("Point", ["x", "y"])

    # Put the matches into the list of matches.
    for i in range(0, len(matches), 2):
        winner = names.index(matches[i])
        loser = names.index(matches[i+1])
        match = Point(winner, y=loser)
        matchList.append(match)

    return matchList

def recalcElo(matches, elos, k):
    for match in matches:
        # Store these for easy access
        eloWinner = elos[match.x]
        eloLoser = elos[match.y]

        # Calculate the likelihood of success for both the winner and the loser
        expectedForWinner = expectedScore(eloWinner, eloLoser)
        expectedForLoser = expectedScore(eloLoser, eloWinner)

        # Calculate the new elo of both the winner and the loser
        newEloWinner = eloWinner + (k * (1 - expectedForWinner))
        newEloLoser = eloLoser + (k * (0 - expectedForLoser))

        # Set the new elos
        elos[match.x] = newEloWinner
        elos[match.y] = newEloLoser

    return elos

# Calculate the expected winning percentage of each of the players
def expectedScore(playerElo, opponentElo):
    bottom = 1 + (10 ** ((opponentElo - playerElo) / 400))
    return 1 / bottom

def main():
    # Get initialized name stuff.
    name = initNames()
    names = name[0]
    nameFile = name[1]

    # Get initialized elo stuff.
    elo = initElo()
    elos = elo[0]
    eloFile = elo[1]

    # Get initialized match stuff.
    match = initMatches()
    matches = match[0]
    matchFile = match[1]

    # Create the list of matches.
    matchList = getMatches(matches, names)

    # Match Matrix does not work. It takes the matches out of order, which would mess with the ELO calculations for large batches of tourney results.

    # K measures the volatility of the elo. As it stands, 30 is pretty volatile, might consider changing it back down to something like 20 or 15, but it is probably a good idea to keep it large with how small the data set is.
    k = 30
    elos = recalcElo(matchList, elos, k)

    # Put the updated elos back into the file they came from.
    updateElo(elos, eloFile)

    nameFile.close()
    eloFile.close()
    matchFile.close()