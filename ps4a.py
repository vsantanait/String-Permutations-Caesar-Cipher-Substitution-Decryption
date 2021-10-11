# Problem Set 4A
# Name: Vanessa Santana


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
    
    if len(sequence) == 1:
        return [sequence]
    
    prev_list = get_permutations(sequence[1:len(sequence)])
    next_list = []

    for i in range(0, len(prev_list)):
        for j in range(0, len(sequence)):

            new_sequence = prev_list[i][0:j] + sequence[0] + prev_list[i][j:len(sequence) - 1]
            if new_sequence not in next_list:
                next_list.append(new_sequence)
                
    return next_list
    

def test_get_permutations():
    """
    Unit test for get_permutations

    Parameters 
    ----------
    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    Returns
    -------
    a list of all permutations of sequence

    """
    
    failure=False
    
    
    # test 1
    sequence = "abc"
    permutation_test1 = get_permutations(sequence)
    
    if str(permutation_test1) != "['abc', 'bac', 'bca', 'acb', 'cab', 'cba']":
        print("FAILURE: TEST1 of test_get_permutations(sequence), where sequence = 'abc'")
        print("\tExpected ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'], but got " + str(permutation_test1))
        
        failure = True
        return # exit function
    
    
    # test 2
    sequence = "bust"
    permutation_test2 = get_permutations(sequence)
    permutation_test2_result = "['bust', 'ubst', 'usbt', 'ustb', 'bsut', 'sbut', 'subt', 'sutb', 'bstu', 'sbtu', 'stbu', 'stub', 'buts', 'ubts', 'utbs', 'utsb', 'btus', 'tbus', 'tubs', 'tusb', 'btsu', 'tbsu', 'tsbu', 'tsub']"
    
    if str(permutation_test2) != permutation_test2_result:
        print("FAILURE: TEST2 of test_get_permutations(sequence), where sequence = 'bust'")
        print("\tExpected " +  permutation_test2_result +  " but got " + str(permutation_test2))
        
        failure = True
        return # exit function
    
    
    # test 3
    sequence = "zebra"
    permutation_test3 = get_permutations(sequence)
    permutation_test3_result = "['zebra', 'ezbra', 'ebzra', 'ebrza', 'ebraz', 'zbera', 'bzera', 'bezra', 'berza', 'beraz', 'zbrea', 'bzrea', 'brzea', 'breza', 'breaz', 'zbrae', 'bzrae', 'brzae', 'braze', 'braez', 'zerba', 'ezrba', 'erzba', 'erbza', 'erbaz', 'zreba', 'rzeba', 'rezba', 'rebza', 'rebaz', 'zrbea', 'rzbea', 'rbzea', 'rbeza', 'rbeaz', 'zrbae', 'rzbae', 'rbzae', 'rbaze', 'rbaez', 'zerab', 'ezrab', 'erzab', 'erazb', 'erabz', 'zreab', 'rzeab', 'rezab', 'reazb', 'reabz', 'zraeb', 'rzaeb', 'razeb', 'raezb', 'raebz', 'zrabe', 'rzabe', 'razbe', 'rabze', 'rabez', 'zebar', 'ezbar', 'ebzar', 'ebazr', 'ebarz', 'zbear', 'bzear', 'bezar', 'beazr', 'bearz', 'zbaer', 'bzaer', 'bazer', 'baezr', 'baerz', 'zbare', 'bzare', 'bazre', 'barze', 'barez', 'zeabr', 'ezabr', 'eazbr', 'eabzr', 'eabrz', 'zaebr', 'azebr', 'aezbr', 'aebzr', 'aebrz', 'zaber', 'azber', 'abzer', 'abezr', 'aberz', 'zabre', 'azbre', 'abzre', 'abrze', 'abrez', 'zearb', 'ezarb', 'eazrb', 'earzb', 'earbz', 'zaerb', 'azerb', 'aezrb', 'aerzb', 'aerbz', 'zareb', 'azreb', 'arzeb', 'arezb', 'arebz', 'zarbe', 'azrbe', 'arzbe', 'arbze', 'arbez']"
    
    if str(permutation_test3) != permutation_test3_result:
        print("FAILURE: TEST3 of test_get_permutations(sequence), where sequence = 'zebra'")
        print("\tExpected " +  permutation_test3_result +  ", but got " + str(permutation_test3))
        
        failure = True
        return # exit function
    
    
    if not failure:
        print("SUCCESS: TEST1 passed! test_get_permutations(sequence), where sequence = 'abc'")
        print("SUCCESS: TEST2 passed! test_get_permutations(sequence), where sequence = 'bust'")
        print("SUCCESS: TEST3 passed! test_get_permutations(sequence), where sequence = 'zebra'")
        
# end of test_get_permutations()


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
    test_get_permutations()

    
    
    


