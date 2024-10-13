from collections import defaultdict

class UnsortEncrypt:
    """Class responsible for unsorting the encrypted message for decryption."""

    def unsort_encrypt_message(self, encrypted_message, codeword):
        """Unsort the message for decryption."""
        cleaned_codeword = self.clean_codeword(codeword)
        sorted_codeword = sorted(cleaned_codeword)
        encrypted_parts = encrypted_message.split()
        
        cipher_dict = self.create_cipher_dict(sorted_codeword, encrypted_parts)

        return self.build_unsorted_message(cleaned_codeword, cipher_dict)

    def clean_codeword(self, codeword):
        """Clean the codeword by converting to uppercase and removing spaces."""
        return ''.join(codeword.upper().split())

    def create_cipher_dict(self, sorted_codeword, encrypted_parts):
        """Create a dictionary mapping each letter in the sorted codeword to parts of the encrypted message."""
        cipher_dict = defaultdict(list)

        for i, part in enumerate(encrypted_parts):
            key = sorted_codeword[i % len(sorted_codeword)]
            cipher_dict[key].append(part)

        return cipher_dict

    def build_unsorted_message(self, codeword, cipher_dict):
        """Build the unsorted message by using the original codeword order."""
        # Create a new dictionary that maps the original codeword to the parts in the cipher dictionary
        new_dict = {codeword[i]: cipher_dict[codeword[i]] for i in range(len(codeword))}
        
        # Combine the parts in the correct order
        max_length = max(len(new_dict[key]) for key in new_dict)
        unsorted_message = ''.join(
            ''.join(new_dict[key][i] for key in new_dict if i < len(new_dict[key]))
            for i in range(max_length)
        )
        
        return unsorted_message
