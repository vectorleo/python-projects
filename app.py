
def logtime(func):
    def wrapper():
      print("before")
      val = func()
      print("after")
      return val
    return wrapper

 
@logtime
def hello():
    print("hello")
  

hello()








    def calulate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank["value"]) 
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def is_blackjack(self):
        return self.get_value() == 21

    def get_value(self):
        self.calulate_value()
        return self.value   
    

    def display(self):
        print(f'''{"Dealer's" if self.dealer else "your"}hand''')
        for card in self.cards :
            print(card)
        
        if not self.dealer:
            print("value: ",self.get_value())
        print()
        
