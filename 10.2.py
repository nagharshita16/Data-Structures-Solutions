def AnagramSort(arr):
    list1 = [], list2 = []
    for i in len(arr):
        list2.append(arr[i])
        for j in len(arr):
            if i != j:
                if isAnagram(arr[i], arr[j]) == True:
                    list2.append(arr[j])
                    list2.pop(j)
                    j = j - 1
        list1 = list1 + list2
        list2 = []
    return list1

def isAnagram(A, B):
    A.sort()
    B.sort()
    if A == B:
        return True
    else:
        return False    


