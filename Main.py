import string
import tkinter as tk
from tkinter import ttk, scrolledtext

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
        cipher_alphabet = cipher_alphabet.replace('A', 'A1').replace('B', 'B2').replace('C', 'C3').replace('D','D4').replace('E', 'E5').replace('F', 'F6').replace('G', 'G7').replace('H', 'H8').replace('I', 'I9').replace('J', 'J0')

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

class CipherApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Cipher Machine")

        self.keyword_label = ttk.Label(self, text="Enter Codeword:")
        self.keyword_entry = ttk.Entry(self, width=30)

        self.message_label = ttk.Label(self, text="Enter the Message:")
        self.message_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=5)

        self.codeword_label = ttk.Label(self, text="Enter Keyword:")
        self.codeword_entry = ttk.Entry(self, width=30)

        self.result_label = ttk.Label(self, text="Result:")
        self.result_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=5)

        self.encrypt_button = ttk.Button(self, text="Encrypt", command=self.run_encryption)
        self.decrypt_button = ttk.Button(self, text="Decrypt", command=self.run_decryption)

        # Layout
        self.keyword_label.pack(pady=5)
        self.keyword_entry.pack(pady=5)

        self.message_label.pack(pady=5)
        self.message_text.pack(pady=5)

        self.codeword_label.pack(pady=5)
        self.codeword_entry.pack(pady=5)

        self.result_label.pack(pady=10)
        self.result_text.pack(pady=10)

        self.encrypt_button.pack(pady=5)
        self.decrypt_button.pack(pady=5)

    def run_encryption(self):
        keyword = self.keyword_entry.get()
        message = self.message_text.get("1.0", tk.END)
        codeword = self.codeword_entry.get()

        cipher_machine = CipherMachine(keyword)

        encrypted_msg = cipher_machine.encrypt_message(message)
        sorted_encrypted_msg = cipher_machine.sorting_encrypt_message(encrypted_msg, codeword)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Encrypted message: {sorted_encrypted_msg}")

    def run_decryption(self):
        keyword = self.keyword_entry.get()
        message = self.message_text.get("1.0", tk.END)
        codeword = self.codeword_entry.get()

        cipher_machine = CipherMachine(keyword)

        unsorted_encrypted_msg = cipher_machine.unsort_encrypt_message(message, codeword)
        decrypted_msg = cipher_machine.decrypt_message(unsorted_encrypted_msg)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Decrypted message: {decrypted_msg}")

if __name__ == "__main__":
    app = CipherApp()
    app.mainloop()