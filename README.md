# pythonpddl
This is a python PDDL parser. It is based on pddlpy [https://github.com/hfoffani/pddl-lib]

# Requirements
This assume you have ANTLR4 installed somewhere to generate the parsing files from pddl.g4

##### ANTLR4 Install Instructions for Ubuntu 16.04

```
cd /usr/local/lib
sudo curl -O http://www.antlr.org/download/antlr-4.7-complete.jar
```

# Installation Instructions
```
make
python setup.py build
sudo python setup.py install
```
