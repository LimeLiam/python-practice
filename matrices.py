import numpy

def matriply(A,B):
    wA = A.shape[1]
    hA = A.shape[0]
    wB = B.shape[1]
    hB = B.shape[0]

    assert wA == hB

    #hA wB for zeroes function, because height goes before width here and that is how they are inherited.
    blankMatrix = numpy.zeros((hA, wB))    

    for i in range(numpy.ndarray.tolist(A)):
        return i
        
