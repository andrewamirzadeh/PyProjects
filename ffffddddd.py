#Author Name: Bijan Amirzadehasl
#Date: 11/1/2021
#Program Name: Amirzadehasl_Player.py
#Purpose: Create a player class. Create and store three player objects. Display the attributes of the three players

#player class
class Player:
    def __init__(self, name, team, position, age, gp, mpg):
        self.name = name
        self.team = team
        self.position = position
        self.age = age
        self.gp = gp
        self.mpg = mpg

def main():
    #three player objects
    p1 = Player('Jaylen Adams', 'Mil', 'G', 24.86, 7, 2.6)
    p2 = Player('Steven Adams', 'Nor', 'C', 27.65, 36, 27.4)
    p3 = Player('Bam Adebayo', 'Mia', 'C-F', 23.66, 33, 33.9)

#formatted output displaying player's attributes
    print("{:<15} {:<12} {:<12} {:<12} {:<12} {:<12}".format('Name', 'Team', 'Position', 'Age', 'GP', 'MPG'))
    print("{:<15} {:<12} {:<12} {:<12} {:<12} {:<12}".format(p1.name, p1.team, p1.position, p1.age, p1.gp, p1.mpg))
    print("{:<15} {:<12} {:<12} {:<12} {:<12} {:<12}".format(p2.name, p2.team, p2.position, p2.age, p2.gp, p2.mpg))
    print("{:<15} {:<12} {:<12} {:<12} {:<12} {:<12}".format(p3.name, p3.team, p3.position, p3.age, p3.gp, p3.mpg))



main()


