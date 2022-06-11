# Firevue
A hirevue question cracker

### Requirements
1. Python 3
2. Mozilla Firefox (Google Chrome might work but I haven't tested it).
3. Hirevue interview invite link

### Steps to run this code
1. Download the repository or the python file `firevue.py`.
2. Move the python file in any new directory (folder). This could be anywhere on the system.
3. Open the valid hirevue invite link in Firefox. If you don't see your name on the page, click the continue or start button and the page showing your name should be next. This will not the start the interview. But it's an important step in capturing the questions.
4. Open the web development console (`CTRL+SHIFT+I` or `CMD+ALT+I`). Click on the network tab. 
5. Reload the current page so it can capture all web traffic.
6. Right click on any entry in console and save all as HAR. Save the HAR file into the same folder that contains the python script `firevue.py`.
<img src="https://i.imgur.com/aIEB26S.jpg" alt="Firevue output" width="850"/>

7. Run the script in command prompt or Terminal using `python3 firevue.py`. Make sure the CMD prompt/Terminal is working on the directory that contains the two files. In other words, open the terminal in that folder. 
If you're on Windows, the prompt will look something like `C:\Users\<your username>\<the folder>` and on macOS `username@hostname the_folder_name %`. If you do not see the folder name in the prompt, you have not opened it in the correct folder. 
Here's how you do it (on both Windows/macOS): Drag the folder onto the command prompt and you will see the path of that folder pasted in there. Add `cd` before the path followed by a space. The command now should look like `cd <the path of the folder>`. Hit enter and then run the above command `python3 firevue.py`.
The script should automatically detect the HAR file, try to do its magic and display your interview questions like shown below.
<img src="https://i.imgur.com/RD1AL67.jpg" alt="Firevue output" width="650"/>

8. Optional: If you want to manually decode encoded text that you find in the HAR file, you can use the `-d` option. Use `python3 firevue.py -h` or `python3 firevue.py --help` to check usage.

### FAQs

#### 1. What does this script do and how does it work?
This script reads web responses that were sent by Hirevue after you clicked the interview link. To my surprise, Hirevue sends all interview-related data including questions to your browser before the interview even starts. This means our browser already has the questions beforehand and displays them one at a time as you go through the interview process. The questions though were encoded with some trivial algorithm which I could easily reverse engineer. 

<img src="https://i.imgur.com/qNpi6Fl.jpg" alt="Encrypted questions as seen in Hirevue response" width="400"/>

I exploited this flaw and wrote python code to analyse the response, decrypt the "encrypted" questions and reveal them in plaintext so you can take all the time you need to prepare and give your best answers.

#### 2. I don't have Python installed. How do I install it?
- Windows users: https://www.tutorialspoint.com/how-to-install-python-in-windows
- MacOS users: It's preinstalled. Just run the code using the above steps.
- Linux users: Yes

#### 3. I followed the above steps and it still doesn't work.
There are a multitude of reasons why this may not work. Each interview can be slightly different in the way they're structured in the delivery process which could mean the questions may be in a different location in the received response, or the encoding might be different, or even worse - Hirevue may have fixed this. The only way I could have made my code more compatible was if I could test this on multiple interview links from different interviewers/companies. This isn't possible at the moment unless applicants send me their interview links for testing.

#### 4. Why didn't I use the python requests library to automate all of this from just the interview link?
I didn't want to access the interview page hundreds of times just to test my code, have them think I'm sus and increase my chances of failing the interview. 

#### 5. Is this safe to run?
Yes, this script is 100% safe, runs locally and only reads the HAR file you've placed in its directory. You may be violating Hirevue's terms and conditions. I haven't read the fine print so I can't tell.
