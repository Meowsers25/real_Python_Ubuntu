# my_output_file = open('hello.txt', 'w')
# my_output_file.writelines('This is my first file.')
# my_output_file.close()

# opening the same file with a w overwrites the previous file
# my_output_file = open('hello.txt', 'w')

# lines_to_write = 'This is my file \n There are many like it \n but this one is mine.'

# my_output_file.writelines(lines_to_write)
# my_output_file.close()

# open and use a to append to current file use \n
# my_output_file = open('hello.txt', 'a')
# next_line = '\n NON SEQUITOR'
# my_output_file.writelines(next_line)
# my_output_file.close()

# my_input_file = open('hello.txt', 'r')
# print(my_input_file.readlines())
# my_input_file.close()

# my_input_file = open('hello.txt', 'r')
# for line in my_input_file.readlines():
#     print(line, end="")
# my_input_file.close()

my_input_file = open('hello.txt', 'r')

line = my_input_file.readline()
while line != "":
    print(line),
    line = my_input_file.readline()
my_input_file.close()

