# PROGRAMING AND SCRIPTS

This repository contains all exercises proposed on module *PROGRAMING AND SCRIPTING* during the course **DATA ANALYTICS**, from ***GMIT - GALWAY-MAYO INSTITUTE OF TECHNOLOGY***. 

<br/>

## PRE-REQUISITES

In order to run the scripts in this repository, the **PYTHON INTERPRETER** must be installed on the local computer.
The Python download requires about 25 Mb of disk space; keep it on your machine, in case you need to re-install Python. When installed, Python requires about an additional 90 Mb of disk space. 
<br/><br/>
## INSTALLATION


##### THE STEPS BELOW DESCRIBE HOW TO INSTALL PYTHON ON A WINDOWS PLATAFORM. TO INSTALL IT ON A DIFFERENT OPERATIONAL SYSTEM, CHECK THE DOWNLOAD SECTION IN https://www.python.org/downloads/


1. Downloading:
   PYTHON INTERPRETER can be downloaded from the link below. More informations available here: https://www.python.org/downloads/
   Download Python: https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe 
2. Click the Save File button.

The file named python-3.7.4-amd64.exe should start downloading into your standard download folder. This file is about 30 Mb so it might take a while to download fully if you are on a slow internet connection (it took me about 10 seconds over a cable modem).

The file should appear as python-3.7.4-amd64.exe

3. Move this file to a more permanent location, so that you can install Python (and reinstall it easily later, if necessary).

4. Feel free to explore this webpage further; if you want to just continue the installation, you can terminate the tab browsing this webpage.

5.Start the Installing instructions directly below. 


#### INSTALLING :
1. **Double-click the icon labeling the file python-3.7.4-amd64.exe**.

A Python 3.7.4 (64-bit) Setup pop-up window will appear. 

Ensure that the Install launcher for all users (recommended) and the Add Python 3.7 to PATH checkboxes at the bottom are checked.

If the Python Installer finds an earlier version of Python installed on your computer, the Install Now message may instead appear as Upgrade Now (and the checkboxes will not appear).

2. **Highlight the Install Now (or Upgrade Now) message, and then click it**. 

When run, a User Account Control pop-up window may appear on your screen. I could not capture its image, but it asks, Do you want to allow this app to make changes to your device. 

3. **Click the Yes button**.

A new Python 3.7.4 (64-bit) Setup pop-up window will appear with a Setup Progress message and a progress bar. 

During installation, it will show the various components it is installing and move the progress bar towards completion. Soon, a new Python 3.7.4 (64-bit) Setup pop-up window will appear with a Setup was successfuly message. 

4. **Click the Close button**. 

Python should now be installed.

<br/>

## VERIFYING

1. Navigate to the directory **C:\Users\<user>\AppData\Local\Programs\Python\Python37** (or to whatever directory Python was installed: see the pop-up window for Installing step 3).

2. Double-click the icon/file **python.exe**. 

A pop-up window with the title **C:\Users\<user>\AppData\Local\Programs\Python\Python37\python.exe** appears, and inside the window; on the first line is the text **Python 3.7.4** ... (notice that it should also say 64 bit). Inside the window, at the bottom left, is the prompt >>>: type exit() to this prompt and press enter to terminate Python.

*You should keep the file python-3.7.4.exe somewhere on your computer in case you need to reinstall Python (not likely necessary).*
<br/>
## SCRIPTS
This repository contains the following scripts:


- **W2_bmi.py**:
This program calculates somebody's Body Mass Index (BMI)
The inputs are the person's height in centimetres and weight in kilograms. 
The output is their weight divided by their height in metres squared. 


- **W3_secondstring.py**:
This program asks a user to input a string and outputs every second letter in reverse order. 
Here is an example:
PLEASE ENTER A SENTENCE: The quick brown fox jumps over the lazy dog.
.o zletrv pu o wr cu h


- **W4_collatz.py**:
This script asks the user to input any positive integer and outputs the successive values 
of the following calculation. At each step, it calculate the next value by taking the current value and, 
if it is even, divide it by two, but if it is odd, multiply it by three and add one. The program 
ends if the current value is one. See example below:
number = 10
10 / 2 = 5
number = 5
5 x 3 + 1 = 16
number = 16
16 / 2 = 8
number = 8
8 / 2 = 4
number = 4
4 / 2 = 2
number = 2
2 / 2 = 1
number = 1
end


- **W5_weekday.py**:
This program tells to the user wether or not today is a weekday
When run, its output will either be the phrase "Yes, unfortunately today is a weekday" or "It is the weekend, yay!"


- **W6_squareroot.py**:
This program takes a positive floating-point number as input and outputs an approximation of its square root, using the Newton's Method
It requires a user to enter 2 parameters:  1. a positive number; and 2. an approximation value (like 0.000001)
It is important to observe here that this script depends on an external function, called **SquaresGMIT.py**


- **W7_Read_a_text_File.py**:
This program ask for a text file name (both text file and python script must be in the same folder), then it asks for a desired character to be seek throughout the program and outputs the number of this character occurrence
Basically, it counts how many times a character has occurred in a text


- **W8_chart.py**:
This program  plots a chart on screen based on these 3 formulas: f(x)=x, g(x)=x2 and h(x)=x3
There is no input asked by user in this script
<br/><br/>

## HOW TO RUN:

The first step is to download this repository's content to the local computer. To do so, follow the steps below:
1. click on the button **CLONE OR DOWNLOAD**
2. Click **DOWNLOAD ZIP**
3. Unzip the file **GMIT-DataAnalitics-master.zip** to a folder

<br/>

### STARTING THE PYTHON INTERPRETER


The simplest way to start the interpreter is to open the terminal and then use the interpreter from the command-line.

To open the command-line interpreter:

- On **Windows**, the command-line is called the command prompt or MS-DOS console. A quicker way to access it is to go to **Start menu → Run** and type **cmd**.
- On **GNU/Linux**, the command-line can be accessed by several applications like xterm, Gnome Terminal or Konsole.
- On **MAC OS X**, the system terminal is accessed through **Applications → Utilities → Terminal**. 


#### RUNNING SCRIPTS USING PYTHON COMMAND

You must have your prompt on the same directory where the scrips were unzipped. In this example, let's consider that the directory is going to be c:\users\download\scripts, once you are on prompt, type as below:

python script_name.py


<br/>

## AUTHOR
***THIAGO HENRIQUE LEAO DE LIMA***
<br/><br/>

## BIBLIOGRAPHY
How To Run Your Python Scripts (https://www.knowledgehut.com/blog/programming/run-python-scripts)
Python Community (https://www.python.org/community/)

<br/>

## License
[MIT](https://choosealicense.com/licenses/mit/)
