import re
import json
import csv

key = []
value = []
#read input file
with open ('input.txt', 'rt') as file1:
    ifile = file1.read()

#to put keys in a seperate list
    pattern_k = re.compile(r'(key)(=)(\w+)')
    matches_k = pattern_k.finditer(ifile)
    for match_k in matches_k:
        result_k = (match_k.group(3))
        key.append(result_k)
    print(key)

#to put values in a seperate list
    pattern_v = re.compile(r'(value)(=)(\w+)')
    matches_v = pattern_v.finditer(ifile)
    for match_v in matches_v:
        result_v = (match_v.group(3))
        value.append(result_v)
    print(value)

#join both lists to form json
    dict_kv = dict(zip(key,value))
    json_kv =json.dumps(dict_kv)
    print(json_kv)

#write json to new ourput file
with open('output.txt' , 'w') as ofile:
    ofile.write(json_kv)

#read the second txt file
with open('output.txt' , 'r') as file2:
    ifile2 = file2.read()
    data = json.loads(ifile2)

#ofile2=csv.writer(open('output.csv','wb+'))
    with open('output.txt' , 'wb+') as ofile2:
        csv_writer = csv.writer(ofile2)
        for item in data:
            ofile2.writerow([item['pk'], item['model']] + item['fields'].values())
