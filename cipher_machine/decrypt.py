class Decrypt:
    """Class responsible for decrypting a message."""

    def __init__(self, cipher_table):
        self.cipher_table = cipher_table

    def decrypt_message(self, message):
        """Decrypt the message by reversing the encryption process."""
        decrypted_message = ''
        for i in range(0, len(message), 2):
            for key in self.cipher_table:
                if message[i] == key:
                    for key2 in self.cipher_table[key]:
                        if message[i + 1] == key2:
                            decrypted_message += self.cipher_table[key][key2]
        return decrypted_message
