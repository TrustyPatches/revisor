import re
import glob

def main():
    print("It's all okay")

class Sheet:
    def __init__(self, title):
        self.title = title
        self.topics = []
        
class Topic:
    def __init__(self, title):
        self.title = title
        self.qaPairs = []

class QAPair:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

if __name__ == '__main__':
    main()

### TESTS ###
