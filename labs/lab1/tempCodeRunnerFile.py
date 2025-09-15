def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """

    print("you have some work todo!, caesar_cypher")

    # TODO: Get user input text
    text = input("Enter text: ")

    # TODO: Get shift value
    shift = int(input("Enter shift value (integer): "))

    # TODO: Ask user whether to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    # TODO: Implement encryption and decryption logic

    #reverses the shift if d is selected
    if choice == 'd':
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                posi = ord(char) - ord('a') 
                result += chr((posi + shift) % 26 + ord('a'))
            else:
                posi = ord((char) - ord('A'))
                result += chr((posi + shift) % 26 + ord('A'))
        else:
            result += char


    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
caesar_cipher()