# This module defines the Message class. Models an email message
# A message has a recipient, a sender, and a message text.
class Message:
    _no_messages=0
    _log = dict()
    ## Constructor method for the class Message. it receives a recipient and a sender
    ## @param recipient: recipient of the message
    ## @param sender: sender of the message
    def __init__(self, recipient, sender):
            self._recipient = recipient
            self._sender = sender
            self._messageBody = ""
            if sender not in Message._log:
                Message._log[sender] = []

    ## Returns the recipient of the message
    ## @return recipient
    def getRecipient(self):
        return self._recipient

    ## Returns the sender of the message
    ## @return sender
    def getSender(self):
        return self._sender

    ## Returns the message body
    ## @return message body
    def getMessageBody(self):
        return self._messageBody

    ## Adds a line to the message body

    # @param line: line of text to add to the body
    def appendLine(self, line):
        self._messageBody += line + '\n'
        self.log_messages(line)

    ## Returns the entire message
    # prints the complete email
    def toString(self):
        print( 'From: '+ self.getSender()+ '\nTo: ', self.getRecipient()+ '\n'+self.getMessageBody())

    ##logs messages
    def log_messages(self, message):
        sender = self.getSender()
        recipient = self.getRecipient()
        Message._log[sender].append({recipient: message})
        Message._no_messages += 1



