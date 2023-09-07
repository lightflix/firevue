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
6. Right click on any entry in the console and save all as HAR. Save the HAR file into the same folder that contains the python script `firevue.py`.
<img src="https://i.imgur.com/aIEB26S.jpg" alt="Firevue output" width="850"/>

7. On Windows, press (Windows key + R) and type `cmd`, then hit enter. This will open a black command prompt window. For Linux/MacOS, open the terminal.
8. In the terminal, type `cd`, followed by a space. 
9. On Windows/macOS, drag the folder onto the command prompt window you just opened. You'll see the name of that folder appear. The command now should look like `cd C:\the\path\to\the\folder`. Hit enter.
10. Type `python3 firevue.py`, then hit enter. If "python3" is not a recognized command then either 1) run the command "python" or 2) go to where python is installed and either 1) rename "python.exe" to "python3.exe" or 2) copy and paste python.exe into the same directory and rename the copy "python3.exe"
11. The script should automatically detect the HAR file and try to do its magic. Follow the instructions on-screen. Eventually it will display your interview questions like shown below:
<img src="https://i.imgur.com/RD1AL67.jpg" alt="Firevue output" width="650"/>

12. Optional: If you want to manually decode encoded text that you find in the HAR file, you can use the `-d` option. Use `python3 firevue.py -h` or `python3 firevue.py --help` to check usage.

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

#### 6. Is there anything that could be done since HireVue has modified the output of the HAR file?
Absolutely, yes there is. If you are using the **_Firefox Browser_** (Chrome produce the files however it did not provide the image previews) and have entered **_Developer Mode > Network (Tab)_** follow the following steps:
1. Navigate to the screen that says "_Aptitude Assessment: The assessment measures your aptitude in areas such as critical thinking and problem-solving. This helps you demonstrate your potential to employers, beyond what appears in your resume. Answer each question carefully, but do not spend too much time on any one question. If you can't determine the answer to a question you should select an answer and move on. You will receive one point for each correct answer. No points are deducted for incorrect answers. The questions become more difficult as the assessment progresses._" **_DO NOT HIT THE BUTTON TO START THE ASSESSMENT!!! Follow the next few steps first._**

2. Examine the files under the "Network" tab. By hovering over certain files (i.e. .png) the spatial questions that include images as the questions in the actual assessment are visible.
   - Consider studying what is provided prior to starting the assessment. One method is to copy the URL (right-click > Copy > Copy URL) of the questions/image and paste it into Google Lens to search the images discovered for pre-discovered answers or simply examine them and figure out the answer on your own. 
     -  [Brainly](https://brainly.com/) (available via both web browser as well as app) provides a lot of answers to the exact same as well as similar questions which assist in finding the pattern of the sequence. Searching for answers via AI is also a viable option if you are not wanting to waste too much of your own brain juice.
     - Another great source for information as well as a few answers is [here](https://av-krishnan.medium.com/) which includes both actual questions as well as sample questions with explanations as to how to solve similar problems.
   - The files where there are four images and no question are typically asking which image does not belong (for example if three shapes have a square in the center and one shape has a circle in the center then the circle centered shape would be the correct answer because it is different than the other three).
   - Questions with a chart, good luck: they typically ask “what is the difference between the percentage of ‘A’ at this time and ‘B’ at this time,” however you will not know which data sets are in question until live in the assessment.
       - A word of advice is knowing how to calculate percentages prior to the assessment starts and plug in the numbers: 

_percentageDifference = (((highestNumber - lowestNumber) / lowestNumber) *100)_

3. Once you are confident start the assessment: by preparing in advance and jotting down the answers available this allows you to answer those questions sooner providing more time on the questions that are hidden from the HAR file. 

