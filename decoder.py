def decode_ciphertext(ciphertext_file, mappings, output_file='decoded.txt'):
    """
    Decode ciphertext using provided letter mappings.

    Args:
        ciphertext_file (str): Path to the file containing the ciphertext.
        mappings (dict): Dictionary of ciphertext letter to plaintext letter mappings.
        output_file (str): Path to save the decoded text.
    """
    with open(ciphertext_file, 'r') as file:
        ciphertext = file.read().strip()

    decoded = []
    for char in ciphertext.upper():
        if char.isalpha():
            # Apply mapping if available, otherwise keep the original character
            decoded_char = mappings.get(char, char)
            decoded.append(decoded_char)
        else:
            # Keep non-alphabetic characters as-is
            decoded.append(char)

    decoded_text = ''.join(decoded)
    print("Decoded text:")
    print(decoded_text)

    with open(output_file, 'w') as file:
        file.write(decoded_text)

    print(f"\nDecoded text saved to {output_file}")

# Example usage:
# Define your mappings here (e.g., from the frequency analysis output)
mappings = {
    'Z': 'T',
    'H': 'H',
    'O': 'E',
    'L': 'A',
    'Q': 'Q',
    'R': 'U',
    'W': 'I',
    'F': 'F',
    'G': 'R',
    # Add more mappings as needed
}

decode_ciphertext('ciphertext.txt', mappings)