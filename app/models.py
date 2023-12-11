class Email:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def to_dict(self):
            return {
                "sender": self.sender,
                "recipient": self.recipient,
                "subject": self.subject,
                "body": self.body
            }
