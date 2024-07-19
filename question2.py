def encrypt_string(input_string, shift):
    def shift_letter(letter, shift):
        if letter.islower():
            return chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
        elif letter.isupper():
            return chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        return letter

    # Split the string into words
    words = input_string.split()
    
    # Reverse every second word
    for i in range(1, len(words), 2):
        words[i] = words[i][::-1]
    
    # Combine the words back into a single string
    modified_string = ' '.join(words)
    
    # Shift each letter in the modified string
    encrypted_string = ''.join(shift_letter(char, shift) for char in modified_string)
    
    return encrypted_string

# Example 
input_string = "Hello World "
shift = 3
encrypted = encrypt_string(input_string, shift)
print(f"Original String: {input_string}")
print(f"Encrypted String: {encrypted}")
