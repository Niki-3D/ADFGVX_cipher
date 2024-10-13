import string

class CipherAlphabet:
    """Class responsible for generating a cipher alphabet based on a keyword."""

    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.cipher_alphabet = self.generate_cipher_alphabet()
        self.cipher_table = self.generate_cipher_table()

    def deduplicate_keyword(self):
        """Return the keyword with duplicate characters removed."""
        unique_chars = []
        for char in self.keyword:
            if char not in unique_chars:
                unique_chars.append(char)
        return ''.join(unique_chars)

    def generate_cipher_alphabet(self):
        """Generate a cipher alphabet based on the keyword and remaining alphabet."""
        keyword_chars = self.deduplicate_keyword()
        cipher_alphabet = list(keyword_chars)

        for char in string.ascii_uppercase:
            if char not in cipher_alphabet:
                cipher_alphabet.append(char)

        # Replace letters A-J with numbered equivalents
        return ''.join(self.replace_with_numbers(cipher_alphabet))

    def replace_with_numbers(self, alphabet):
        """Replace letters A-J with alphanumeric counterparts."""
        replacements = {
            'A': 'A1', 'B': 'B2', 'C': 'C3', 'D': 'D4', 'E': 'E5',
            'F': 'F6', 'G': 'G7', 'H': 'H8', 'I': 'I9', 'J': 'J0'
        }
        return [replacements.get(c, c) for c in alphabet]

    def generate_cipher_table(self):
        """Generate the cipher table for encryption."""
        table = {}
        letters = ['A', 'D', 'F', 'G', 'V', 'X']
        for i in range(6):
            table[letters[i]] = {}
            for j in range(6):
                table[letters[i]][letters[j]] = self.cipher_alphabet[i * 6 + j]
        return table
