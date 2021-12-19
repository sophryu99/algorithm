import os
import collections

# Get file names from the leetcode directory (only python files)
python_files = [x for x in os.listdir("./leetcode") if x.endswith(".py")]

# Sort by question num
master = collections.defaultdict(str)
for i in python_files:
    num = int(i.split('_')[0])
    master[num] += i

sorted_questions = dict(sorted(master.items(), key=lambda item: item[0]))
questions_list = list(sorted_questions.values())
# Link relative path
questions_list = ['[' + i + ']' + '({})'.format(i)  for i in questions_list]
# Add to table and default checkbox
questions_list = ['|' + i + '|'+ '[X]' + '|' + '|' + '|' + '\n' for i in questions_list]

# Export it to markdown, convert to table
markdown = open('./leetcode/readme.md', 'w')
markdown.write("## Leetcode Python Questions Solved\n")
markdown.write("|Question| Attempt 1| Attempt 2|Attempt 3|")
markdown.write("\n")
markdown.write("|---|---|---|---|")
markdown.write("\n")
markdown.writelines(questions_list)
