
def main():
    test = open("test.txt", "r+")

    lines = ["12", "14", "15", "16"]

    test.truncate(0)

    for i in lines:
        test.write(i + "\n")

    test.close()

main()