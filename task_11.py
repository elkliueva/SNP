class Dessert():

    def __init__(self, name = None, calories = None):
        self.name = name
        self.calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise ValueError("Calories must be a number or None")
        self._calories = value

    def is_healthy(self):
        return self.calories is not None and self.calories < 200
    
    def is_delicious(self):
        return True
