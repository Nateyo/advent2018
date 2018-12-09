"""
Day 5: Alchemical Reduction
https://adventofcode.com/2018/day/5
"""


def will_react(a: str, b: str) -> bool:
    """
    Compare two polymers to determine reaction potential.

    Args:
        a (str): A single character.
        b (str): A single character.

    Returns:
        bool: True if the polymers will react, False otherwise.
    """
    return abs(ord(a) - ord(b)) == 32


def react(unreacted: str) -> list:
    """
    Given a string, react the polymers.

    Args:
        unreacted (str): The polymer string to be reacted.

    Returns:
        list: List of characters for the fully reacted polymer chain.
    """
    unreacted = unreacted.strip()
    reacted = []

    for char in unreacted:
        if not reacted:
            reacted.append(char)
        else:
            if will_react(char, reacted[-1]):
                reacted.pop()
            else:
                reacted.append(char)

    return reacted


def find_character_set(polymer: str) -> dict:
    """
    Given a polymer, determine the character set 

    Args:
        polymer (str): The polymer to be evaluated.

    Returns:
        dict: A dictionary where every key a character and the value 
              is the occurence sum of that character.
    """
    character_set = {}

    for char in polymer.lower():
        if char not in character_set:
            character_set[char] = 1
        else:
            character_set[char] += 1

    return character_set


def main():
    # Test will_react function
    test_will_react = will_react("c", "C")
    assert test_will_react == True

    # Test react function
    test_string = "dabAcCaCBAcCcaDA"
    reacted = react(test_string)
    assert len(reacted) == len("dabCBAcaDA")

    # Read in our polymer
    with open("day5/polymer.txt") as f:
        polymer = f.read()

    result = react(polymer)
    print(f"Original Reaction Length: {len(result)}")

    print("Evaluating polymer for troublesome units...")

    # Let's not assume our character set, but instead determine them all
    charset = find_character_set(polymer)

    min_polymer_count = 999999
    min_polymer_char = None

    # For every character in characterset, remove them from original polymer
    # and react the resulting polymer.
    for char in charset:
        reduced_polymer = polymer.replace(char, "")
        reduced_polymer = reduced_polymer.replace(char.upper(), "")

        polymer_length = len(react(reduced_polymer))

        if polymer_length < min_polymer_count:
            min_polymer_count = polymer_length
            min_polymer_char = char

    print(
        f"Removing unit '{min_polymer_char}' produced the best length: {min_polymer_count}"
    )


if __name__ == "__main__":
    main()
