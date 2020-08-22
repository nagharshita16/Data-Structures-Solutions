counter = 0
def Merge(A, B):
    i,j = 0, 0
    while j < len(B):
        if A[i] == NULL:
            A[i] = B[j]
            i = i + 1 
            j = j + 1
        if A[i] > B[j]:
            Shift(A, counter)
            A[i] = B[j]
            i +=1
            j +=1
        else:
            i = i + 1
        counter =  counter + 1    
    return A    
     

def Shift(A. counter):
    while A[i] != NULL:
        c = c + 1
        i = i - 1
    length = len(A) - c
    i = length - 1
    while i != counter - 1:
        A[i+1] = A[i]
        i = i - 1   
