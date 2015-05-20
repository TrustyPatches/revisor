import re
import glob

def main():
    print("It's all okay")
    sl = SheetLibrary()


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

    def create_topics_raw(self, section):
        topic_match_pattern = r'(^###\s+)([\w+\s*]*)'
        topic = []
        topics_section = []
        for line in section:
            if (topic and re.match(topic_match_pattern, line)):
                topics_section.append(topic)
                topic = []
            topic.append(line)
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
                return title_match.group(2).lower().rstrip('\n').rstrip(' ')
        return "Untitled"

    def create_qa_pairs(self, questions, answers):
        # Divide questions and answers into arrays of strings containing 
        # each question/answer
        # Iterate through both, creating QA_Pairs and then spitting them out 
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
            if (not re.match(r'(\s*\n\s*)', line)):
                qa.append(line)
        return qa_group

class QAPair:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

if __name__ == '__main__':
    main()

### TESTS ###
