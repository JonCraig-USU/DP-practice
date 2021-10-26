# Can string A be built from the key values in D?
'''Assumptions made:
    spaces will be ignored
    no spaces will be entered thus striip is not needed
    single line A values only'''

# *** Practice values ***
import numpy as np


A0 = "_catinthehat"
D0 = {"ca", "tin", "inth", "it", "ehat", "th"}
# build(A0, D0) returns true
A1 = "_ttttttttttt"
D1 = {"g", "a", "t"}
# returns true
A2 = "_nowheretorunnow"
D2 = {"this", "will", "return", "false"}
# return false
A3 = "_yttttttttttttttttttttttttttttttttttt"
D3 = {"g", "a", "t"}
# return false

# Arrays of probs for simpler testing
As = [A0, A1, A2, A3]
Ds = [D0, D1, D2, D3]

# Recursive alg with one arg, n
def build(n):
    if n == 1:
        return True
    for i in range(1, n):
        if A[i:n] in D:
            if build(i):
                return True
    return False

def buildDP(n):
    # global solution set up
    global sol
    sol = np.zeros(n+1)

    # set all initial values to false
    for k in range(1, n+1):
        sol[k] = False

    # set the base case when n = 0 to true
    sol[0] = True

    for i in range(1, n):
        for j in range(1, i):
            if A[j:i] in D:
                if sol[j]:
                    sol[i] = True
    return sol[n]

def traceBAck(n):
    global sol

    if n == 0:
        return []
    
    # if sol[]
    return


for rep in range(4):
    A = As[rep]
    D = Ds[rep]
    print(str(rep) + " recursive: " + str(build(len(A))))
    print(str(rep) + " DP: " + str(build(len(A))))

print("===================================")


