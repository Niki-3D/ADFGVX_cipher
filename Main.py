import string
import tkinter as tk
from tkinter import Label, Text, Button

def generate_cipher_alphabet(keyword):
    keyword = keyword.upper()
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


def generate_cipher_table(cipher_alphabet):
    table = {}
    letters = ['A', 'D', 'F', 'G', 'V', 'X']
    for i in range(6):
        table[letters[i]] = {}
        for j in range(6):
            table[letters[i]][letters[j]] = cipher_alphabet[i * 6 + j]

    return table


def encrypt_message(message, table):
    message = message.upper().replace(' ', '')
    encrypted_message = ''
    for letter in message:
        for key in table:
            for key2 in table[key]:
                if letter == table[key][key2]:
                    encrypted_message += key + key2

    return encrypted_message


def sorting_encrypt_message(encrypted_message, keyword):
    keyword = keyword.upper().replace(' ', '')
    keyword = list(keyword)
    cipher_dict = {}
    for letter in keyword:
        cipher_dict[letter] = []
    for i in range(len(encrypted_message)):
        cipher_dict[keyword[i % len(keyword)]].append(encrypted_message[i])
    further_encrypted_message = ''
    for key in cipher_dict:
        cipher_dict[key] = ''.join(cipher_dict[key])

    for key in sorted(cipher_dict.keys()):
        further_encrypted_message += cipher_dict[key] + ' '
    further_encrypted_message = further_encrypted_message.strip()

    return further_encrypted_message


def unsort_encrypt_message(encrypted_message, keyword):
    keyword = keyword.upper().replace(' ', '')
    sorted_keyword = sorted(list(keyword))
    cipher_dict = {}
    further_unsorted_encrypted_message = ''
    encrypted_message = encrypted_message.split()
    for letter in sorted_keyword:
        cipher_dict[letter] = []
    for i in range(len(encrypted_message)):
        cipher_dict[sorted_keyword[i % len(sorted_keyword)]].append(encrypted_message[i])
    new_dict = {}
    for i in range(len(keyword)):
        new_dict[keyword[i]] = cipher_dict[keyword[i]]

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


def decrypt_message(message, table):
    decrypted_message = ''
    for i in range(0, len(message), 2):
        for key in table:
            if message[i] == key:
                for key2 in table[key]:
                    if message[i + 1] == key2:
                        decrypted_message += table[key][key2]

    return decrypted_message


print("Cipher Table:", generate_cipher_table(generate_cipher_alphabet('nachtbommenwerper')))
encrypted_msg = encrypt_message('attackat1200am', generate_cipher_table(generate_cipher_alphabet('nachtbommenwerper')))
print("Encrypted message:", encrypted_msg)
sorted_encrypted_msg = sorting_encrypt_message(encrypted_msg, 'PRIVACY')
print("Sorted encrypted message:", sorted_encrypted_msg)
unsorted_encrypted_msg = unsort_encrypt_message(sorted_encrypted_msg, 'PRIVACY')
print("Unsorted encrypted message:", unsorted_encrypted_msg)
decrypted_msg = decrypt_message(unsorted_encrypted_msg,
                                generate_cipher_table(generate_cipher_alphabet('nachtbommenwerper')))
print("Decrypted message:", decrypted_msg)
