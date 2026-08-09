MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-'}


sentence = input("Enter your sentence")

#print(f"Are you sure you want to transfer this sentence into morse, {decoded}")

confirmation = input(f"Are you sure you want to transfer this sentence into morse?, {sentence} (Y / N)")

if confirmation.upper() == "Y":
    new_sentence = sentence.upper()

    morse_resultat = []
    for letters in new_sentence:
        code = MORSE_CODE_DICT.get(letter,letter)
        morse_resultat.append(kode)

    morse_setning = ' '.join(morse_resultat)

    print(f"Here is your sentence converted into morse:, {morse_setning}")
else:
    print("Script is cancelled by user")