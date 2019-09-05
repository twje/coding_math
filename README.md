# Coding Math

The YouTube chennal [Coding Math](https://www.youtube.com/user/codingmath/playlists) demonstrates math through coding with JavaScript. This flask web application provides a simple framework to allow students to follow along with the coding exercises.

The diretories under `src\static\js` correspond to sections in the channel, section for trigonemtry, physics etc. A section directory contains java script files that corrspond to the episodes as you follow along with the exercies, i.e. `trigonometry\trig01.js`

## Prerequisites

*  Python 3.X
*  git client

## Getting Started

1.  Clone the repostory to a directory:
   
    `git clone https://github.com/twje/coding_math.git .`

2.  Create a python virtual environment:

    `python -m venv venv`
    
3.  Activate python virtual environment:

    `venv\Scripts\activate.bat`

4.  Install dependancies:

    `pip install -r requirements.txt`
    
5.  Start web application:
    
    `cd src`
    
    `python run.py`

6.  Test URL in browser: `http://127.0.0.1:4990/`. You will see a list of sections and links - click `trig01.js` to run the javascript to display a trig curve.
