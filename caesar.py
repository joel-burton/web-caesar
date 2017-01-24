def encrypt(text, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""

    for ch in text:
        if ch.lower() in alphabet:
            encrypted = encrypted + rotate_character(ch, rot)
        else:
            encrypted = encrypted + ch

    return encrypted



def alphabet_position(letter):
    letter = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    position = alphabet.find(letter)

    return position



def rotate_character(char, rot):
    rotation = (alphabet_position(char) + int(rot)) % 26
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()

    if char in lower:
        return lower[rotation]

    if char in upper:
        return upper[rotation]

    else:
        return char
