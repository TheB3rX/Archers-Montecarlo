import random

class Archer:
    # Maxium endurance for an archer
    max_endurance= 0
    # Gender of an archer
    gender = 0
    # Individual archer score, defaults with 0
    individual_score = 0
    # Represents current archer endurance
    endurance = 0
    # Exp of an archer, defaults in 10
    EXP = 10
    # Luck is a value between 1 to 3
    luck = 0
    first_lucky_round = None
    second_lucky_round = None
    last_lucky_round = None
    endurance_bonus_round_activated = None

    def __init__(self):
        # Start a random number
        num = random.random()

        # If the number is equal or less than 0.5, the archer is going to be male
        if num <= 0.5:
            self.gender = 0
        # If the number is greater than 0.5, the archer is going to be female 
        elif num > 0.5:
            self.gender = 1

        # If the number less than 0.5 gets a value between 36 to 45
        if num < 0.5:
            self.endurance = 35 + random.randint(1, 10)
        # If the number greater than 0.5 gets a value between 25 to to 34
        else:
            self.endurance = 35 - random.randint(1, 10)

        # If the number greater than 0.5 gets a value between 25 to to 34
        if num <= 0.3:
            self.luck = 1
        # If the number greater than 0.5 gets a value between 25 to to 34
        elif 0.3 < num <= 0.66:
            self.luck = 2
        # If the number greater than 0.5 gets a value between 25 to to 34
        else:
            self.luck = 3
        self.max_endurance = self.endurance

    # Adds score for an archer
    def setIndividualScore(self, score):
        self.individual_score += score

    # Sets the endurance of the Archer from the attribute max_endurance 
    def resetEndurance(self):
        self.endurance = self.max_endurance

    # Recalculates the luck of 
    def recalculateLuck(self):
        self.luck = random.uniform(1, 3)
