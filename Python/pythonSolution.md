# Python Class Documentation: LeastRepeatingCharacterFinder 

## Objective

The `LeastRepeatingCharacterFinder` class is designed to find the least repeating character in a given input string. This class provides a simple solution without utilizing any in-built or 3P packages.

## Approach

The approach used by the `LeastRepeatingCharacterFinder` class is straightforward:

1. **Input Validation**: Check if the input string is empty or None. If so, raise a ValueError.
2. **Count Characters**: Count the occurrences of each character in the input string using a dictionary.
3. **Find Minimum Count**: Identify the character with the minimum count of occurrences.
4. **Return Result**: Return the least repeating character found in the input string.

## Function Details

### `find_least_repeating_character(input_string)`

This method takes a single argument `input_string`, which is the string in which we want to find the least repeating character.

#### Parameters

- `input_string` (str): The input string to search.

#### Raises

- `ValueError`: If the input_string is empty or None.

#### Returns

- `str`: The least repeating character found in the input string.

#### Description

This method finds the least repeating character in the input string using the approach mentioned above. It starts by validating the input string to ensure it's not empty or None. Then, it counts the occurrences of each character in the input string, identifies the character with the minimum count, and returns that character.

## Usage

To use the `LeastRepeatingCharacterFinder` class, follow these steps:

1. Import the class.
2. Create an instance of the class.
3. Call the `find_least_repeating_character()` method with the input string as an argument.

#### Example

```python
from leastRepeatingChar import LeastRepeatingCharacterFinder
finder = LeastRepeatingCharacterFinder()
input_string = "aaabbbcccdddeeefffg"
result = finder.find_least_repeating_character(input_string)
print(result)
```

#### Expected Output
```python
$ python3 findLeastRepeatingChar.py
{'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3, 'f': 3, 'g': 1}
g
```