# Can string A be built from the key values in D?
'''Assumptions made:
    spaces will be ignored
    no spaces will be entered thus striip is not needed
    single line A values only'''

# *** Practice values ***
A0 = "catinthehat"
D0 = ["ca", "tin", "inth", "it", "ehat", "th"]
# build(A0, D0) returns true
A1 = "ttttttttttt"
D1 = ["g", "a", "t"]
# returns true
A2 = "nowheretorunnow"
D2 = ["this", "will", "return", "false"]
# return false
A3 = "ttttttttttttttttttttttttttttttttttty"
D3 = ["g", "a", "t"]
# return false


# recursive solution
def build(A, D):
    if len(A) == 0:
        return True
    for i in D:
        l = len(i)
        if A[:l] == i:
            if build(A[l:], D):
                return True
    return False

As = [A0, A1, A2, A3]
Ds = [D0, D1, D2, D3]
for prob in range(4):
    print(build(As[prob], Ds[prob]))
