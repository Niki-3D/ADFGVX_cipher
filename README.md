# ADFGVX Cipher Machine

https://en.wikipedia.org/wiki/ADFGVX_cipher
## Overview

This Python script implements a  version of the ADFGVX cipher, a field cipher used by the German Army during World War I. The ADFGVX cipher is a combination of a Polybius square and a columnar transposition cipher. The script allows users to encrypt and decrypt messages using a given codeword.

## Usage

To use the script, follow these steps:

1. Run the script.
2. Enter a codeword when prompted. This codeword will be used to generate the cipher alphabet.
3. Enter a message to be encrypted or decrypted in the provided text area.
4. Enter a keyword for encryption or decryption in the corresponding entry field.
5. Click the "Encrypt" or "Decrypt" button to view the result in the output text area.

## ADFGVX Cipher Algorithm

The script employs the following steps for encryption:

1. **Generate Cipher Alphabet**: The script generates a cipher alphabet based on the provided codeword, ensuring uniqueness and incorporating digits 0-9.

2. **Generate Cipher Table**: A 6x6 table is created using the letters ADFGVX as column headings and row identifiers. The table is populated with the generated cipher alphabet.

3. **Encrypt Message**: The input message is converted to uppercase, and each letter is substituted with the corresponding ADFGVX pair from the cipher table.

4. **Sorting Encryption**: The encrypted message is further encrypted using a keyword. The columns are sorted alphabetically based on the keyword, and the resulting ciphertext is constructed.

For decryption, the reverse process is applied:

1. **Unsort Encryption**: The encrypted message is decrypted by reconstructing the columns based on the provided keyword.

2. **Decrypt Message**: The decrypted columns are used to look up the original ADFGVX pairs from the cipher table, resulting in the decrypted message.

## Example

Using the example from the Wikipedia page:

- **Codeword**: "nachtbommenwerper"
- **Message**: "attack at 1200am"
- **Keyword**: "PRIVACY"

The encrypted message is: "DGDD DAGD DGAF ADDF DADV DVFA ADVX"

The decrypted message is: "ATTACKAT1200AM"

