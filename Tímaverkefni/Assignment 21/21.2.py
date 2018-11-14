class ChessPlayer:

    def __init__(self, name = "", birth_year = 0, chess_rating = 0):
        self.name = name
        self.birth_year = birth_year
        self.chess_rating = chess_rating

    def __gt__(self, other):
        return self.chess_rating > other.chess_rating

    def __str__(self):
        return "Name: {}\nYear: {}\nRating: {}\n".format(self.name, self.birth_year, self.chess_rating)

def create_players(players_list, number_of_players):
    for i in range(number_of_players):
        name  =input("Enter Name: ")
        year = int(input("Enter Year: "))
        rating  = int(input("Enter Rating: "))
        players_list.append(ChessPlayer(name, year, rating))

def get_highest_rated_player(players):
    highest_rated_player = ChessPlayer()
    for player in players:
        if player > highest_rated_player:
            highest_rated_player = player
    return highest_rated_player

def get_average_rating(players):
    rating_list = [i.chess_rating for i in players]
    return sum(rating_list)/len(rating_list)
def main():

    number_of_players = int(input("Number of players: "))
    players = []
    
    print("--- Reading players ---")
    #here you should get info from the user about 
    #number_of_players many chess player
    # code goes here....
    create_players(players, number_of_players)

    print("--- Displaying players --- ")
    #here you should print each player
    #code goes here....
    for player in players:
        print(player)

    highest_rated_player = get_highest_rated_player(players)
    print("Highest rated player: ")
    print(highest_rated_player)

    average_rating = get_average_rating(players)
    print("Average rating:", "{:.2f}".format(average_rating))

main()