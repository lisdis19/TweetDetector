![logo%20%281%29.png](attachment:logo%20%281%29.png)

*TweetDetector* is a simple Twitter scraper. It detects in images utilizing YOLOv5 and labels according to an established corpus in our code. 

In order to use this program a Jupyter Notebook is included in this repository with a step-by-step instruction to ensure the program runs smoothly.

Questions? Ran into any Bugs or Issues? *Reach Lisa DiSalvo at ldisalvo@arcadia.edu*

# Setup

Clone GitHub [repository](https://github.com/lisdis19/TweetDetector), install [dependencies](https://github.com/lisdis19/TweetDetector/blob/main/requirements.txt) and check PyTorch and GPU.
This project is ran on Python 3.9.6 (64-bit). Windows 11


```python
# !git clone https://github.com/lisdis19/TweetDetector  # clone
%cd TweetDetector (OR CD directly to the path to where the files downloaded on your PC)
%pip install -qr requirements.txt  # install the requirements file for YOLO image detection library
%pip install -qr requirements2.txt #install requirements for TweetDetector

#in Command Prompt, type in python --version to check what version of Python you are running on your system
#Then, to test if libraries work, type in python, then the following lines of code
import torch
import utils
display = utils.notebook_init()  # checks
```
