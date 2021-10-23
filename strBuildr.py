# Can string A be built from the key values in D?
'''Assumptions made:
    spaces will be ignored
    no spaces will be entered thus striip is not needed
    single line A values only'''

# Practice values
A = "catinthehat"
D = ["ca", "tin", "inth", "it", "ehat", "th"]
# build(A, D) returns true

def build(A, D):
    if len(A) == 0:
        return True
    for i in D:
        l = len(D[i])
        if A[:l] == D[i]:
            if build(A[:l], D):
                return True
    return False
