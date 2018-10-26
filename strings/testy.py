print("""this is a 
    string that spans multiple 
    lines......""")
print('Here is a string across multiple\
lines but printed out on one.')

phrase = 'Here is some Py practice'
print(len(phrase))
print(phrase[3])

print(phrase[0:5])  # 0 - 5
print(phrase[:5])  # 0 - 5
print(phrase[5:])  # 5 - end
print(phrase[:])  # whole thing

first_name = 'Luna'
last_name = 'Petunia'
print(first_name, last_name)
bazoo = 'bazinga'
print(bazoo[2:6])  #up to but not including

loud_voice = "Can you hear me now"
print(loud_voice.upper())
u_i = input('Hey what\'s up>')
print(u_i)

response = input('What shouls I yell?')
response = response.upper()
print('OK here goes.......', response)

num = '12'
print(num)
print(int(num) + 12)

num2 = '35'
num3 = 35
print(num2 + str(num3))

weight = 0.2
animal = 'newt'
print(f'{weight} is the weight of a {animal}')

phrase2 = 'Holy crappers its a newt'
print(phrase2.find('crappers'))  # returns first instance
print(phrase2.find('shite'))  # returns -1 if not found


my_story = "I'm telling the truth. I speak nothing but the truth"
print(my_story.replace('the truth', 'lies'))
print(my_story)
my_story = my_story.replace('the truth', 'lies')
print(my_story)

triple = 'AAA'
print(triple.find('a'))

lets_find = input('Enter a phrase: ')
print(lets_find.find('f'))