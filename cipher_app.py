import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from cipher_machine import CipherMachine

class CipherApp(tk.Tk):
    """GUI Application for the Cipher Machine."""

    def __init__(self):
        """Initialize the main window and set up the GUI elements."""
        super().__init__()
        self.title("Cipher Machine")
        
        self.create_widgets()
        self.layout_widgets()

    # --- GUI Widget Creation ---

    def create_widgets(self):
        """Create the widgets for the GUI."""
        self.keyword_label = self.create_label("Enter Codeword:")
        self.keyword_entry = self.create_entry()

        self.message_label = self.create_label("Enter the Message:")
        self.message_text = self.create_scrolled_text()

        self.codeword_label = self.create_label("Enter Keyword:")
        self.codeword_entry = self.create_entry()

        self.result_label = self.create_label("Result:")
        self.result_text = self.create_scrolled_text()

        self.encrypt_button = self.create_button("Encrypt", self.run_encryption)
        self.decrypt_button = self.create_button("Decrypt", self.run_decryption)

    def create_label(self, text):
        """Create and return a label widget."""
        return ttk.Label(self, text=text)

    def create_entry(self):
        """Create and return an entry widget."""
        return ttk.Entry(self, width=30)

    def create_scrolled_text(self):
        """Create and return a scrolled text widget."""
        return scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=5)

    def create_button(self, text, command):
        """Create and return a button widget."""
        return ttk.Button(self, text=text, command=command)

    # --- GUI Layout Configuration ---

    def layout_widgets(self):
        """Organize widgets in the window."""
        self.layout_widget(self.keyword_label, self.keyword_entry)
        self.layout_widget(self.message_label, self.message_text)
        self.layout_widget(self.codeword_label, self.codeword_entry)
        self.layout_widget(self.result_label, self.result_text)
        self.layout_buttons(self.encrypt_button, self.decrypt_button)

    def layout_widget(self, label, widget):
        """Layout a label and its corresponding input widget."""
        label.pack(pady=5)
        widget.pack(pady=5)

    def layout_buttons(self, *buttons):
        """Layout multiple buttons in the window."""
        for button in buttons:
            button.pack(pady=5)

    # --- Event Handling ---

    def run_encryption(self):
        """Handles encryption when the button is pressed."""
        if self.validate_inputs():
            cipher_machine = CipherMachine(self.get_keyword())
            encrypted_msg = self.perform_encryption(cipher_machine)
            sorted_encrypted_msg = self.sort_encrypted_message(cipher_machine, encrypted_msg)
            self.display_result(f"Encrypted message: {sorted_encrypted_msg}")

    def run_decryption(self):
        """Handles decryption when the button is pressed."""
        if self.validate_inputs():
            cipher_machine = CipherMachine(self.get_keyword())
            unsorted_encrypted_msg = self.unsort_encrypted_message(cipher_machine)
            decrypted_msg = cipher_machine.decrypt_message(unsorted_encrypted_msg)
            self.display_result(f"Decrypted message: {decrypted_msg}")

    # --- Helper Methods ---

    def get_keyword(self):
        """Get and return the keyword from the entry."""
        return self.keyword_entry.get().strip()

    def get_message(self):
        """Get and return the message from the scrolled text."""
        return self.message_text.get("1.0", tk.END).strip()

    def get_codeword(self):
        """Get and return the codeword from the entry."""
        return self.codeword_entry.get().strip()

    def validate_inputs(self):
        """Validate user inputs and show error message if validation fails."""
        keyword = self.get_keyword()
        message = self.get_message()
        codeword = self.get_codeword()

        if not keyword or not message or not codeword:
            messagebox.showerror("Input Error", "All fields must be filled!")
            return False

        return True

    def perform_encryption(self, cipher_machine):
        """Encrypt the message using the CipherMachine."""
        return cipher_machine.encrypt_message(self.get_message())

    def sort_encrypted_message(self, cipher_machine, encrypted_msg):
        """Sort the encrypted message based on the codeword."""
        return cipher_machine.sorting_encrypt_message(encrypted_msg, self.get_codeword())

    def unsort_encrypted_message(self, cipher_machine):
        """Unsort the encrypted message for decryption."""
        return cipher_machine.unsort_encrypt_message(self.get_message(), self.get_codeword())

    def display_result(self, result):
        """Display the result in the result text area."""
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
