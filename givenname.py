def main():
    names = []
    i = 0
    while i < 5:
        name = input("Vorname > ")
        names.append(name)
        i += 1
    index = int(input("Welcher Vorname soll ausgegeben werden (1-5) > "))
    print(names[index - 1])


if __name__ == "__main__":
    main()