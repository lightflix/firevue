#Simple tool to extract and decode hirevue questions from a browser HAR file
import json, glob, argparse

class color:
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   BOLD = '\033[1m'
   END = '\033[0m'

def decoder_plaintext(ciphertext):
    #uno reverse card
    return ciphertext

def decoder_original(ciphertext):
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

    #if length of string is odd, it can't be evenly divided leaving out an additional character in the second half from being printed in loop, so we append that separately.
    if(len(chars) % 2 == 1):
        result.append(second_half[-1])

    #convert array/list back to string and return.
    return "".join(result)

def harParse():

    har_file = glob.glob('*.har')

    if len(har_file) != 1:
        raise ValueError("[x] Error: HAR file does not exist in current directory or there is more than one HAR file in current directory!")

    #pick the only har file in current directory.
    har_filename = har_file[0]

    print(har_file[0])

    #load json from the HAR file
    har_file = json.load(open(har_filename, encoding="utf-8"))

    try:
        entries = har_file.get('log').get('entries')
    except AttributeError:
        raise AttributeError("[x] Error: Logs or Entries not found")

    #iterate though each request made by the browser
    try:
        for entry in entries:

            #in each entry, get inside the response object and then into content.
            content = entry.get('response').get('content')

            #questions are normally in the content object with the key "text"
            if "text" in content and "\"questions\":" in content.get("text") and "interviewerId" in content.get("text"):
                if not content.get("mimeType") == "application/json":
                    print("[-] Warning: json mimetype not found, attempting to fetch info")

                #the questions are again encoded in json to pythonise that.
                return json.loads(content["text"])

    except TypeError:
        raise TypeError("[x] Error: Entries object isn't an iterable."+" Current Type:"+str(type(entries)))

    #no questions found :(
    return False

def getQuestions(obj, decoder_func):

    question_list = obj.get('questions')
    if question_list == None:
        print("[x] Not available")
    else:

        i = 0
        for q in question_list:
            if q.get('type') != "mindx-assessment":
                print(color.GREEN+"\n  - Question "+str(i+1)+": Prep Time (sec): "+str(q.get('prepTimeSeconds'))+", Max Answer Duration (sec): "+str(q.get('maxDuration'))+", Answer type: "+str(q.get('type'))+color.END+"\n")

                # send each question into the decoder that converts it back to plaintext.
                print(decoder_func(q.get('text')))

                #if questions is of multiple choice type, print options.
                if str(q.get('type')) == "multiple-selection":
                    for option in q.get('options'):
                        print("  [ ]",decoder_func(option))

                if str(q.get('type')) == "multiple-choice":
                    for option in q.get('options'):
                        print("  [ ]",decoder_func(option))

                print("\n -------------------------------")
            i += 1

def getInfo(content, decoder_func):

    print(color.BOLD+"\n[-] Interview Details\n"+color.END)

    print(color.GREEN+"  - Interviewer: "+color.END+str(content.get('interviewer')))
    print(color.GREEN+"  - Role: "+color.END+str(content.get('position')))
    # print(color.GREEN+"  - Total number of questions (includes games section): "+color.END+str(content.get('questionCount')))
    print(color.GREEN+"  - Number of retries allowed: "+color.END+str(content.get('retryAllowance')))
    print(color.GREEN+"  - Interview Duration: "+color.END+str(content.get('interviewDurationMinutes'))+" mins")
    print(color.GREEN+"  - Estimated Duration: "+color.END+str(content.get('estimatedMinutesToComplete'))+" mins")
    print(color.GREEN+"  - Invite Date: "+color.END+str(content.get('interviewUses')[0].get('invitedDate')))

    print(color.BOLD+"\n[-] All possible Interview Questions"+color.END)
    getQuestions(content, decoder_func)

    print(color.BOLD+"\n[-] Interview Sections"+color.END)
    section_list = content.get('sections')
    if section_list == None:
        print("[x] Not available")
    else:
        print("[-] Questions in this interview: ")
        i = 0
        for s in section_list:
            print(color.BLUE+"\n  - Section "+str(i+1)+": "+str(s.get('name'))+color.END+"\n"+str(s.get('instructions'))+"\n\n -------------------------------")
            getQuestions(s, decoder_func)
            i += 1

if __name__ == "__main__":

    cmdlineParse = argparse.ArgumentParser(description="This utility scans through a HAR file (JSON), automatically searches for interview data and displays them in decoded form. This is the default behaviour if no optional argument is specified. See below for manual decoding of text (for advanced users only).")

    cmdlineParse.add_argument('-d','--decode', type=str, help="Specify encoded text from the HAR file to be decoded, within double quotes. This mode does not read files and only uses the decode function of this script. Warning: Decoding may be incorrect if string supplied is incomplete or there are additional characters.  \n\nExample usage: \npython firevue.py -d \"[String including \\\" as seen in file]\"", dest="encoded_string")
    args = cmdlineParse.parse_args()

    if args.encoded_string:
        print(color.YELLOW+"\n--== Firevue: Decode Mode ==--"+color.END)

        es = args.encoded_string

        if(es[:1] != "\"" or es[-1:] != "\""):
            print("[x] Error: Decoding failed. String incomplete or there are additional characters. String must begin and end with \\\" inside double quotes.\n")
            exit(0)

        print("\n"+decoder_original(es[1:-1])+"\n")
        exit(0)

    #parse result contains the interview details and all questions.
    try:
        parse_result = harParse()
    except ValueError as e:
        print(str(e))
        exit()

    if parse_result == False:
        print("\n[x] ERROR: Incorrect HAR parsing, exiting.")
        exit()

    print(color.YELLOW+"\n--== Firevue: A Hirevue Question Cracker v1.1 ==--"+color.END)

    #fetch values and print them neatly
    decoders = [decoder_plaintext, decoder_original]
    for decoder in decoders:
        getInfo(parse_result, decoder)
        print("\n\n*** If the questions are readable, enter \"Y\" to finish, otherwise enter \"N\" to try again. ***\n")
        response = input().lower()
        if response == "y":
            break

    # getInfo(parse_result)

    # with open("parsed_result.json","w") as f:
    #     json.dump(parse_result, f, indent=4)

    print(color.BLUE+"\n[-] Good luck! :D\n"+color.END)
