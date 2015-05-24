import re
import sys
import yaml
import glob

if sys.version_info[0] >= 3:
    get_input = input
else:
    get_input = raw_input


###################################### MAIN ###################################### 

#TODO Most of this should be refactored into another class specifically for 
# displaying, constructing and looping the menu

def main():
    """Entry point for the command-line program, start up menu system """
    print("It's all okay")

    cm = ConsoleMenu()
    cm.enter_menu()

###################################### MENU ######################################

class ConsoleMenu:
    """Holds the logic for guiding a user through a console based session."""
    
    def enter_menu(self):
        self.print_title()
        sl = SheetLibrary()

        while True:
            print("Select an option:\n")
            print("\t1. Generate mock test [not implemented]")
            print("\t2. Browse sheets")
            self.print_alt_menu(0)
            selection = get_input()[0]

            if (selection in "Qq"): 
                exit(0)
            if (selection == '1'):
                self.generate_test()
            if (selection == '2'):
                self.browse_sheets()
        
    def browse_sheets(self):
        sl = SheetLibrary()

        print ("Please select a sheet number:\n")

        for i in range(len(sl.get_sheet_titles())):
            print("\t" + str(i + 1) + ". " + sl.get_sheet_titles()[i])

        self.print_alt_menu(1)

        selection = get_input()[0]
        if (selection in "Qq"): exit(0)
        if (selection in "Bb"): return
        selected_sheet = sl.sheets[int(selection) - 1]

        self.browse_topics(selected_sheet)

    def browse_topics(self, selected_sheet):
        print ("Please select a topic number:\n")

        for i in range(len(selected_sheet.get_topics_titles())):
            print("\t" + str(i + 1) + ". " + selected_sheet.get_topics_titles()[i])

        self.print_alt_menu(1)

        selection = get_input()[0]
        if (selection in "Qq"): exit(0)
        if (selection in "Bb"): return
        selected_topic = selected_sheet.topics[int(selection) - 1]

        self.cycle_topic_questions(selected_topic)

    def cycle_topic_questions(self, selected_topic):
        for qa in selected_topic.qa_pairs:
            print("\n" + "".join(qa.question))
            command = get_input("...")
            if (command == "Q" or command == "q"): exit(0)
        get_input("That's all the questions. Ready for the answers now..?\n")
        for qa in selected_topic.qa_pairs:
            print("".join(qa.answer))
            command = get_input()
            if (command == "Q" or command == "q"): exit(0)
        print("")

    def generate_test(self):
        print("Not implemented")

    def print_alt_menu(self, mode):
        if (mode == 0): print("\nq: Quit")
        if (mode == 1): print("\nq: Quit | b: Back")

    def old_menu(self):
        self.printTitle()
        sl = SheetLibrary()
   
        print("Please select a sheet number:\n")
    
        for i in range(len(sl.get_sheet_titles())):
            print("     " + str(i + 1) + ". " + sl.get_sheet_titles()[i])

        selected_sheet = sl.sheets[int(get_input()) - 1]
    
        for i in range(len(selected_sheet.get_topics_titles())):
            print("     " + str(i + 1) + ". " + selected_sheet.get_topics_titles()[i])

        selected_topic = selected_sheet.topics[int(get_input()) - 1]

        for qa in selected_topic.qa_pairs:
            print("\n" + "".join(qa.question))
            command = get_input("...") 
            if (command == "q" or command == "Q"): exit(0)
    
        get_input("That's all the questions. Ready for the answers now..?\n")
        for qa in selected_topic.qa_pairs:
            print("".join(qa.answer))
            command = get_input()
            if (command == "q" or command == "Q"): exit(0)
    
        print("")
    
    def print_title(self):
        """Print some funky ASCII title graphics"""
        print("")
        print("         /=================\\")
        print("         |   S H E E T S   | ")
        print("         \\=================/")
        print("")
    

################################## SHEET LIBRARY #################################

class SheetLibrary:
    """Holds a collection of sheets generated from local markdown files"""
    def __init__(self):
        self.filenames = self.get_filenames()
        self.sheets = self.create_sheets()

    def get_filenames(self):
        config = yaml.load(open(".config.yml", 'r'))
        pathnames = config["sheetspath"]
        blacklistnames = config["blacklist"]
        filenames = []
        for path in pathnames:
            directory = path + "/*.md"
            for filename in glob.glob(directory):
                if (filename not in blacklistnames):
                    filenames.append(path + "/" + filename)
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


###################################### SHEET ###################################### 

class Sheet:
    """Represents a single sheet of question and answers pairs, divided into topics"""
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
        topics_section.append(topic)
        return topics_section

###################################### TOPIC ##################################### 

class Topic:
    """Represents a single topic filled with related question answer pairs"""
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
        qa_group.append(qa)
        return qa_group

##################################### QA PAIR ####################################

class QAPair:
    """A single question answer pair containing all appropriate data"""
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

if __name__ == '__main__':
    main()


##################################### TESTS ######################################
