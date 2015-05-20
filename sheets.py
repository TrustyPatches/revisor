import re
import sys
import glob

if sys.version_info[0] >= 3:
    get_input = input
else:
    get_input = raw_input

def main():
    print("It's all okay")
    printTitle()
    sl = SheetLibrary()
   
    print("Please select a sheet number:\n")
    
    for i in range(len(sl.get_sheet_titles())):
        print("     " + str(i + 1) + ". " + sl.get_sheet_titles()[i])

    selected_sheet = sl.sheets[int(get_input()) - 1]
     
    for i in range(len(selected_sheet.get_topics_titles())):
        print("     " + str(i + 1) + ". " + selected_sheet.get_topics_titles()[i])

    selected_topic = selected_sheet.topics[int(get_input()) - 1]

    for qa in selected_topic.qa_pairs:
        print("".join(qa.question))
        get_input("...") 

    get_input("That's all the questions. Ready for the answers now..?\n")

    for qa in selected_topic.qa_pairs:
        print("".join(qa.answer))
        get_input()

    print("")

def printTitle():
    print("")
    print("         /=================\\")
    print("         |   S H E E T S   | ")
    print("         \\=================/")
    print("")

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
            sheet = Sheet(title, questions, answers)
            sheets.append(sheet)
        return sheets

    def get_sheet_titles(self):
        sheet_titles = []
        for s in self.sheets:
            sheet_titles.append(s.title)
        return sheet_titles

    def grab_title(self, line):
        title_match_pattern = r'(^#\s+)([\w+\s*]*)'
        title_match = re.match(title_match_pattern, line)
        return title_match.group(2).rstrip('\n') if (title_match) else ""
    
    def set_section(self, section, line):
        section_match_pattern = r'(^##\s+)([\w+\s*]*)'
        section_match = re.match(section_match_pattern, line)
        return section_match.group(2).lower().rstrip('\n').rstrip(' ') if (section_match) else section


class Sheet:
    def __init__(self, title, questions, answers):
        self.title = title
        self.topics = self.create_topics(questions, answers)
        
    def create_topics(self, questions, answers):
        topics = []
        topics_questions = self.create_topics_raw(questions)
        topics_answers = self.create_topics_raw(answers)
        if (len(topics_questions) != len(topics_answers)):
            # TODO This error message should be more verbose if possible
            print("Error: Number of questions doesn't match number of answers.")
            exit()
        else: 
            topics_count = len(topics_questions)
        for i in range(topics_count):
            new_topic = Topic(topics_questions[i], topics_answers[i])
            topics.append(new_topic)
        
        return topics


    def get_topics_titles(self):
        topic_titles = []
        for t in self.topics:
            topic_titles.append(t.title)
        return topic_titles

    def create_topics_raw(self, section):       
        topic_match_pattern = r'(^###\s+)([\w+\s*]*)'
        section_match_pattern = r'(^##\s+)([\w+\s*]*)'
        topic = []
        topics_section = []
        for line in section:
            if (topic and re.match(topic_match_pattern, line)):
                topics_section.append(topic)
                topic = []
            if (not re.match(section_match_pattern, line) and
                not re.match(r'(\s*\n+\s*)', line)):
                topic.append(line)
        print(topics_section)
        return topics_section

class Topic:
    def __init__(self, questions, answers):
        self.title = self.grab_title(questions)
        self.qa_pairs = self.create_qa_pairs(questions, answers)

    def grab_title(self, questions): 
        topic_match_pattern = r'(^###\s+)([\w+\s*]*)'
        for line in questions:
            title_match = re.match(topic_match_pattern, line)
            if (title_match):
                return title_match.group(2).rstrip('\n').rstrip(' ')
        return "Untitled"

    def create_qa_pairs(self, questions, answers):
        qa_questions = self.divide_qa(questions)
        qa_answers = self.divide_qa(answers)
        if (len(qa_questions) != len(qa_answers)):
            # TODO This error message should be more verbose if possible
            print("Error: Number of questions doesn't match number of answers.")
            exit()
        else: 
            qa_count = len(qa_questions)

        qa_pairs = []
        for i in range(qa_count):
            qa = QAPair(qa_questions[i], qa_answers[i])
            qa_pairs.append(qa)
        return qa_pairs

    def divide_qa(self, group):
        qa_match_pattern = r'(^\d*\.\s+)(.*)'
        qa_group = []
        qa = []
        for line in group[1:]:
            if (qa and re.match(qa_match_pattern, line)):
                qa_group.append(qa)
                qa = []     
            if (not re.match(r'(\s*\n+\s*)', line)):
                qa.append(line)
        return qa_group

class QAPair:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

if __name__ == '__main__':
    main()

### TESTS ###
