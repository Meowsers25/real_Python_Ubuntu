word = input('Please enter a word: ')

if len(word) < 5:
    print('Less than 5 characters')
elif len(word) > 5:
    print('More than 5 characters.')
else:
    print('Word has 5 characters.')