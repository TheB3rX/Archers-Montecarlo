from colorama import init, Fore, Back, Style  # Importing necessary modules for color formatting
from prettytable import PrettyTable  # Importing PrettyTable for displaying tabular data
from Team import Team  # Importing the Team class from a custom module
import random  # Importing the random module for generating random numbers
import matplotlib.pyplot as plt  # Importing matplotlib for plotting graphs

# Start the archers game
def initGame(teamOne, teamTwo):
    # Initializes the archery game between two teams.
    init()  # Initialize colorama for colored output
    table = PrettyTable()  # Create a PrettyTable for displaying game scores
    table.field_names = [Fore.RED+"Team", Fore.GREEN+"Score", Fore.BLUE+"Luckiest Player", Fore.YELLOW+"Most Experienced Player"]  # Set table headers with colored text
    games = 1000  # Number of games to be played

    # Loop until all games are played
    while games > 0:
        resetEndurance(teamOne, teamTwo)  # Reset endurance of all players before each game
        initRounds(teamOne, teamTwo)  # Start the rounds of the game
        games -= 1  # Decrement games count after each game

    # Get the luckiest player and the player who gained the most experience in the current game
    luckiest_player_team1, luck_score_team1 = teamOne.extraShotDraw()
    most_experienced_player_team1 = max(teamOne, key=lambda x: x.EXP)

    luckiest_player_team2, luck_score_team2 = teamTwo.extraShotDraw()
    most_experienced_player_team2 = max(teamTwo, key=lambda x: x.EXP)

    # Add final scores of both teams to the table
    table.add_row([teamOne.name, teamOne.teamScore, f"{luckiest_player_team1.luck} ({luck_score_team1})", most_experienced_player_team1.EXP])
    table.add_row([teamTwo.name, teamTwo.teamScore, f"{luckiest_player_team2.luck} ({luck_score_team2})", most_experienced_player_team2.EXP])
    
    # Display gender-wise score comparison for each team
    showTableGenderScore(teamOne, 'Team 1')
    showTableGenderScore(teamTwo, 'Team 2')
    
    # Display the winning team and their scores
    showWinTeam(teamOne, teamTwo)
    
    # Print the final scores table
    print(table)

# Shooting simulation for each player
def shootingPlayers(archer, team):
    # Simulates shooting for each player in a team.
    table = PrettyTable()  # Create a PrettyTable for displaying shooting details
    endurance = archer.endurance  # Get the endurance of the archer
    table.field_names = [Fore.RED+"Endurance", Fore.GREEN+"Score", "Gender"]  # Set table headers with colored text
    playerScore = 0  # Initialize player's score to 0

    # Loop until the endurance of the archer is greater than 5
    while endurance > 5:
        playerScore += takeShot(archer)  # Take a shot and update player's score
        endurance -= 5  # Decrease endurance after each shot by 5
    table.add_row([archer.endurance, playerScore, "Female" if archer.gender == 1 else "Male"])  # Add shooting details to the table

    # Reduce endurance randomly by 1 or 2 after each round
    if random.random() < 0.5:
        archer.endurance -= 2
    else:
        archer.endurance -= 1
    
    # Update individual score of the archer and team score
    archer.setIndividualScore(playerScore)
    team.updateTeamScore(playerScore)
    
    # Print shooting details table
    print(table)

# Take a shot for an archer
def takeShot(archer):
    # Simulates taking a shot for an archer and returns the score.
    shot = random.random()  # Generate a random number between 0 and 1
    if archer.gender == 0:  # If the archer is male
        # Assign score based on shot probability
        if shot <= 0.2:
            return 10
        elif 0.2 < shot <= 0.53:
            return 9
        elif 0.53 < shot <= 0.93:
            return 8
        else:
            return 0
    elif archer.gender == 1:  # If the archer is female
        # Assign score based on shot probability
        if shot <= 0.3:
            return 10
        elif 0.3 < shot <= 0.68:
            return 9
        elif 0.68 < shot <= 0.95:
            return 8
        else:
            return 0

# Initialize rounds between teams
def initRounds(teamOne, teamTwo):
    # Initiates rounds of shooting between two teams.
    cycle = 10  # Number of rounds
    while cycle > 0:
        for archer in teamOne:
            shootingPlayers(archer, teamOne)  # Perform shooting for each player in teamOne
            print("==========Team One==========")
        for archer in teamTwo:
            shootingPlayers(archer, teamTwo)  # Perform shooting for each player in teamTwo
            print("==========Team Two==========")
        extraShotDraw(teamOne)  # Perform extra shot draw for teamOne
        extraShotDraw(teamTwo)  # Perform extra shot draw for teamTwo
        cycle -= 1  # Decrement cycle count after each round

# Reset endurance of all players in both teams
def resetEndurance(team1, team2):
    # Resets endurance of all players in both teams.
    for archer in team1:
        archer.resetEndurance()  # Reset endurance for each player in team1
    for archer in team2:
        archer.resetEndurance()  # Reset endurance for each player in team2

# Perform an extra shot for the luckiest archer in a team
def extraShotDraw(team):
    # Performs an extra shot for the luckiest archer in a team.
    maxLuck = 0  # Initialize maximum luck to 0
    luckiestArcher = None  # Initialize luckiest archer to None
    for archer in team:
        if archer.luck > maxLuck:
            maxLuck = archer.luck  # Update maximum luck if luck of the archer is greater
            luckiestArcher = archer  # Update luckiest archer
    team.updateTeamScore(takeShot(luckiestArcher))  # Update team score with an extra shot for the luckiest archer

# Show gender-wise score comparison for a team
def showTableGenderScore(archers, teamName):
    # Displays gender-wise score comparison for a team.
    score_men = []
    score_women = []
    total_women = 0
    total_men = 0

    for archer in archers:
        if archer.gender == 1:
            score_men.append(archer.individual_score)
            total_men += 1
        else:
            score_women.append(archer.individual_score)
            total_women += 1

        categories = [f"Women ({total_women})", f"Men ({total_men})"]

        if len(score_women) > 0:
            average_women = sum(score_women) / len(score_women)
        else:
            average_women = 0

        if len(score_men) > 0:
            average_men = sum(score_men) / len(score_men)
        else:
            average_men = 0 

        heights = [average_women, average_men]

    plt.figure(figsize=(8, 6))
    plt.bar(categories, heights, color=['pink', 'blue'])
    plt.title(f'Average Score by Gender - {teamName}')
    plt.xlabel('Gender')
    plt.ylabel('Average Score')
    plt.show()

# Show winning team
def showWinTeam(team1, team2):
    # Displays the winning team and their scores.
    plt.bar([team1.name, team2.name], [team1.teamScore, team2.teamScore], color=['red', 'blue'])
    plt.title('Team Scores')
    plt.xlabel('Teams')
    plt.ylabel('Score')

    women_team1 = sum(1 for archer in team1 if archer.gender == 0)
    men_team1 = sum(1 for archer in team1 if archer.gender == 1)
    women_team2 = sum(1 for archer in team2 if archer.gender == 0)
    men_team2 = sum(1 for archer in team2 if archer.gender == 1)

    print(f"{team1.name}: Women: {women_team1}, Men: {men_team1}")
    print(f"{team2.name}: Women: {women_team2}, Men: {men_team2}")

    plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))

    plt.tight_layout()
    plt.show()

# Initialize team instances
teamOneInit = Team("Team 1")
teamTwoInit = Team("Team 2")

# Start the archery game
initGame(teamOneInit, teamTwoInit)
