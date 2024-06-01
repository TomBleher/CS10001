

# question 4.a
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



# question 4.b
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


# question 4.c
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

# question 4.d
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

# question 4.e
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

# question 4.f
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


# question 5.a