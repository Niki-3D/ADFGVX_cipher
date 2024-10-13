from collections import defaultdict

class SortEncrypt:
    """Class responsible for sorting the encrypted message based on the codeword."""

    def sorting_encrypt_message(self, encrypted_message, codeword):
        """Further encrypt the message by sorting based on the codeword."""
        cleaned_codeword = self.clean_codeword(codeword)
        cipher_dict = self.create_cipher_dict(cleaned_codeword, encrypted_message)

        return self.build_sorted_message(cipher_dict)

    def clean_codeword(self, codeword):
        """Clean the codeword by converting to uppercase and removing spaces."""
        return ''.join(codeword.upper().split())

    def create_cipher_dict(self, codeword, encrypted_message):
        """Create a dictionary that maps each letter in the codeword to the corresponding characters in the encrypted message."""
        cipher_dict = defaultdict(list)

        for i, char in enumerate(encrypted_message):
            # Use modulo to cycle through the codeword
            key = codeword[i % len(codeword)]
            cipher_dict[key].append(char)

        return cipher_dict

    def build_sorted_message(self, cipher_dict):
        """Build the further encrypted message by sorting the keys of the cipher dictionary."""
        # Sort the keys and join the corresponding characters
        sorted_message = ''.join(''.join(cipher_dict[key]) for key in sorted(cipher_dict.keys()))
        return sorted_message.strip()

