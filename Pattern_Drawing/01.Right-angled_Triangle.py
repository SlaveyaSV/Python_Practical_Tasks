def right_angled_triangle(rows_count):
    for row in range(1, rows_count + 1):
        print("*" * row)


number_of_rows = int(input("Enter triangle height: "))
right_angled_triangle(number_of_rows)
