# cipher_machine.py
import string

class CipherMachine:
    """Class representing a cipher machine that encrypts and decrypts messages using a keyword cipher."""
    
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

    def encrypt_message(self, message):
        """Encrypts the message by replacing characters with coordinates in the cipher table."""
        message = message.upper().replace(' ', '')
        encrypted_message = ''
        for letter in message:
            for key in self.cipher_table:
                for key2 in self.cipher_table[key]:
                    if letter == self.cipher_table[key][key2]:
                        encrypted_message += key + key2

        return encrypted_message

    def sorting_encrypt_message(self, encrypted_message, codeword):
        """Further encrypt the message by sorting based on the codeword."""
        codeword = codeword.upper().replace(' ', '')
        codeword = list(codeword)
        cipher_dict = {}
        for letter in codeword:
            cipher_dict[letter] = []
        for i in range(len(encrypted_message)):
            cipher_dict[codeword[i % len(codeword)]].append(encrypted_message[i])
        further_encrypted_message = ''
        for key in cipher_dict:
            cipher_dict[key] = ''.join(cipher_dict[key])

        for key in sorted(cipher_dict.keys()):
            further_encrypted_message += cipher_dict[key] + ' '
        further_encrypted_message = further_encrypted_message.strip()

        return further_encrypted_message

    def unsort_encrypt_message(self, encrypted_message, codeword):
        """Unsort the message for decryption."""
        codeword = codeword.upper().replace(' ', '')
        sorted_codeword = sorted(list(codeword))
        cipher_dict = {}
        further_unsorted_encrypted_message = ''
        encrypted_message = encrypted_message.split()
        for letter in sorted_codeword:
            cipher_dict[letter] = []
        for i in range(len(encrypted_message)):
            cipher_dict[sorted_codeword[i % len(sorted_codeword)]].append(encrypted_message[i])
        new_dict = {}
        for i in range(len(codeword)):
            new_dict[codeword[i]] = cipher_dict[codeword[i]]

        for key in new_dict:
            new_dict[key][0] = list(new_dict[key][0])
        i = 0
        while True:
            for key in new_dict:
                if len(new_dict[key][0]) > i:
                    further_unsorted_encrypted_message += new_dict[key][0][i]
                else:
                    break

            if i >= max(len(new_dict[key][0]) for key in new_dict):
                break

            i += 1

        return further_unsorted_encrypted_message

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
