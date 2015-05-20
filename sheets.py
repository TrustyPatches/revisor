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
            title = ""
            section = ""
            questions = []
            answers = []
            with open(f, "r") as lines:
                for line in lines:
                    section = self.set_section(section, line)
                    if (section == "questions"):
                        questions.append(line)
                    if (section == "answers"):
                        answers.append(line)
                    if (title == ""): 
                        title = self.grab_title(line)
                print (questions)
                print (answers)
            sheet = Sheet(title, questions, answers)
            sheets.append(sheet)
        return sheets

    def grab_title(self, line):
        title_match_pattern = r'(^#\s+)([\w+\s*]*)'
        title_match = re.match(title_match_pattern, line)
        return title_match.group(2).lower().rstrip('\n') if (title_match) else ""
    
    def set_section(self, section, line):
        section_match_pattern = r'(^##\s+)([\w+\s*]*)'
        section_match = re.match(section_match_pattern, line)
        return section_match.group(2).lower().rstrip('\n').rstrip(' ') if (section_match) else section


class Sheet:
    def __init__(self, title, questions, answers):
        self.title = title
        self.topics = self.create_topics(questions, answers)
        
    def create_topics(self, questions, answers):
        topic = []
        topics_questions = self.create_topics_raw(questions)
        topics_answers = self.create_topics_raw(answers)
            
        return None

    def create_topics_raw(self, section):
        topic_match_pattern = r'(^##\s+)([\w+\s*]*)'
        topic = []
        topics_section = []
        for line in section:
            if (topic and re.match(topic_match_pattern, line)):
                topics_section.append(topic)
                topic = []
            topic.append(line)
        return topics_section

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
