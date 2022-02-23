def isSequence(arr, seqs):
    #build list of subarrays
    res = [arr[i: j] for i in range(len(arr))
          for j in range(i + 1, len(arr) + 1)]
    
    s = [] # initialize empty array
    for e in seqs:
        if e in res:
            s.append(e) # fill with matching elements 
    
    s1 = set() # build solution set
    
    for e in s:
        print(e)
        for e2 in e:
            s1.add(e2) # add to set
    
    # convert to set
    s2 = set(arr)
    
    if s1 == s2:
        return True
    else:
        return False

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5,]
    seqs = [[1, 2], [3, 4], [5]]
    answer = isSequence(arr, seqs)
    print(answer)