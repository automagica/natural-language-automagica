# Automagica with Natural Language

Wouldn't it be cool if we could write Robotic Process Automation scripts in plain ol' English rather than the already easy Python scripting language? Well it's possible with Automagica! We have coooed up a more human-friendly interface to get started with automation!

## How it works
Natural language for Automagica (.nla) looks like this:
```
open the browser
navigate to google.com
search for oranges
```

## Try it yourself

A Wit.ai key is included, so you can get a headstart! 

Install the following required packages:
```
pip install https://github.com/OakwoodAI/automagica/tarball/master
pip install https://github.com/OakwoodAI/understanding/tarball/master
```
Then install Natural Language for Automagica:
```
git clone https://github.com/OakwoodAI/natural-language-automagica
cd natural-language-automagica
pip install .
```

Then you can get started by running the examples:
```
cd examples
nla google.nla
nla wikipedia.nla
nla youtube.nla
```

Et voilà :-).
## Features
Currently only a small list of features of Automagica is implemented here, but feel free to make a pull request! 
## Requirements
Python 3.6