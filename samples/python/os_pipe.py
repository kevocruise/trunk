import os
from threading import Thread


def receiver(receiver_reader, sender_writer):
    """Receive a message from a pipe
    :param receiver_reader Read object from os.pipe that expects input on from a sender
    :param sender_writer Write object from os.pipe to write to, to tell the sender the message has been received
    """

    i = 0
    while 1:

        # Receive a message then message the sender back on the sender write pipe
        received = os.read(receiver_reader, 128)
	    print("%d: %s" % (i, received))
        os.write(sender_writer, "received")
        i += 1

	if received == "quit":
            break


# Create the read and write for the sender and receiver
receiver_read, receiver_write = os.pipe()
sender_read, sender_write = os.pipe()

read_thread = Thread(target=receiver, args=(receiver_read, sender_write))
read_thread.start()

while 1:

    # Take in input from the user and write the message to the receiver
    user_input = raw_input("~ ")
    os.write(receiver_write, user_input)

    # Wait for a message back from the receiver
    message_back = os.read(sender_read, 128)
    if message_back != "received":
        raise Exception("something went wrong, receiver delivered message %s" % message_back)

    # Quit is the user wants to quit
    if user_input == "quit":
        read_thread.join()
	break
