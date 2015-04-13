import re
import glob

metadata = {}
questions = {}
solutions = {}

def main():
    for filename in glob.glob("*.md"):
        with open(filename, "r") as f:
            lines = f.readlines()
            isAnswer = False
            question = ""
            previous_line = ""
            questionCount = 0
            next_line = ""
        
            for i in range(0, len(lines)):
                line = lines[i]

                if (is_section_markdown(next_line)):
                    isAnswer = line.lower == "answer"
            
                elif (is_topic_markdown(next_line)):
                    topic = line
                    questionCount = 0
        
                elif (is_question(line)):
                    print question
                    print line
                    question = line
                    questionCount += 1
    
                elif (is_not_heading_markdown(line)):
                    print line
                    question += line
                else:
                    print "DISCARDED?: " + line

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
