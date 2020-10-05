import random
from collections import deque
s = open("rating.txt", "w")
s.write("Tim 350\nJane 200\nAlex 400\n")
s.close()


class RockPaperScissors:
    def __init__(self):
        self.score = 0
        self.our_rating = {}
        self.win = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
        self.name = ""
        self.winn = []
        self.lose = []
        self.winn1 = []
        
    def greetings(self):
        self.name = input("Enter your name: ")
        print("Hello,", self.name)
        options = input()
        print("Okay, let's start")
        if options == "":
            self.default_game()
        else:
            self.more_options(options.split(","))
        
        
    def more_options(self, options):
        while True:
            option = random.choice(options)
            choose = input()
            if choose in options:
                choose_in_list = options.index(choose)
                items = deque(options)
                items.rotate(-choose_in_list)
                items.popleft()
                self.winn = list(items)
                self.winn1 = self.winn[len(self.winn) // 2:]
                self.lose = self.winn[:len(self.winn) // 2]
                if self.winn1.count(option) > 0:
                    self.score += 100
                    print(f"Well done. The computer chose {option} and failed")
                elif choose == option:
                    self.score += 50
                    print(f"There is a draw ({option})")
                else:
                    print(f"Sorry, but the computer chose {option}")
            if choose == "!exit":
                print("Bye!")
                break
            elif choose == "!rating":
                rating = open("rating.txt", "r")
                for line in rating:
                    k, v = line.strip().split(" ")
                    self.our_rating[k.strip()] = int(v.strip())
                if self.name in self.our_rating:
                    start_score = self.our_rating[self.name]
                    print("Your rating:", self.score + start_score)
                else:
                    print("Your rating:", self.score)
                rating.close()
            elif choose not in options:
                print("Invalid input")
            
        
    
    def default_game(self):
        while True:
            option = random.choice(["scissors", "paper", "rock"]) 
            choose = input()
            if choose == "!exit":
                print("Bye!")
                break
            elif choose == "!rating":
                rating = open("rating.txt", "r")
                for line in rating:
                    k, v = line.strip().split(" ")
                    self.our_rating[k.strip()] = int(v.strip())
                if self.name in self.our_rating:
                    start_score = self.our_rating[self.name]
                    print("Your rating:", self.score + start_score)
                else:
                    print("Your rating:", self.score)
                rating.close()
            elif choose not in self.win:
                print("Invalid input")
            elif self.win[choose] == option:
                self.score += 100
                print(f"Well done. The computer chose {option} and failed")
            elif choose == option:
                self.score += 50
                print(f"There is a draw ({option})")
            elif self.win[option] == choose:
                print(f"Sorry, but the computer chose {option}")

    
    
        
game = RockPaperScissors()
game.greetings()
