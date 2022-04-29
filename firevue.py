#Simple tool to extract and decode hirevue questions from a browser HAR file
import json
import glob

def keyCheck(object, key):

    if type(object) == str:
        return object
    try:
        value = object[key]
    except KeyError:
        return "[not available]"
    else:
        if type(value) == int:
            return str(value)
        return value

def decoder(ciphertext):

    if ciphertext == "[not available]":
        return ciphertext

    chars = list(ciphertext)
    first_half = chars[:len(chars)//2]
    second_half = chars[len(chars)//2:]
    result = []

    for i in range(0, len(first_half)):
        result.append(second_half[i])
        result.append(first_half[i])

    return "".join(result)

def harParse():

    har_file = glob.glob('*.har') 

    if len(har_file) != 1:
        raise ValueError("[x] Error: There must only be one har file in the current directory.")

    har_filename = har_file[0]

    har_file = json.load(open(har_filename))

    entries = keyCheck(keyCheck(har_file, 'log'), 'entries')

    for entry in entries:
        content = keyCheck(keyCheck(entry, 'response'), 'content') 

        if "text" in content and "\"questions\":" in content["text"]:
            return json.loads(content["text"])
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
                print(decoder(keyCheck(q,'text')))
                print("\n -------------------------------")
            i += 1

if __name__ == "__main__":

    parse_result = harParse()

    if parse_result == False:
        print("\n[x] ERROR: Incorrect HAR parsing, exiting.")
        exit()

    print("\n--== Infinite Prep Time: A Hirevue Question Cracker v1.0 ==--")

    infoGet(parse_result)
    print("\n[-] Done!\n")
