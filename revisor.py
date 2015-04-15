import re
import glob

metadata = []
questions = {}
solutions = {}

def main():
    for filename in glob.glob("Q*.md"):
        with open(filename, "r") as lines:
            #lines = f.readlines()
            is_answer = False
            question = ""
            previous_line = ""
            question_count = 0
            next_line = ""
            whole = ""
            section = ""
            topic = ""
            section_match_pattern = r'(^#\s+)(\w+)\s*'
            topic_match_pattern = r'(^##\s+)(\w+)\s*'
            question_match_pattern = r'(^\d\.\s+)(.*)' 
            
            for line in lines:
                
                start = 0
                
                # elif line is question, inc count, grab line
                question_match = re.match(question_match_pattern, line)
                while (question_match):
                    question = question_match.group(2) + "\n"
                    try:
                        line = next(lines)
                    except StopIteration:
                        line = ""
                    while (line and 
                        not(re.match(question_match_pattern, line) or 
                            re.match(topic_match_pattern, line) or
                            re.match(section_match_pattern, line))):
                        question += line
                        try:
                            line = next(lines)
                        except StopIteration:
                            line = ""
                    print question
                    question_match = re.match(question_match_pattern, line)

                # if line is heading 1, grab value 
                section_match = re.match(section_match_pattern, line)
                if (section_match):
                    section = section_match.group(2).lower()
                    print section
                
                # elif line is heading 2, grab value
                topic_match = re.match(topic_match_pattern, line)
                if (topic_match):
                    topic = topic_match.group(2).lower()
                    print topic
                       


            print
            print metadata
            print
            print questions
            print
            print solutions
            print

                #if (is_section_markdown(next_line)):
                #    isAnswer = (line.lower == "answer")
                #    i += 1
            
                #elif (is_topic_markdown(next_line)):
                #    print "THAT'S IT"
                #    topic = line
                #    questionCount = 0
                #    i += 1
        
                #elif (bool(is_question(line))):
                #    print str(questionCount) + " " + question
                #    question = line
                #    questionCount += 1
    
                #elif (is_not_heading_markdown(line) and is_not_heading_markdown(next_line)):
                #    question += line

                #else:
                #    print "DISCARDED?: " + line



def is_section_markdown(s):
    return s.startswith("===")

def is_topic_markdown(s):
    return s.startswith("---")

def is_question(s):
    return re.match('^\d*\.', s)

def is_not_heading_markdown(s):
    return not re.match('-|=', s)


if __name__ == '__main__':
    main()


########## Tests ##########


def test_is_section_markdown_true():
    assert is_section_markdown("===============") == True

def test_is_section_markdown_false():
    assert is_section_markdown("aaaaaaaaaaaaaaa") == False

def test_is_topic_markdown_true():
    assert is_topic_markdown("-----------------") == True

def test_is_topic_markdown_false():
    assert is_topic_markdown("aaaaaaaaaaaaaaaaa") == False

def test_is_question_true():
    assert bool(is_question("5. important question?")) == True

def test_is_question_multi_true():
    assert bool(is_question("34. important question?")) == True

def test_is_question_false():
    assert bool(is_question("x. not a question")) == False

def test_is_not_heading_markdown_true():
    assert is_not_heading_markdown("asdasd") == True

def test_is_not_heading_markdown_false():
    assert is_not_heading_markdown("=======") == False
