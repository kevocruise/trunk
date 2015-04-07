'''
Simple use-case of dynamically calling functions in a class
'''

import sys

class Dyna:
    def __init__(self):
        pass


    def print_out(self, message):
        message = message.split(" ")
        exec_def = getattr(self, "{}_{}".format("print_out", message[0]))
        
        # Pop the head off the message then pass it to our dynamically called function
        del message[0]
        exec_def(" ".join(message))
    
    
    def print_out_one(self, message):
        sys.stdout.write("> {}\n".format(message))
        sys.stdout.flush()


    def print_out_two(self, message):
        sys.stdout.write("# {}\n".format(message))
        sys.stdout.flush()


new_dyna = Dyna()

new_dyna.print_out_one('''Print out messages to screen using different cursors
Specify 'one' for options one cursor followed be a space then your message or specify 'two' the same for the second cursor
    ''')

while 1:
    input = raw_input("input:  ")
    if input == "quit":
        break

    new_dyna.print_out(input)