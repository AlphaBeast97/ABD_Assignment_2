def remove_duplicates(numbers):
    """Return a new list containing each number only once."""
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers


def find_average(numbers):
    """Return the average of the numbers in the list."""
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


def multiply_by_scalar(numbers, scalar):
    """Return a new list with every number multiplied by scalar."""
    return [number * scalar for number in numbers]


if __name__ == "__main__":
    values = [2, 4, 2, 6, 8, 4]
    scalar = 3

    print("Original list:", values)
    print("Without duplicates:", remove_duplicates(values))
    print("Average:", find_average(values))
    print("Multiplied by scalar:", multiply_by_scalar(values, scalar))