from src.bots.bot import Bot

new=["2","2","2","2","2","2","2","2","2","2","2","2","2"]

class LearnBot(Bot):

    def __init__(self):
        super().__init__("Bot", new, new, new, new)