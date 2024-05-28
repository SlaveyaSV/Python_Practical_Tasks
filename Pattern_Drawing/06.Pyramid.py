def pyramid(height):
    for row in range(1, height + 1):
        for column in range(1, height * 2):
            if height - row < column < height + row:
                print("*", end="")
            else:
                print(" ", end="")
        print()


pyramid_height = int(input("Enter pyramid height: "))
pyramid(pyramid_height)
