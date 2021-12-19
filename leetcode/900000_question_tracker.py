import os
import collections

class QuestionTracker:
    def __init__(self):
        self.questions_list = []

    def get_file_names(self):
        # Get python files
        python_files = [x for x in os.listdir("./leetcode") if x.endswith(".py")]

        # Sort by question num
        master = collections.defaultdict(str)
        for i in python_files:
            num = int(i.split('_')[0])
            master[num] += i

        sorted_questions = dict(sorted(master.items(), key=lambda item: item[0]))
        self.questions_list = list(sorted_questions.values())
        return self.questions_list
        
    def convert_format(self, q_list):
        # Link relative path
        q_list = ['[' + i + ']' + '({})'.format(i)  for i in q_list]
        # Add to table and default checkbox
        self.questions_list = ['|' + i + '|'+ '[x]' + '|' + '|' + '|' + '\n' for i in q_list]
        return self.questions_list

    def write_to_markdown(self, q_list):
        # Export it to markdown, convert to table
        markdown = open('./leetcode/readme.md', 'w')
        markdown.write("## Leetcode Python Questions Solved\n")
        markdown.write("|Question| Attempt 1| Attempt 2|Attempt 3|")
        markdown.write("\n")
        markdown.write("|---|---|---|---|")
        markdown.write("\n")
        markdown.writelines(q_list)
        markdown.write("\n")
        markdown.write("Total: {} questions".format(len(q_list)))
        print('Markdown export success')


### Driver code
q = QuestionTracker()
q_list = q.get_file_names()
converted_list = q.convert_format(q_list)
q.write_to_markdown(converted_list)

