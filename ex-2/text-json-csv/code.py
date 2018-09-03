import re
import json
import csv
import os

key = []
value = []
key2 = []
value2 = []

# func for text to csv
def file_to_csv():

    try:
        #read input file
        with open ('input.txt', 'r') as file1:
            ifile = file1.read()
    except FileNotFoundError as e:
        print(e)
    else:
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
        print(json_kv)
        #write json to new ourput file
        with open('output.json' , 'w') as ofile:
            ofile.write(json_kv)

        #def json_to_csv():

        #     #read json file
        # with open('output.json' , 'r') as file2:
        #     ifile2 = file2.read()
        #     data = json.loads(ifile2)
        #
        #     for k , v in data.items():
        #         key2.append(k)
        #         txt_1 = ','.join(key2)
        #         value2.append(v)
        #         txt_2 = ','.join(value2)
        #
        #     with open('output.csv' , 'w') as ofile2:
        #         ofile2.write(txt_1)
        #         ofile2.write(txt_2)
        #return json_to_csv

file_to_csv()

def json_to_csv():

    #read json file
    with open('output.json' , 'r') as file2:
        if os.stat("file2").st_size == 0:
            ifile2 = file2.read()
            data = json.loads(ifile2)

            for k , v in data.items():
                key2.append(k)
                txt_1 = ','.join(key2)
                value2.append(v)
                txt_2 = ','.join(value2)

                with open('output.csv' , 'w') as ofile2:
                    ofile2.write(txt_1)
                    ofile2.write(txt_2)

#
# if __name__ == '__main__':
#     main()
