letter = input("Enter a letter: ")

vowel_list = ['A', 'E', 'I', 'O', 'U']

if letter.upper() in vowel_list:
    print(f'{letter} is a vowel.')
else:
    print(f'{letter} is a consonant.')
