def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    hashtable = {} # initialize empty dictionary

    for i, v in enumerate(weights):

        # hash table contains an entry for weight limit - weight value
        if limit - v in hashtable:

            # index of second value
            pair = hashtable.get(limit-v), i
            return tuple(sorted(pair, reverse=True))

        # if not in hashtable, create entry 
        else:

            hashtable[v] = i
    return None
