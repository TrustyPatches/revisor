import re
import glob

def main():
    print("It's all okay")
    

class SheetGenerator:
    def __init__(self):
        markdown_filenames = get_markdown_filenames()

    def get_markdown_filenames():
        filenames = []
        for filename in glob.glob("*.md")
            filenames += filename
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
