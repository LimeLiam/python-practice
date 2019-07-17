#Dot product function for vectors

def dotProduct(vec1, vec2):
    assert(len(vec1) == len(vec2))
    m = 0
    for i in range(len(vec1)):
        m += vec1[i] * vec2[i]
    return m

def dotAnd(A, B):
    return dotProduct([1,1,-1.5], [int(A), int(B), 1]) > 0

def dotOr(A, B):
    return dotProduct([1,1,-0.5], [int(A), int(B), 1]) > 0

def exOr(A,B):
    return dotProduct([-3,1,1], [int(dotOr(A, B)), int(dotAnd(A, B))]
