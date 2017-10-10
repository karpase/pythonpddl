import sys
from pythonpddl import pddl

def adjust_til(problem, time_adjustment):
    for el in problem.initialstate:
        if isinstance(el, pddl.TimedFormula):
            el.timespecifier = max(0, el.timespecifier - time_adjustment)            

def main():
    if len(sys.argv) < 4:
        print("Usage: pddl.py <domain> <problem> <til_adjustment> <new_problem>")
        return

    domainfile = sys.argv[1]
    problemfile = sys.argv[2]
    adjustment = float(sys.argv[3])
    
    (_,prob) = pddl.parseDomainAndProblem(domainfile, problemfile)
    adjust_til(prob, adjustment)
    
    new_problem = sys.argv[4]
    
    np = open(new_problem, 'w')
    np.write(prob.asPDDL())
    np.close()
    
    
    
    #for a in dom.actions:
    #    for b in [False, True]:
    #        print(a.name, "c", b, list(map(lambda x: x.asPDDL(), a.get_pre(b))))
    #    for b in [False, True]:
    #        print(a.name, "e", b, list(map(lambda x: x.asPDDL(), a.get_eff(b))))

    #for da in dom.durative_actions:
    #    for t in ["start","all","end"]:
    #        for b in [False, True]:
    #            print(da.name, "c", t, b, list(map(lambda x: x.asPDDL(), da.get_cond(t, b))))
    #    for t in ["start","all","end"]:
    #        for b in [False, True]:
    #            print(da.name, "e", t, b, list(map(lambda x: x.asPDDL(), da.get_eff(t, b))))


if __name__ == "__main__":
    main()