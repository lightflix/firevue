# Firevue
A hirevue question cracker

### Requirements
1. Python 3
2. Mozilla Firefox (Google Chrome might work but I haven't tested it).
3. Hirevue interview invite link

### Steps to run this code
1. Download the repository or the python file.
2. Add the python file in its own directory (folder).
3. Open the valid hirevue invite link in Firefox.
4. Open the web development console (CTRL+SHIFT+I or CMD+ALT+I). Click on the network tab. 
5. Reload the page so it can capture all web traffic. 
6. Right click on any entry in console and save all as HAR. Save the HAR file into the same folder as the python script. ![Steps in web dev console](https://i.imgur.com/aIEB26S.jpg)\
8. Run the python script in command prompt or Terminal using `python firevue.py`.
The script should automatically detect the HAR file, try to do its magic and display your interview questions as shown below. Good luck!\
![Firevue output](https://i.imgur.com/RD1AL67.jpg)

### FAQs

#### 1. What does this script do and how does it work?
This script reads web responses that were sent by Hirevue after you clicked the interview link. To my surprise, Hirevue sends all interview-related data including questions to your browser before the interview even starts. This means our browser already has the questions beforehand and displays them one at a time as you go through the interview process. The questions though were encoded with some trivial algorithm which I could easily reverse engineer. 
![Encrypted questions as seen in Hirevue response](https://i.imgur.com/qNpi6Fl.jpg)\
I exploited this flaw and wrote python code to analyse the response, decrypt the "encrypted" questions and reveal them in plaintext so you can take all the time you need to prepare and give your best answers.

#### 2. I don't have Python installed. How do I install it?
- Windows users: https://www.tutorialspoint.com/how-to-install-python-in-windows
- MacOS users: It's preinstalled. Just run the code using the above steps.
- Linux users: Yes

#### 3. I followed the above steps and it still doesn't work.
This is unfortunate but I can count the number of Hirevue interviews I've gotten in one hand and I've tested this code only on one of them. There are a multitude of reasons why this may not work. Each interview can be slightly different in the way they're structured in the delivery process which could mean the questions may be in a different location in the received response, or the encoding might be different, or even worse - Hirevue may have fixed this. The only way I could have made my code more compatible was if I could test this on multiple interview links from different interviewers/companies. This isn't possible at the moment unless I have volunteers.

#### 4. Why didn't I use the python requests library to automate all of this from just the interview link?
I didn't want to access the interview page hundreds of times just to test my code, have them think I'm sus and increase my chances of failing the interview. 

