class Encrypt:
    """Class responsible for encrypting a message."""

    def __init__(self, cipher_table):
        self.cipher_table = cipher_table
        self.reverse_lookup = self.create_reverse_lookup()

    def create_reverse_lookup(self):
        """Create a reverse lookup dictionary to map characters to their coordinates in the cipher table."""
        reverse_lookup = {}
        for row_key in self.cipher_table:
            for col_key in self.cipher_table[row_key]:
                value = self.cipher_table[row_key][col_key]
                reverse_lookup[value] = row_key + col_key
        return reverse_lookup

    def encrypt_message(self, message):
        """Encrypt the message by replacing characters with coordinates in the cipher table."""
        # Clean up the message: convert to uppercase and remove spaces
        message = message.upper().replace(' ', '')
        
        # Build the encrypted message using the reverse lookup
        encrypted_message = ''.join(self.reverse_lookup.get(letter, '') for letter in message)
        
        return encrypted_message
