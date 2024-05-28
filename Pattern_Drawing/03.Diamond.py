def diamond_top_part(diamond_size):
    if diamond_size % 2 != 0:
        first_row = 1
    else:
        first_row = 2
    for row in range(first_row, diamond_size + 1, 2):
        print(f'{" " * ((diamond_size - row) // 2)}{"*" * row}')


def diamond_bottom_part(diamond_size):
    if diamond_size % 2 != 0:
        first_row = diamond_size - 2
    else:
        first_row = diamond_size
    for row in range(first_row, 0, -2):
        print(f'{" " * ((diamond_size - row) // 2)}{"*" * row}')


diamond_total_size = int(input("Enter diamond total height: "))
diamond_top_part(diamond_total_size)
diamond_bottom_part(diamond_total_size)
