connectedDevices = ["a", "b", "c", "d"]

if len(connectedDevices) > 1:
    for item in list(enumerate(connectedDevices, start = 1)):
        print("%s: %s" % (item[0], item[1]))

selection = connectedDevices[int(input("Selection: ")) - 1]

print(selection)
