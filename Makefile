ANTLRLIB=/usr/local/lib/antlr-4.7-complete.jar
ANTLR=java -jar $(ANTLRLIB)
ANTLRLANG=-Dlanguage=Python3

all: pddl.g4
	$(ANTLR) $(ANTLRLANG) -o pythonpddl pddl.g4
 
