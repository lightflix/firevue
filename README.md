# Firevue
A hirevue question cracker

## *Update (15-11-2023): Many users reported that this script does not work anymore. Hirevue may have likely patched this.*

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
6. Right click on any entry in the console and save all as HAR. Save the HAR file into the same folder that contains the python script `firevue.py`.
<img src="https://i.imgur.com/aIEB26S.jpg" alt="Firevue output" width="850"/>

7. On Windows, press (Windows key + R) and type `cmd`, then hit enter. This will open a black command prompt window. For Linux/MacOS, open the terminal.
8. In the terminal, type `cd`, followed by a space. 
9. On Windows/macOS, drag the folder onto the command prompt window you just opened. You'll see the name of that folder appear. The command now should look like `cd C:\the\path\to\the\folder`. Hit enter.
10. Type `python3 firevue.py`, then hit enter. If "python3" is not a recognized command then either 1) run the command "python" or 2) go to where python is installed and either 1) rename "python.exe" to "python3.exe" or 2) copy and paste python.exe into the same directory and rename the copy "python3.exe"
11. The script should automatically detect the HAR file and try to do its magic. Follow the instructions on-screen. Eventually it will display your interview questions like shown below:
<img src="https://i.imgur.com/RD1AL67.jpg" alt="Firevue output" width="650"/>

12. Optional: If you want to manually decode encoded text that you find in the HAR file, you can use the `-d` option. Use `python3 firevue.py -h` or `python3 firevue.py --help` to check usage.

> :warning:NOTE:
> When this script was created Hirevue included the assessment questions within the HAR file (located within the "text" field of the HTTP "response" object): the majority of the HireVue assessments no longer include the questions as text (encrypted).

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
