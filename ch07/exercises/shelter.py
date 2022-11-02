import time


class Animal:
    def __init__(self, name: str, type: str):
        '''
        constructor
        name: (str) Name of the animal
        type: (str): Type of the animal. For example, 'dog' or 'cat'
        '''
        self.name = name
        self.type = type
        self.id = id(name)
        self.arrived_date = time.strftime("%d/%m/%Y")
        self.adopted_date = ''

    def set_adopted_date(self, date: str):
        '''
        sets the day the animal was adopted.
        date: (str) date in "%d/%m/%Y" format
        '''
        self.adopted_date = date
        
    def __str__(self) -> str:
        return 'name: ' + self.name +\
            ', type: ' + self.type +\
            ', arrived: ' + self.arrived_date +\
            ', adopted: ' + self.adopted_date
