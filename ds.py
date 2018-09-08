import json

with open('input.json') as data_file:

    data = json.load(data_file)

for key, value in data.items():

    #print key, value
    print "key=",key
    print "value=",value
