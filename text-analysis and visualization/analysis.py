import os
import re
import json

cwd = os.getcwd()
file_to_work_on = []
save_file = 'topfifty.json'
word_dict = {}

for root, dirs, files in list(os.walk(cwd)):
    for file in files:
        if file.endswith('.txt'):
            file_to_work_on.append(file)

# read file to fh
# remove all stop words, and punctuation marks
# how about non ascii/that weird char?
# create dict {word: word_count}
# save to new file

# caution reading as byte
# thus either convert using decode or the method check 4 lines down
with open(os.path.join(cwd, file_to_work_on[0]), 'rb') as rf:
    f_contents = rf.read()

raw_s = r'{}'.format(f_contents)

pattern = re.compile(r'[^\w\s]')
f_contents = re.sub(pattern=pattern, repl=r' ', string=raw_s)

word_list = f_contents.split(' ')

for word in word_list:
    if word not in word_dict:
        word_dict[word] = 1
    elif word in word_dict:
        word_dict[word] += 1
    else:
        raise Exception

top_occuring_words = [{'word': x, 'size': y} for x, y in word_dict.items() if x in sorted(word_dict, reverse=True)[:50]]
# print(top_occuring_words)
# print(sorted(top_occuring_words, key=lambda item: item[1], reverse=True))

with open(os.path.join(cwd, save_file), 'w') as wf:
    json.dump(top_occuring_words, wf, indent=2)


# [{word: "Running", size: "10"}, {word: "Surfing", size: "20"},
#  {word: "Climbing", size: "50"}, {word: "Kiting", size: "30"}, {word: "Sailing", size: "20"}, {word: "Snowboarding", size: "60"}]
