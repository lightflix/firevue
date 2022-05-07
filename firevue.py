#Simple tool to extract and decode hirevue questions from a browser HAR file
import json
import glob
from typing import Type

class color:
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   BOLD = '\033[1m'
   END = '\033[0m'

def decoder(ciphertext):

    #if questions couldn't be extracted
    if ciphertext == None:
        return ciphertext

    #convert string to character array
    chars = list(ciphertext)

    #first half of ciphertext array
    first_half = chars[:len(chars)//2]

    #second half of ciphertext array
    second_half = chars[len(chars)//2:]
    result = []

    for i in range(0, len(first_half)):

        #take one char from the first half and another char from the second half and add to resultant array.
        result.append(second_half[i])
        result.append(first_half[i])

    #convert array/list back to string and return.
    return "".join(result)

def harParse():

    har_file = glob.glob('*.har') 

    if len(har_file) != 1:
        raise ValueError("[x] Error: HAR file does not exist in current directory or there is more than one HAR file in current directory!")

    #pick the only har file in current directory. 
    har_filename = har_file[0]

    #load json from the HAR file
    har_file = json.load(open(har_filename, encoding="utf-8"))

    try:
        entries = har_file.get('log', None).get('entries', None)
    except AttributeError:
        raise AttributeError("[x] Error: Logs or Entries not found")

    #iterate though each request made by the browser 
    try:
        for entry in entries:

            #in each entry, get inside the response object and then into content.
            content = entry.get('response', None).get('content', None) 

            #questions are normally in the content object with the key "text"
            if "text" in content and "\"questions\":" in content["text"]:

                #the questions are again encoded in json to pythonise that.
                return json.loads(content["text"])

    except TypeError:
        raise TypeError("[x] Error: Entries object isn't an iterable."+" Current Type:"+str(type(entries)))

    #no questions found :(
    return False

def infoGet(content):

    question_list = content.get('questions', None)
    print(color.BOLD+"\n[-] Interview Details\n"+color.END)

    print(color.GREEN+"  - Interviewer: "+color.END+str(content.get('interviewer', None)))
    print(color.GREEN+"  - Role: "+color.END+str(content.get('position', None)))
    print(color.GREEN+"  - Number of questions (includes games section): "+color.END+str(content.get('questionCount', None)))
    print(color.GREEN+"  - Number of retries allowed: "+color.END+str(content.get('retryAllowance', None)))
    print(color.GREEN+"  - Interview Duration: "+color.END+str(content.get('interviewDurationMinutes', None))+" mins")
    print(color.GREEN+"  - Estimated Duration: "+color.END+str(content.get('estimatedMinutesToComplete', None))+" mins")
    print(color.GREEN+"  - Invite Date: "+color.END+str(content.get('interviewUses', None)[0].get('invitedDate', None)))

    print(color.BOLD+"\n[-] Interview Questions"+color.END)
    if question_list == None:
        print("[x] Not available")

    else:
        i = 0
        for q in question_list:
            if q.get('type', None) != "mindx-assessment":
                print(color.GREEN+"\n  - Question "+str(i+1)+": Prep Time (sec): "+str(q.get('prepTimeSeconds', None))+", Max Answer Duration (sec): "+str(q.get('maxDuration', None))+", Answer type: "+str(q.get('type', None))+color.END+"\n")

                # send each question into the decoder that converts it back to plaintext. 
                print(decoder(q.get('text', None)))
                print("\n -------------------------------")
            i += 1

if __name__ == "__main__":

    #parse result contains the interview details and all questions.
    try:
        parse_result = harParse()
    except ValueError as e:
        print(str(e))
        exit()

    if parse_result == False:
        print("\n[x] ERROR: Incorrect HAR parsing, exiting.")
        exit()

    print(color.YELLOW+"\n--== Infinite Prep Time: A Hirevue Question Cracker v1.0 ==--"+color.END)

    #fetch values and print them neatly
    infoGet(parse_result)
    print(color.BLUE+"\n[-] Good luck! :D\n"+color.END)
