file_read = open('Codingal.txt', 'r')
print("File in Read Mode - ")
print(file_read.read())
file_read.close

file_write = open('Codingal.txt', 'w')
file_write.write("File in Write Mode . . . .")
file_write.write("Hi! I am Penguin. I am 5 years old.")
file_write.close

file_append = open('Codingal.txt', 'a')
file_append.write("\n File in Append Mode")
file_append.write("Hi! I am Penguin. I am 5 years old.")
file_append.close