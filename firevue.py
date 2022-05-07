#Simple tool to extract and decode hirevue questions from a browser HAR file
import json
import glob

def keyCheck(object, key):

    #the object should be a dict, not an string. It could be a string if the keyCheck() returned "[not available]" on a recursive call.
    if type(object) == str:
        return object
    try:
        value = object[key]
    except KeyError:
        return "[not available]"
    else:
        #if if value from key is an int, then we convert it to str on return.
        if type(value) == int:
            return str(value)
        return value

def decoder(ciphertext):

    #if questions couldn't be extracted
    if ciphertext == "[not available]":
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
        raise ValueError("[x] Error: There must only be one har file in the current directory.")

    #pick the only har file in current directory. 
    har_filename = har_file[0]

    #load json from the HAR file
    har_file = json.load(open(har_filename, encoding="utf-8"))

    entries = keyCheck(keyCheck(har_file, 'log'), 'entries')

    #iterate though each request made by the browser 
    for entry in entries:

        #in each entry, get inside the response object and then into content.
        content = keyCheck(keyCheck(entry, 'response'), 'content') 

        #questions are normally in the content object with the key "text"
        if "text" in content and "\"questions\":" in content["text"]:

            #the questions are again encoded in json to pythonise that.
            return json.loads(content["text"])

    #no questions found :(
    return False

def infoGet(content):

    question_list = keyCheck(content,'questions')
    print("\n[-] Interview Details\n")

    print("  - Interviewer: "+keyCheck(content,'interviewer'))
    print("  - Role: "+keyCheck(content,'position'))
    print("  - Number of questions (includes games section): "+keyCheck(content,'questionCount'))
    print("  - Number of retries allowed: "+keyCheck(content,'retryAllowance'))
    print("  - Interview Duration: "+keyCheck(content,'interviewDurationMinutes')+" mins")
    print("  - Invite Date: "+keyCheck(keyCheck(content, 'interviewUses')[0], 'invitedDate'))

    print("\n[-] Interview Questions")
    if question_list == "[not available]":
        print("[x] Not available")
    else:
        i = 0
        for q in question_list:
            if keyCheck(q,'type') != "mindx-assessment":
                print("\n  - Question "+str(i+1)+": Prep Time (sec): "+keyCheck(q,'prepTimeSeconds')+", Max Answer Duration (sec): "+keyCheck(q,'maxDuration'))

                # send each question into the decoder that converts it back to plaintext. 
                print(decoder(keyCheck(q,'text')))
                print("\n -------------------------------")
            i += 1

if __name__ == "__main__":

    #parse result contains the interview details and all questions.
    parse_result = harParse()

    if parse_result == False:
        print("\n[x] ERROR: Incorrect HAR parsing, exiting.")
        exit()

    print("\n--== Infinite Prep Time: A Hirevue Question Cracker v1.0 ==--")

    #fetch values and print them neatly
    infoGet(parse_result)
    print("\n[-] Done!\n")
