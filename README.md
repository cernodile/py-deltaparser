# py-deltaparser
This is a tool I wrote for my team of programmers and researchers originally - but decided to finally share to the outside world. We've had this tool for many many years and have gone through several iterations of rewrites. There may be more tools to come from us. The tool allows you to read Growtopia's items.dat file through database versions of 2 to 12 (latest as of 4th Feb 2021). This is a stripped down version of our much larger tool - but this is a good starting point for anyone curious and smart enough.

## Usage
You must have installed Python on your computer in order to use this software. Once you have installed it, open Command Prompt or terminal, whichever you have at hand, navigate to the project folder and execute following: 
```
python main.py
```

**YOU MUST HAVE items.dat FILE IN THE SAME DIRECTORY AS SCRIPT!**

The "main.py" file will use any supported data parser present in the codebase (such as world planner json or csv format or ID->name resolver) - you can easily extend this to your needs, read into item_parser.py to see how much data you can play around with and make it useful for yourself.

## Permissions
Do whatever you please with it. If you use code from this repository, credit would be appreciated.

## Ports/Cool Stuff
Did you make anything cool with this project? Perhaps ported it to your preferred language? Let me know and I may feature it here.

[houzeyhoo's c-deltaparser](https://github.com/houzeyhoo/c-deltaparser)
