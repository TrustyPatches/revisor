import re
import glob

metadata = []
questions = {}
solutions = {}

def main():
    for filename in glob.glob("Q*.md"):
        with open(filename, "r") as lines:
            section = ""
            topic = ""
            question = ""
            question_count = 0
            section_match_pattern = r'(^#\s+)(\w+)(.*)'
            topic_match_pattern = r'(^##\s+)([\w+\s*]*)'
            # TODO question variables should be renamed b/c apply to answers too
            question_match_pattern = r'(^\d\.\s+)(.*)'  
            
            for line in lines:
                
                # elif line is question, inc count, grab line
                question_match = re.match(question_match_pattern, line)
                while (question_match):
                    question = question_match.group(2) + "\n"
                    question_count += 1
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
                    # if question, add to questions
                    if (section.lower().startswith("question")):
                        questions[(filename, topic, question_count)] = question
    
                    # if answer, add to solutions
                    if (section.lower().startswith("solution")):
                        solutions[(filename, topic, question_count)] = question

                    question_match = re.match(question_match_pattern, line)
                    if (not question_match and section.startswith("question")):
                        metadata.append((filename, topic, question_count))
                
                # if line is heading 1, grab value 
                section_match = re.match(section_match_pattern, line)
                if (section_match):
                    section = section_match.group(2).lower()
                    print section
                
                # elif line is heading 2, grab value
                topic_match = re.match(topic_match_pattern, line)
                if (topic_match):
                    topic = topic_match.group(2).lower()
                    question_count = 0
                    print topic
                


            print
            print metadata
            print
            print questions
            print
            print solutions
            print



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
