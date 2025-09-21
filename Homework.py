file_read = open('Homework2.txt', 'r')
print("File in Read Mode - ")
print(file_read.read())
file_read.close

file_write = open('Homework3.txt', 'w')
file_write.write("File in Write Mode . . . .")
file_write.write("Hi! My name is Anaira.")
file_write.close

file_append = open('Homework4.txt', 'a')
file_append.write("\n File in Append Mode")
file_append.write("I am turning 12 in 6 days.")
file_append.close