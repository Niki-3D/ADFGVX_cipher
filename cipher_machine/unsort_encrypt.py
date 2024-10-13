class UnsortEncrypt:
    """Class responsible for unsorting the encrypted message for decryption."""

    def unsort_encrypt_message(self, encrypted_message, codeword):
        """Unsort the message for decryption."""
        codeword = codeword.upper().replace(' ', '')
        sorted_codeword = sorted(list(codeword))
        encrypted_message = encrypted_message.split()

        cipher_dict = {letter: [] for letter in sorted_codeword}

        for i, part in enumerate(encrypted_message):
            cipher_dict[sorted_codeword[i % len(sorted_codeword)]].append(part)

        new_dict = {codeword[i]: cipher_dict[codeword[i]] for i in range(len(codeword))}

        further_unsorted_encrypted_message = ''.join(
            ''.join(new_dict[key][0][i] for key in new_dict if i < len(new_dict[key][0]))
            for i in range(max(len(new_dict[key][0]) for key in new_dict))
        )

        return further_unsorted_encrypted_message
