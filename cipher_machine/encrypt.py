class Encrypt:
    """Class responsible for encrypting a message."""

    def __init__(self, cipher_table):
        self.cipher_table = cipher_table

    def encrypt_message(self, message):
        """Encrypt the message by replacing characters with coordinates in the cipher table."""
        message = message.upper().replace(' ', '')
        encrypted_message = ''
        for letter in message:
            for key in self.cipher_table:
                for key2 in self.cipher_table[key]:
                    if letter == self.cipher_table[key][key2]:
                        encrypted_message += key + key2
        return encrypted_message
