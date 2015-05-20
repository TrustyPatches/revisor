import re
import glob

def main():
    print("It's all okay")
    sc = SheetCreator()
    print(sc.filenames)

class SheetCreator:

    BLACKLIST = ["README.md"]

    def __init__(self):
        self.filenames = self.get_filenames()

    def get_filenames(self):
        filenames = []
        for filename in glob.glob("*.md"):
            if (filename not in self.BLACKLIST):
                filenames.append(filename)
        return filenames

class Sheet:
    def __init__(self, title):
        self.title = title
        self.topics = []
        
class Topic:
    def __init__(self, title):
        self.title = title
        self.qa_pairs = []

class QAPair:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

if __name__ == '__main__':
    main()

### TESTS ###
