def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    hashtable = {} # initialize empty dictionary

    result = [] # intitalize empty list to add intersections

    for i in arrays:
        for e in i: 
            if e not in hashtable: 
                hashtable[e] = 1 # amt of e in hashtable 
            else: 
                hashtable[e] += 1 # add intersection to hashtable
                if hashtable[e] == len(arrays): # if intersection in every array
                    result.append(e) # add intersection to result 
    

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
