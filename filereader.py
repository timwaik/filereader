import os
import sys

class File_Handler(object):
    """docstring for File_Handler."""
    def __init__(self):
        super(File_Handler, self).__init__()

    def mainloop(self):
        print("\nFile Handling application. What do you want to do?")
        print("1. Create file\n2. Read file\n3. Write to file\n4. Delete file ")
        choice = input("Type in 1, 2, 3 or 4 to pick answer, or [Quit] to quit.")
        if choice.lower() == "quit":
            sys.exit("Goodbye!")
        else:
            try:
                choice = int(choice)
            except ValueError:
                print("You didn't input a number!")

        if choice == 1:
            print("Creating file..")
            filename = input("What do you want to call it?\n")
            print("Creating file ", filename)
            self.file_new(filename)
            print("File created!")
        elif choice == 2:
            filename = input("What file do you want to read?")
            print("Reading file..")
            self.file_read(filename)
            print("END OF FILE")
        elif choice == 3:
            print("Do you want to [1] write to a new file, or [2] append to an existing file?")
            new_or_append = int(input())
            if new_or_append == 1:
                filename = input("What file do you want to create?")
                text_to_add = input("Type in the text you want to add:\n")
                print("Creating file and adding text..")
                self.file_write(filename, text_to_add)
            elif new_or_append == 2:
                filename = input("What file do you want to write to?")
                print("Writing to file", filename)
                text_to_add = input("Type in the text you want to add:\n")
                print("Adding text..")
                self.file_append(filename, text_to_add)
                print("Text added!")
        elif choice == 4:
            filename = input("What file do you want to delete?")
            print("Deleting file ", filename)
            self.file_delete(filename)
            print(filename, " successfully deleted!")
        else:
            print("Invalid input!")

    #NEW FILE
    def file_new(self, filename):
        new_file = open(filename, "x")

    #READ FILES
    def file_read(self, filename):
        read_file = open(filename, "r")
        print(read_file.read())

    def file_read_line(self, filename):
        read_file = open(filename, "r")
        print(read_file.readline())

    def file_read_custom(self, filename, limit):
        read_file = open(filename, "r")
        print(read_file.read(limit))

    def file_read_line_custom(self, filename, limit):
        read_file = open(filename, "r")
        print(read_file.readline())

    #WRITE FILES
    def file_write(self, filename, text_to_add):
        write_file = open(filename, "w")
        write_file.write(text_to_add)

    def file_append(self, filename, text_to_add):
        append_file = open(filename, "a")
        append_file.write(text_to_add)

    #DELETE FILES
    def file_delete(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print(filename, " does not exist!")

p1 = File_Handler()
while True:
    p1.mainloop()
