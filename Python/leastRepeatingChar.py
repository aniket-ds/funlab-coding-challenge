class LeastRepeatingCharacterFinder:
    """
    A class to find the least repeating character in a string.

    Attributes:
    None

    Methods:
    find_least_repeating_character(input_string): Finds the least repeating character in the input string.
    """

    def find_least_repeating_character(self, input_string):
        """
        Finds the least repeating character in the input string.

        Args:
        input_string (str): The input string to search.
    
        Raises:
        ValueError: If the input_string is empty or None.

        Returns:
        str: The least repeating character found in the input string.
        """

        try:
            # Check if input_string is empty or None
            if not input_string:
                raise ValueError("Input string cannot be empty")

            # Dictionary to store character counts
            char_counter_dict = {}

            # Count occurrences of each character
            for char in input_string:
                if char not in char_counter_dict:
                    char_counter_dict[char] = 1
                else:
                    char_counter_dict[char] += 1

            # Printing the count of each character in the input string
            print(char_counter_dict)

            # Find the least repeating character
            # assigning a greater positive number
            count = 99999 
            least_repeating_char = ''
            
            for char, char_count in char_counter_dict.items():
                if char_count < count:
                    count = char_count
                    least_repeating_char = char

            return least_repeating_char


        except Exception as e:
            raise ValueError(f"Error occurred: {e}")