print("Start game")

while True:

    event = input('Enter event: ')

    if event == "attack":
        print("Hero attacks")
    elif event == "heal":
        print("Hero heals")
    elif event == "info":
        print("Hero info")
        continue
    elif event == "exit":
        break
    else:
        print("Unknown command")

    print("Hero hp = 100")

print("End game")
