from collections import Counter

def frequency_analysis_from_file(filename, language='french'):
    """
    Perform frequency analysis on ciphertext from a file and suggest possible plaintext mappings.

    Args:
        filename (str): Path to the file containing the ciphertext.
        language (str): 'english' or 'french' for frequency tables.
    """
    with open(filename, 'r') as file:
        ciphertext = file.read().strip()

    # Remove non-alphabetic characters and convert to uppercase
    cleaned = ''.join(c for c in ciphertext.upper() if c.isalpha())
    if not cleaned:
        print("No alphabetic characters found in ciphertext.")
        return

    # Count letter frequencies
    freq = Counter(cleaned)
    total = sum(freq.values())

    # Print frequency table
    print("Letter frequencies in ciphertext:")
    for letter, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{letter}: {count} ({count/total:.2%})")

    # Suggest mappings based on language
    if language == 'english':
        # English letter frequencies (most common first)
        english_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
        print("\nSuggested mappings (English):")
        for cipher_letter, _ in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            if len(english_freq) > 0:
                print(f"{cipher_letter} → {english_freq[0]}")
                english_freq = english_freq[1:]
    elif language == 'french':
        # French letter frequencies (most common first)
        french_freq = 'ESAINTRULODCMPVÉQFGHJBXZYWK'
        print("\nSuggested mappings (French):")
        for cipher_letter, _ in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            if len(french_freq) > 0:
                print(f"{cipher_letter} → {french_freq[0]}")
                french_freq = french_freq[1:]
    else:
        print("Unsupported language. Use 'english' or 'french'.")

# Example usage
frequency_analysis_from_file('ciphertext.txt', language='english')