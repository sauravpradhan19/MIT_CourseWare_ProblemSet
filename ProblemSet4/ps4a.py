# Problem Set 4A
# Name: Saurav Pradhan
# Collaborators:None
def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence)==1:
        return sequence
    smaller_sequence=get_permutations(sequence[:-1])
    new=[]
    for word in smaller_sequence:
        for i in range(len(word)+1):
            if word[:i]+sequence[-1:]+word[i:] not in new:
                new.append(word[:i]+sequence[-1:]+word[i:])
    return new


if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'aaa'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
     #delete this line and replace with your code here

