import string

class CipherMachine:
    def __init__(self, keyword):
        self.keyword = keyword
        self.cipher_alphabet = self.generate_cipher_alphabet()
        self.cipher_table = self.generate_cipher_table()

    def generate_cipher_alphabet(self):
        keyword = self.keyword.upper()
        unique_letters = []
        for char in keyword:
            if char not in unique_letters:
                unique_letters.append(char)
        for char in string.ascii_uppercase:
            if char not in unique_letters:
                unique_letters.append(char)
        cipher_alphabet = ''.join(unique_letters)
        cipher_alphabet = cipher_alphabet.replace('A', 'A1').replace('B', 'B2').replace('C', 'C3').replace('D',
                                                                                                           'D4').replace(
            'E', 'E5').replace('F', 'F6').replace('G', 'G7').replace('H', 'H8').replace('I', 'I9').replace('J', 'J0')

        return cipher_alphabet

    def generate_cipher_table(self):
        table = {}
        letters = ['A', 'D', 'F', 'G', 'V', 'X']
        for i in range(6):
            table[letters[i]] = {}
            for j in range(6):
                table[letters[i]][letters[j]] = self.cipher_alphabet[i * 6 + j]

        return table

    def encrypt_message(self, message):
        message = message.upper().replace(' ', '')
        encrypted_message = ''
        for letter in message:
            for key in self.cipher_table:
                for key2 in self.cipher_table[key]:
                    if letter == self.cipher_table[key][key2]:
                        encrypted_message += key + key2

        return encrypted_message

    def sorting_encrypt_message(self, encrypted_message, codeword):
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
        decrypted_message = ''
        for i in range(0, len(message), 2):
            for key in self.cipher_table:
                if message[i] == key:
                    for key2 in self.cipher_table[key]:
                        if message[i + 1] == key2:
                            decrypted_message += self.cipher_table[key][key2]

        return decrypted_message


def main():
    keyword = input("Enter keyword for the cipher machine: ")
    cipher_machine = CipherMachine(keyword)

    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").upper()

    if choice == 'E':
        message = input("Enter the message to encrypt: ")
        codeword = input("Enter the codeword: ")
        keyword = input("Enter the keyword: ")

        encrypted_msg = cipher_machine.encrypt_message(message)
        sorted_encrypted_msg = cipher_machine.sorting_encrypt_message(encrypted_msg, codeword)
        print("Encrypted message:", sorted_encrypted_msg)

    elif choice == 'D':
        message = input("Enter the message to decrypt: ")
        codeword = input("Enter the codeword: ")
        keyword = input("Enter the keyword: ")

        unsorted_encrypted_msg = cipher_machine.unsort_encrypt_message(message, codeword)
        decrypted_msg = cipher_machine.decrypt_message(unsorted_encrypted_msg)
        print("Decrypted message:", decrypted_msg)

    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
