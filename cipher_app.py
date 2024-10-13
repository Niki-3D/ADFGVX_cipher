# cipher_app.py
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from cipher_machine import CipherMachine

class CipherApp(tk.Tk):
    """GUI Application for the Cipher Machine."""
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Cipher Machine")

        # GUI Elements
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
        """Handles encryption when the button is pressed."""
        try:
            keyword = self.keyword_entry.get().strip()
            message = self.message_text.get("1.0", tk.END).strip()
            codeword = self.codeword_entry.get().strip()

            if not keyword or not message or not codeword:
                raise ValueError("All fields must be filled!")

            cipher_machine = CipherMachine(keyword)
            encrypted_msg = cipher_machine.encrypt_message(message)
            sorted_encrypted_msg = cipher_machine.sorting_encrypt_message(encrypted_msg, codeword)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Encrypted message: {sorted_encrypted_msg}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def run_decryption(self):
        """Handles decryption when the button is pressed."""
        try:
            keyword = self.keyword_entry.get().strip()
            message = self.message_text.get("1.0", tk.END).strip()
            codeword = self.codeword_entry.get().strip()

            if not keyword or not message or not codeword:
                raise ValueError("All fields must be filled!")

            cipher_machine = CipherMachine(keyword)
            unsorted_encrypted_msg = cipher_machine.unsort_encrypt_message(message, codeword)
            decrypted_msg = cipher_machine.decrypt_message(unsorted_encrypted_msg)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Decrypted message: {decrypted_msg}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
