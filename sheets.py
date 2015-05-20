import re
import glob

def main():
    print("It's all okay")
    sl = SheetLibrary()
    print(sl.filenames)

class SheetLibrary:

    BLACKLIST = ["README.md"]

    def __init__(self):
        self.filenames = self.get_filenames()
        self.sheets = self.create_sheets()

    def get_filenames(self):
        filenames = []
        for filename in glob.glob("*.md"):
            if (filename not in self.BLACKLIST):
                filenames.append(filename)
        return filenames

    def create_sheets(self):
        sheets = []
        for f in self.filenames:
            sheet = Sheet(f)
            sheets.append(sheet)
        return sheets

class Sheet:
    def __init__(self, filename):
        self.title = filename
        self.topics = self.create_topics(filename)
        
    def create_topics(self, filename):
        topics = []

        return topics

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
