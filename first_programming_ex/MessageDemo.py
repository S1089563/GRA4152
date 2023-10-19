def demoMessage():
    import argparse
    import textwrap
    from Message import Message
    parser = argparse.ArgumentParser(prog='my test program',
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    description=textwrap.dedent('''\
                                                 Messenger
                                     --------------------------------
                                     A simulated message program. A message has a sender, a recipient and the body of the message:
                                     Methods:
                                     1) getRecipient:  returns the recipient of the message
                                        @return recipient: return the recipient of the message
                                        
                                     2) getSender:  returns the sender of the message
                                        @return sender: returns the sender of the message
                                     
                                     3) getMessageBody: returns the message body
                                        @return message body: returns the message body
                                        
                                     4) appendLine: adds a message to the message body
                                        @param: message to add to the body
                                    
                                     5) toString: returns the complete message including recipient sender and body message
                                        @return mail: complete message including recipients, sender and body 

                                     '''),
                                    epilog=textwrap.dedent('''\
                                                Usage
                                     --------------------------------
                                      Customer1 = Customer(args.init_recipient, args.init_sender) # initialize a Message
                                      Customer1.appendLine(args.init_line) # add a message
                                      Customer1.toString() # returns the complete message
                                     ''')
                    )

    parser.add_argument('--init_sender', default='A', type=str)
    parser.add_argument('--init_recipient', default='B', type=str)
    parser.add_argument('--init_line', default='Hello', type=str)
    parser.add_argument('--run_demo', action='store_true', help='runs this demo')
    args = parser.parse_args()

    if args.run_demo:
        customer1 = Message(args.init_recipient, args.init_sender)
        customer1.appendLine(args.init_line)
        customer1.toString()
        print('Expected:\n From: A\n To: B\n Hello')
        customer2 = Message('A', 'B')
        customer2.appendLine('Hi')
        print('Total no. of messages: ', Message._no_messages)
        print('Expected: 2')
        print('Log of sender A: ', Message._log['A'])
        print('Expected: {A: {B,Hello}')


demoMessage()