import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from ttkthemes import ThemedTk
from cipher_machine import CipherMachine

class CipherApp(ThemedTk):
    """GUI Application for the Cipher Machine with VS Code-like dark theme."""

    def __init__(self):
        """Initialize the main window and set up the GUI elements."""
        super().__init__(theme="equilux")  # Set a dark theme
        self.title("Cipher Machine")

        self.style = ttk.Style()
        self.configure_gui_style()

        self.create_widgets()
        self.layout_widgets()

    def configure_gui_style(self):
        """Configure the style to have a dark theme similar to VS Code."""
        dark_bg = "#2D2D2D"
        input_bg = "#3C3C3C"
        accent_blue = "#007ACC"
        self.style.configure('TLabel', foreground="white", background=dark_bg, font=("Helvetica", 10))
        self.style.configure('TButton', foreground="white", background=accent_blue, font=("Helvetica", 10), relief="flat", padding=5)
        self.style.configure('TEntry', background=input_bg, foreground="white", insertcolor="white")
        self.style.configure('TScrolledText', background=input_bg, foreground="white", insertcolor="white")
        self.config(background=dark_bg)

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

    def layout_widgets(self):
        """Organize widgets in the window using grid layout."""
        self.layout_widget(self.keyword_label, self.keyword_entry, 0)
        self.layout_widget(self.message_label, self.message_text, 1)
        self.layout_widget(self.codeword_label, self.codeword_entry, 2)
        self.layout_widget(self.result_label, self.result_text, 3)
        self.layout_buttons(4)

    def layout_widget(self, label, widget, row):
        """Layout a label and its corresponding input widget."""
        label.grid(row=row, column=0, sticky="W", padx=10, pady=10)
        widget.grid(row=row, column=1, padx=10, pady=10, sticky="EW")

    def layout_buttons(self, row):
        """Layout encryption and decryption buttons."""
        self.encrypt_button.grid(row=row, column=0, padx=10, pady=10, sticky="EW")
        self.decrypt_button.grid(row=row, column=1, padx=10, pady=10, sticky="EW")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def create_label(self, text):
        """Create and return a label widget."""
        return ttk.Label(self, text=text, style='TLabel')

    def create_entry(self):
        """Create and return an entry widget."""
        return ttk.Entry(self, width=30, style='TEntry')

    def create_scrolled_text(self):
        """Create and return a scrolled text widget."""
        st = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=5)
        st.config(background="#3C3C3C", foreground="white", insertbackground="white", relief="flat", borderwidth=0)
        return st

    def create_button(self, text, command):
        """Create and return a button widget."""
        return ttk.Button(self, text=text, command=command, style='TButton')

    def run_encryption(self):
        """Handle encryption when the button is pressed."""
        if self.validate_inputs():
            cipher_machine = CipherMachine(self.get_keyword())
            encrypted_msg = cipher_machine.encrypt_message(self.get_message())
            sorted_encrypted_msg = cipher_machine.sorting_encrypt_message(encrypted_msg, self.get_codeword())
            self.display_result(f"Encrypted message: {sorted_encrypted_msg}")

    def run_decryption(self):
        """Handle decryption when the button is pressed."""
        if self.validate_inputs():
            cipher_machine = CipherMachine(self.get_keyword())
            unsorted_encrypted_msg = cipher_machine.unsort_encrypt_message(self.get_message(), self.get_codeword())
            decrypted_msg = cipher_machine.decrypt_message(unsorted_encrypted_msg)
            self.display_result(f"Decrypted message: {decrypted_msg}")

    def validate_inputs(self):
        """Validate user inputs and show error message if validation fails."""
        if not all([self.get_keyword(), self.get_message(), self.get_codeword()]):
            messagebox.showerror("Input Error", "All fields must be filled!")
            return False
        return True

    def get_keyword(self):
        """Get and return the keyword from the entry."""
        return self.keyword_entry.get().strip()

    def get_message(self):
        """Get and return the message from the scrolled text."""
        return self.message_text.get("1.0", tk.END).strip()

    def get_codeword(self):
        """Get and return the codeword from the entry."""
        return self.codeword_entry.get().strip()

    def display_result(self, result):
        """Display the result in the result text area."""
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)


if __name__ == "__main__":
    app = CipherApp()
    app.mainloop()
