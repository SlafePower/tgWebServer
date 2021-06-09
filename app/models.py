
class Message(object):
    def __init__(self, id, text, date) -> None:
        self.id = id
        self.text = text
        self.date = date # todo: fix to format HH:MM:SS YYYY 
    
    def __repr__(self) -> dict:
        return {
            'id': self.id,
            'text': self.text,
            'date': self.date
        }