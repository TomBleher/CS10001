# Skeleton file for HW1 - Spring 2024 - Extended Intro to CS

# Add your implementation to this file

# Replace the 'pass' command with your implementation in each function.
# you may NOT change the signature of the existing functions.
# you can add new functions if needed.

# Change the name of the file to include your ID number (hw1_ID.py).


# Question 4a
def union_strings(str1,str2):
	
	# initialize list to hold the letters which appear in the input strings
	present_letters = []
	
	try: 
		assert len(str1)>=0 and len(str2)>= 0
	
		# Check if character in input strings 
		for char1, char2 in zip(str1, str2):
			if char1 not in present_letters: 
				present_letters.append(char1)
			else:
				pass
	
			if char2 not in present_letters: 
				present_letters.append(char2)
			else:
				pass			
					
		# after we checked for the characters in the strings, return
		return present_letters
		
	except AssertionError as e:
		print(f"Please enter a non-empty string \n {e}")

# Question 4b
def format_str(text_to_format, st_to_insert):
    try:
        # require that the input will be proper
        assert isinstance(text_to_format, str)
        assert isinstance(st_to_insert, str)
        assert len(text_to_format) > 0 
        assert len(st_to_insert) > 0

        # initialize as the input
        formatted_text = []
    
        # loop over all characters of the string
        for idx, char in enumerate(text_to_format):
        
            # if this is the character we want to replace
            if char == "?":
                # replace the character ? with st_to_insert
                formatted_text.append(st_to_insert)
            else:
                # otherwise, add the original character
                formatted_text.append(char)

        # join the list into a single string
        formatted_text = ''.join(formatted_text)

        # return the formatted_text
        return formatted_text
        
    except AssertionError as e:
        print(f"Please enter a proper string \n {e}")


# Question 4c
def least_pal(text):
    # initialize empty 
    text_reversed = []

    try:
        # require that the input will be proper
        assert isinstance(text, str)
        assert len(text) > 0 
        
        # initialize number of impurities
        k=0

        # convert to reverse string
        text_reversed = text[::-1]

        # if the strings are equal, they are a palindrome of k=0
        if text == text_reversed:
            k = 0

        # if not perfect, calculate number of needed fixes (fix is only a change of character)
        else:
            for iter_idx, (char, rev_char) in enumerate(zip(text, text_reversed)):
                
                # we only want to check for half the string
                if iter_idx >= len(text)/2:
                    break
                    
                if char != rev_char:
                    k+=1

        # return the amount of strings needed to be replaced
        return k 
        
    except AssertionError as e:
        print(f"Please enter a proper string \n {e}")

# Question 4d
def least_frequent(text):
    
    # initiate a dictionary to hold the count for each character
    char_count = {   
    
        }
    
    try:
        # require that the input will be proper
        assert isinstance(text, str)
        assert len(text) > 0 

        for char in text:
            # for the first round initiate the keys and ints 
            if char not in list(char_count.keys()):
                char_count[char] = 1
                
            # for the later rounds, add to the count for each letter
            else: 
                char_count[char] += 1
        
        # get the min reapeting variable
        min_char_rep = min(char_count.values())
        
        # get key from value - somewhat of a bad code, but I have a lot of psets to hand in 
        min_char = list(char_count.keys())[list(char_count.values()).index(min_char_rep)]
            
        return min_char

    except AssertionError as e:
        print(f"Please enter a proper string \n {e}")


# Question 4e
def longest_common_suffix(lst):
    
    try:
        
        # require that the inputs will be proper
        assert isinstance(lst, list)
        assert len(lst) > 0 
        
        # an item will always share all characters with itself
        if len(lst) == 1:
            return lst[0]
        
        # also require that the items will be proper 
        for item in lst:
            assert isinstance(item, str)
            assert len(item) > 0
        
        # initiate string for final result
        shared_suffix = ''
        
        # find the length of the shortest item in the input list 
        min_char_len = min(len(item) for item in lst)
        
        # loop over length of the shortest item, start from 1 since we use reverse indexing
        for i in range(1, min_char_len):
            
            # check the intercection (logical and) of the condition for all items in list
            if all(item[-i] == lst[0][-i] for item in lst):
                shared_suffix += lst[0][-i]
            
            # stop when we arrived at a place where the characters do not match
            else:
                break
        
        # since we started from the last index, it makes sense to return the reversed
        return shared_suffix[::-1]

    except AssertionError as e:
        print(f"Please enter a non-empty list with non-empty strings \n {e}")  


# Question 4f
def is_int(text):

    try:
        
        # require that the inputs will be proper
        assert isinstance(text, str)
        assert len(text) > 0
        
        # define the integers that are strings
        string_ints = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        # initiate the bool check for the validity of each character in text
        string_bool = []
        
        for iter_idx, char in enumerate(text):
            
            # if the first char is zero in a multi-int string it is invalid
            if iter_idx==0 and char=='0' and len(text)!=1:
                string_bool = [False]
                break
            
            # it is a valid string integer
            if char in string_ints:
                string_bool.append(True)
            
            # it is an invalid character
            else: 
                string_bool.append(False)
        
        # will only return True if all the characters are valid
        return all(string_bool)
                
    except AssertionError as e:
        print(f"Please enter a non-empty string \n {e}")


