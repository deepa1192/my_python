import re
import json
import csv
import os

key = []
value = []

# func for text to csv
def file_to_csv():

    try:
        #read input file
        with open ('input.txt', 'r') as file1:
            ifile = file1.read()
            # #to put keys in a seperate list
            pattern_k = re.compile(r'(key)(=)(\w+)')
            matches_k = pattern_k.finditer(ifile)
            for match_k in matches_k:
                result_k = (match_k.group(3))
                key.append(result_k)
            #to put values in a seperate list
            pattern_v = re.compile(r'(value)(=)(\w+)')
            matches_v = pattern_v.finditer(ifile)
            for match_v in matches_v:
                result_v = (match_v.group(3))
                value.append(result_v)
            #join both lists to form json
            dict_kv = dict(zip(key,value))
            json_kv =json.dumps(dict_kv, indent =2)
            #write json to new ourput file
            with open('output.json' , 'w') as ofile:
                ofile.write(json_kv)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)

file_to_csv()

def json_to_csv():
    #read json file
    # if os.stat("output.json").st_size == 0:
        # Print("if")
    with open('output.json') as file2:
        data = json.load(file2)
        with open('output.csv' , 'w') as ofile2:

            for k , v in data.items():
                ofile2.write(k + ',' + v + ';')

json_to_csv()

if '__name__' == '__main__':
    main()
