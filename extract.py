import json
import os

def count_pronouns():
    han_counter = 0
    hon_counter = 0
    den_counter = 0
    det_counter = 0
    denna_counter = 0
    denne_counter = 0
    hen_counter = 0


    directory = r'./data'
    for filename in os.listdir(directory):
        if(filename == ".DS_Store"):
            continue
        print(filename)
        for line in open("./data/"+ filename, 'r'):
            if(line != "\n"):
                data = json.loads(line)
                word = ""
                if 'retweeted_status' in data:
                    continue
                for letter in data['text']:
                    if(letter == " "):
                        if (word.lower() == "han"):
                            han_counter = han_counter +1
                        if (word.lower() == "hon"):
                            hon_counter = hon_counter +1
                        if (word.lower() == "den"):
                            den_counter = den_counter +1
                        if (word.lower() == "det"):
                            det_counter = det_counter +1
                        if (word.lower() == "denna"):
                            denna_counter = denna_counter +1
                        if (word.lower() == "denne"):
                            denne_counter = denne_counter +1
                        if (word.lower() == "hen"):
                            hen_counter = hen_counter +1
                        word = ""
                        continue
                    word = word + letter


    print("han: "+ str(han_counter))
    print("hon "+ str(hon_counter))
    print("den "+ str(den_counter))
    print("det "+ str(det_counter))
    print("denna "+ str(denna_counter))
    print("denne "+ str(denne_counter))
    print("hen "+ str(hen_counter))
