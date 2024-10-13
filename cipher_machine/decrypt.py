class Decrypt:
    """Class responsible for decrypting a message."""

    def __init__(self, cipher_table):
        self.cipher_table = cipher_table
        self.reverse_lookup = self.create_reverse_lookup()

    def create_reverse_lookup(self):
        """Create a reverse lookup dictionary to map coordinates back to characters."""
        reverse_lookup = {}
        for row_key in self.cipher_table:
            for col_key in self.cipher_table[row_key]:
                value = self.cipher_table[row_key][col_key]
                reverse_lookup[row_key + col_key] = value
        return reverse_lookup

    def decrypt_message(self, message):
        """Decrypt the message by reversing the encryption process."""
        decrypted_message = []
        
        # Iterate over the message in pairs of two (coordinates)
        for i in range(0, len(message), 2):
            # Get the coordinates from the message
            coord = message[i:i+2]
            # Retrieve the original character from the reverse lookup
            decrypted_character = self.reverse_lookup.get(coord, '')
            decrypted_message.append(decrypted_character)
        
        return ''.join(decrypted_message)
