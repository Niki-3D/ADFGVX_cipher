class SortEncrypt:
    """Class responsible for sorting the encrypted message based on the codeword."""

    def sorting_encrypt_message(self, encrypted_message, codeword):
        """Further encrypt the message by sorting based on the codeword."""
        codeword = codeword.upper().replace(' ', '')
        codeword = list(codeword)
        cipher_dict = {letter: [] for letter in codeword}

        for i, char in enumerate(encrypted_message):
            cipher_dict[codeword[i % len(codeword)]].append(char)

        further_encrypted_message = ''.join(''.join(cipher_dict[key]) for key in sorted(cipher_dict.keys()))

        return further_encrypted_message.strip()
