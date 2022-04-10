def print_maps(playersmap, bothitmap):
    print("\n")


    for index, row in enumerate(playersmap): # playersmap and bothitmap got the same rows and columns
        print("  ".join(row) + "  |  " + "  ".join(bothitmap[index]))
    print("Your ships on the map             |  The locations you hit and missed on bottard's map")