# Question 4g (Optional)
def merge(text1, text2):
    pass


# Question 5a
def is_anagram(st1, st2):
    
    try:
        
        # require that the inputs will be proper
        assert isinstance(st1, str)
        assert isinstance(st2, str)        
        
        assert len(st1) > 0 
        assert len(st2) > 0         
        
        st1_chars = []
        st2_char_bools = []

        for char1 in st1:
            st1_chars.append(char1)
        
        for char2 in st2:
            if char2 in st1_chars:
                st2_char_bools.append(True)
            else:
                st2_char_bools.append(False)
        
        # will only return true if all characters of st2 meet the requirements        
        return all(st2_char_bools)

    except AssertionError as e:
        print(f"Please enter non-empty strings \n {e}")  


# Question 5b
def is_anagram_v2(st1, st2):
    for ch in st1+st2:
        if st1.count(ch) != st2.count(ch):
            return False
    return True


# Question 5c
def is_anagram_v3(st1, st2):
	return sorted(st1)==sorted(st2)


# Question 6a
def eval_mon(monomial, val):
    pass


# Question 6b
def eval_pol(polynomial, val):
    pass


########
# Tester
########

def test():
    # Testing Q4
    if "".join(sorted(union_strings("aabcccdde", "bccay"))) != "abcdey":
        print("error in union_strings - 1")
    if "".join(sorted(union_strings("aabcccdde", ""))) != "abcde":
        print("error in union_strings - 2")

    if format_str("I2?", "CS") != "I2CS":
        print("error in format_str - 1")
    if format_str("???", "W") != "WWW":
        print("error in format_str - 2")
    if format_str("ABBC", "z") != "ABBC":
        print("error in format_str - 3")

    if least_pal("abcdefgh") != 4:
        print("error in least_pal - 1")
    if least_pal("radarr") != 2:
        print("error in least_pal - 2")
    if least_pal('race car') != 1:
        print("error in least_pal - 3")
    if least_pal('tenat') != 1:
        print("error in least_pal - 4")

    if least_frequent('aabcc') != 'b':
        print("error in least_frequent - 1")
    if least_frequent('aea.. e') != ' ':
        print("error in least_frequent - 2")
    if least_frequent('zzz') != 'z':
        print("error in least_frequent - 3")

    if longest_common_suffix(["abccdba", "cba", "zaba"]) != "ba":
        print("error in longest_common_suffix - 1")
    if longest_common_suffix(["hello", "world"]) != "":
        print("error in longest_common_suffix - 2")
    if longest_common_suffix(["intro", "maestro"]) != "tro":
        print("error in longest_common_suffix - 3")
    if longest_common_suffix(["intro"]) != "intro":
        print("error in longest_common_suffix - 4")

    if is_int("12x"):
        print("error in is_int - 1")
    if is_int("-0"):
        print("error in is_int - 2")
    if not is_int("42"):
        print("error in is_int - 3")

    if merge("abcd", "") != "abcd":
        print("error in merge - 1")
    if merge("aabbddfgk", "adkox") != "aaabbdddfgkkox":
        print("error in merge - 2")

    # Testing Q5
    if not is_anagram("tommarvoloriddle", "iamlordvoldemort"):
        print("error in is_anagram - 1")
    if is_anagram("abce", "abcd"):
        print("error in is_anagram - 2")
    if not is_anagram("listen", "silent"):
        print("error in is_anagram - 3")

    if not is_anagram_v2("tommarvoloriddle", "iamlordvoldemort"):
        print("error in is_anagram_v3 - 1")
    if is_anagram_v2("abce", "abcd"):
        print("error in is_anagram_v3 - 2")
    if not is_anagram_v2("listen", "silent"):
        print("error in is_anagram_v3 - 3")

    if not is_anagram_v3("tommarvoloriddle", "iamlordvoldemort"):
        print("error in is_anagram_v3 - 1")
    if is_anagram_v3("abce", "abcd"):
        print("error in is_anagram_v3 - 2")
    if not is_anagram_v3("listen", "silent"):
        print("error in is_anagram_v3 - 3")

    # Testing Q6
    if eval_mon("+5x^3", 4) != 320:
        print("error in eval_mon - 1")
    if eval_mon("-5x^0", 1000) != -5:
        print("error in eval_mon - 2")
    if eval_mon("+1x^10", 2) != 1024:
        print("error in eval_mon - 3")

    if eval_pol("+5x^3-4x^2+7x^1-5x^0+10x^11", 4) != 41943319:
        print("error in eval_pol - 1")
    if eval_pol("+1x^0+1x^1+1x^2+1x^3+1x^4+1x^5", 5) != 3906:
        print("error in eval_pol - 2")
    if eval_pol("+11x^0+1x^1+1x^2+1x^3+1x^4+1x^5", 2) != 73:
        print("error in eval_pol - 3")

    print("`test()` completed.")
