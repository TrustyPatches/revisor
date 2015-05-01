import re
import glob

# TODO  metadata should be created and maintained as a sorted array 
# with the structure m[0] = (topic, subtopic, count), etc (probably)
# that way it can replace temp_menu
metadata = []
questions = {}
solutions = {}
temp_menu = []

def main():
    loadFiles()
    printTitle()
    displayTopics()

    print "\nPlease select a topic: "

    response = int(raw_input()) - 1
    topic = temp_menu[response][0]
    key = temp_menu[response][1]
    print key
    
    # this sucks, should be dict or better
    for i in metadata:
        if (i[1] == key):
            count = i[2]
    
    # In fact this is all terrible, but main concept here
    for i in range(1, count + 1):
        print "\nQuestion " + str(i) + ":"
        print questions[(topic, key, i)]
        raw_input()

    for i in range(1, count + 1):
        print "\nAnswer " + str(i) + ":"
        print solutions[(topic, key, i)]
        raw_input()


def displayTopics():
    #print questions
    print solutions

    print "\nLoaded topics:\n"
    for i in range(0, len(metadata)):
        temp_menu.append((metadata[i][0], metadata[i][1]))
        print "     " + str(i + 1) + ". " + metadata[i][0] + "/ " + metadata[i][1] 
    

def loadFiles():
    for filename in glob.glob("*.md"):
        with open(filename, "r") as lines:
            section = ""
            topic = ""
            subtopic = ""
            question = ""
            question_count = 0
            topic_match_pattern = r'(^#\s+)([\w+\s*]*)'
            section_match_pattern = r'(^##\s+)(\w+)(.*)'
            subtopic_match_pattern = r'(^###\s+)([\w+\s*]*)'
            # TODO question variables should be renamed b/c apply to answers too
            question_match_pattern = r'(^\d*\.\s+)(.*)'  
            
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
                            re.match(subtopic_match_pattern, line) or
                            re.match(topic_match_pattern, line) or
                            re.match(section_match_pattern, line))):
                        question += line
                        try:
                            line = next(lines)
                        except StopIteration:
                            line = ""
                    
                    # if question, add to questions
                    if (section.lower().startswith("question")):
                        questions[(topic, subtopic, question_count)] = question
    
                    # if answer, add to solutions
                    if (section.lower().startswith("solution")):
                        solutions[(topic, subtopic, question_count)] = question

                    # if not a question or answer must be end of subtopic
                    question_match = re.match(question_match_pattern, line)
                    if (not question_match and section.lower().startswith("question")):
                        metadata.append((topic, subtopic, question_count))
              
                # if line is topic heading, grab value
                topic_match = re.match(topic_match_pattern, line)
                if (topic_match):
                    topic = topic_match.group(2).lower().rstrip('\n')

                # if line is section heading, grab value
                section_match = re.match(section_match_pattern, line)
                if (section_match):
                    section = section_match.group(2).lower().rstrip('\n')
                
                # elif line is subtopic heading, grab value
                subtopic_match = re.match(subtopic_match_pattern, line)
                if (subtopic_match):
                    subtopic = subtopic_match.group(2).lower().rstrip('\n')
                    question_count = 0


def printTitle():
    print
    print "     /===============\\"
    print "     | R E V I S O R | "
    print "     \\===============/"
    print

def printDictionaries():
    print
    print metadata
    print
    print questions
    print
    print solutions
    print
    for q in questions: print questions[q]
    print
    for a in solutions: print solutions[a]


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
