from Archer import Archer

class Team(list):
    # A class representing a team in the archery game.
    #
    # Attributes:
    #     teamScore (int): Represents the team's score.
    #     name (str): Represents the name of the team.
    teamScore = 0  # Class attribute to store the team's total score
    name = ""  # Class attribute to store the name of the team

    def __init__(self, name):
        # Initializes a team with five instances of the Archer class.
        #
        # Args:
        #     name (str): The name of the team.
        self.name = name  # Assign the team name
        self.team = [Archer() for _ in range(5)]  # Create a list of Archer instances for the team

    def updateTeamScore(self, score):
        # Updates the team's score by adding the value of 'score'.
        #
        # Args:
        #     score (int): The score to be added to the team's total score.
        self.teamScore += score  # Update the team's total score by adding the provided score

    def __iter__(self):
        # Returns an iterator over the archers in the team.
        self.index = 0  # Initialize the index for iteration
        return self  # Return the instance itself as an iterator

    def __next__(self):
        # Returns the next archer of the team in each call until the end of the list is reached,
        # at which point a StopIteration exception is raised.
        if self.index >= len(self.team):  # Check if the index exceeds the length of the team
            raise StopIteration  # Raise StopIteration exception if the end of the list is reached
        result = self.team[self.index]  # Get the archer at the current index
        self.index += 1  # Move to the next index for the next iteration
        return result  # Return the archer obtained

