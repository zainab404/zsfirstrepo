import sys

class Girl:
    age = 21
    career = "Software Engineer"
    favorite_movies = ["Wolf of Wall Street", "American Psycho", "Rough Night"]
    boyfriend = "Guillermo"
    
    def gaming(self, game):
        play_choice = input("Would you like to play video games?")
        while play_choice.lower == "Yes":
            print("Here {}".format(game))
        sys.exit
