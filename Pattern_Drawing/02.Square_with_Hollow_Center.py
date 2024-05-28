def first_last_row(rows_count):
    print("*" * rows_count)


def middle_rows(rows_count):
    for _ in range(rows_count-2):
        print(f"*{' ' * (rows_count-2)}*")


number_of_rows = int(input("Enter square height: "))

first_last_row(number_of_rows)
middle_rows(number_of_rows)
first_last_row(number_of_rows)
