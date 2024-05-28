def left_angled_triangle(rows_count):
    for row in range(rows_count, 0, -1):
        print("*" * row)


number_of_rows = int(input("Enter triangle height: "))
left_angled_triangle(number_of_rows)
