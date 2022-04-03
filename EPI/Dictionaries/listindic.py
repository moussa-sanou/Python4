
eng_dic = {}

# Adding list as value
eng_dic['solitude'] = ['lone', 'lonely', 'alone', 'unaccompanied', 'without society']
eng_dic['hope'] = ['aspiration', 'desire', 'wish', 'expectation', 'ambition']
print(eng_dic)

# Creating a dictionary with an empty list
eng_dic.clear()
eng_dic = {'solitude':[]}
eng_words = ['lone', 'lonely', 'alone', 'unaccompanied', 'without society']
eng_dic['solitude'].append(eng_words[0])
print(eng_dic)

eng_dic['solitude'] = eng_words
print(eng_dic)

if (eng_dic.get('solitude')):
    for list_item in eng_dic['solitude']:
        print(list_item)
else:
    print('word not in dictionary')