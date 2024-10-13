import string

class CipherAlphabet:
    """Class responsible for generating a cipher alphabet based on a keyword."""

    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.cipher_alphabet = self.generate_cipher_alphabet()
        self.cipher_table = self.generate_cipher_table()

    def deduplicate_keyword(self):
        """Return the keyword with duplicate characters removed."""
        return ''.join(sorted(set(self.keyword), key=self.keyword.index))

    def generate_cipher_alphabet(self):
        """Generate a cipher alphabet based on the keyword and remaining alphabet."""
        keyword_chars = self.deduplicate_keyword()
        remaining_chars = self.get_remaining_characters(keyword_chars)
        full_alphabet = keyword_chars + remaining_chars

        return ''.join(self.replace_with_numbers(full_alphabet))

    def get_remaining_characters(self, keyword_chars):
        """Return the characters that are not in the keyword."""
        return ''.join([char for char in string.ascii_uppercase if char not in keyword_chars])

    def replace_with_numbers(self, alphabet):
        """Replace letters A-J with alphanumeric counterparts."""
        replacements = {
            'A': 'A1', 'B': 'B2', 'C': 'C3', 'D': 'D4', 'E': 'E5',
            'F': 'F6', 'G': 'G7', 'H': 'H8', 'I': 'I9', 'J': 'J0'
        }
        return [replacements.get(char, char) for char in alphabet]

    def generate_cipher_table(self):
        """Generate the cipher table for encryption."""
        table = {}
        letters = ['A', 'D', 'F', 'G', 'V', 'X']
        for i in range(len(letters)):
            table[letters[i]] = {letters[j]: self.cipher_alphabet[i * len(letters) + j] for j in range(len(letters))}
        return table
