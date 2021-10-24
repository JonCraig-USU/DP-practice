# Can string A be built from the key values in D?
'''Assumptions made:
    spaces will be ignored
    no spaces will be entered thus striip is not needed
    single line A values only'''

# *** Practice values ***
A0 = "catinthehat"
D0 = {"ca", "tin", "inth", "it", "ehat", "th"}
# build(A0, D0) returns true
A1 = "ttttttttttt"
D1 = {"g", "a", "t"}
# returns true
A2 = "nowheretorunnow"
D2 = {"this", "will", "return", "false"}
# return false
A3 = "yttttttttttttttttttttttttttttttttttt"
D3 = {"g", "a", "t"}
# return false

# Arrays of probs for simpler testing
As = [A0, A1, A2, A3]
Ds = [D0, D1, D2, D3]

# Recursive alg with one arg, n
def build(n):
    if n == 0:
        return True
    for i in range(n):
        if A[i:n] in D:
            if build(i):
                return True
    return False

def buildDP(n):

    return True


for rep in range(4):
    A = As[rep]
    D = Ds[rep]
    print(build(len(A)))

print("===================================")


