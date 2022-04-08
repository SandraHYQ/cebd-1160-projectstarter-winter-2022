import datetime


class Sale:
    id = 0
    date = datetime.date

    def __init__(self, id, date):
        self.id = id
        self.date = date
