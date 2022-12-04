def solve(input_path: str) -> None:
    """
    Find the highest amount of calories carried by the elves.

    :param input_path: The path of the input file containing the calories carried by the elves.
    :return: Doesn't return anything, prints the answers.
    """
    # Read the input file
    file = open(input_path)
    lines = file.read().splitlines()

    # Transform the data into a usable format
    calories_by_elves = {}
    elf_calories = []
    elf_number = 0

    # Parse the file
    for line in lines:
        # The line is a number
        if line != "":
            elf_calories.append(int(line))
        # We've finished reading the calories of the current elf
        else:
            calories_by_elves[elf_number] = elf_calories.copy()
            elf_calories.clear()
            elf_number += 1
    # Don't forget about the last elf
    calories_by_elves[elf_number] = elf_calories.copy()

    # Sum the calories carried by each elf
    elf_number = 0
    for calories in calories_by_elves.values():
        calories_by_elves[elf_number] = sum(calories)
        elf_number += 1

    # Get the largest number
    print(f"The largest amount of calories carried by one of the elves is: {max(calories_by_elves.values())}")
    # Get the three largest ones
    _values = list(calories_by_elves.values())
    _values.sort()
    print(f"The total amount of calories carried by the three elves carrying the most is: {sum(_values[-3:])}")
