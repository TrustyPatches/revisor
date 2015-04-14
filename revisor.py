import re
import glob

metadata = []
questions = {}
solutions = {}

def do_nothing():
    a = 2 * 2

def main():
    for filename in glob.glob("Q*.md"):
        with open(filename, "r") as f:
            lines = f.readlines()
            is_answer = False
            question = ""
            previous_line = ""
            question_count = 0
            next_line = ""
            whole = ""
            topic = ""

            i = 0
            while (i < len(lines) - 1):
                line = lines[i]
                next_line = lines[i + 1]

                if (is_section_markdown(next_line)):
                    is_answer = (line.lower == "answer")
                    i += 2
                elif (is_topic_markdown(next_line)):
                    if (not is_answer and topic): 
                        metadata.append((filename, topic, question_count))
                    topic = line
                    question_count = 0
                    i += 2
                elif (bool(is_question(line)) and question):
                    if (not is_answer):
                        questions[(filename, topic, question_count)] = (question)
                    else:
                        solutions[(filename, topic, question_count)] = (question)
                    question = line
                    i += 1
                else:
                    question += line
                    i += 1
            solutions[(filename, topic, question_count)] = (question)
            
            print metadata 
            print questions
            print solutions

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
