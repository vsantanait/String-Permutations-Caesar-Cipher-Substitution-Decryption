# Problem Set 4B
# Name: Vanessa Santana


import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        
        return self.message_text
        

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        
        return self.valid_words.copy()
        

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        try:
        
            assert (shift >= 0) and (shift < 26)
            
            uppercase_alphabet = string.ascii_uppercase
            lowercase_alphabet = string.ascii_lowercase
            
            shift_dict = {}
            
            uletter_index = -1
            new_uletter_index = -1
            
            lletter_index = -1
            new_lletter_index = -1
            
            
            for char in uppercase_alphabet:
                uletter_index = uppercase_alphabet.find(char)
                
                if (shift == 25):
                    new_uletter_index = (uletter_index + shift)%26
                
                elif (uletter_index + shift) < len(uppercase_alphabet):
                    new_uletter_index = (uletter_index + shift)
                    
                else:
                    new_uletter_index = (uletter_index + shift)%25 - 1
                
                shift_dict[char] = uppercase_alphabet[new_uletter_index]
                
                
            for char in lowercase_alphabet:
                lletter_index = lowercase_alphabet.find(char)
                
                if (shift == 25):
                    new_lletter_index = (lletter_index + shift)%26
                
                elif (lletter_index + shift) < len(lowercase_alphabet):
                    new_lletter_index = (lletter_index + shift)
                    
                else:
                    new_lletter_index = (lletter_index + shift)%25 - 1
                    
                shift_dict[char] = lowercase_alphabet[new_lletter_index]
    
            return shift_dict
            
                    
        except:
            
            print("Invalid shift value! Please enter a shift value")
            print(" greater than or equal to zero, and less that 26.")
            

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        try:
        
            assert (shift >= 0) and (shift < 26)
            
            shift_dict = Message.build_shift_dict(self, shift)
            shift_mess_text = ""
            
                    
        except:
            
            print("Invalid shift value! Please enter a shift value")
            print(" greater than or equal to zero, and less that 26.")
            
        try:
            assert len(self.message_text) > 0
            
            for char in self.message_text:
                
                if char.isalpha():
                    shift_mess_text = shift_mess_text + shift_dict[char]
                else:
                    shift_mess_text = shift_mess_text + char
                    
            return shift_mess_text
                    
        except:
            print("Invalid message! Please enter a valid message to encrypt.")
        

class PlaintextMessage(Message):
    
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        
        return self.shift
        

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        
        return self.encryption_dict.copy()
        

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        
        return self.message_text_encrypted
        

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        
        try:
            assert (shift >= 0) and (shift < 26)
            
            self.shift = shift
            self.encryption_dict = Message.build_shift_dict(self, shift)
            self.message_text_encrypted = Message.apply_shift(self, shift)
            
            
        except:
            
            print("Invalid shift value! Please enter a shift value")
            print(" greater than or equal to zero, and less that 26.")
            
        


class CiphertextMessage(Message):
    
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        # Message.__init__(self, text)
        PlaintextMessage.__init__(self, text, 0)
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        decrypt_tuple = () #RETURN VALUE
        decrypted_dict = {} #DICTIONARY of ORIGINAL shift value and DECRYPTED message
        
        word_list = self.get_valid_words()
        
        # encrypted_text = self.get_message_text()
        # decrypted_obj = PlaintextMessage(encrypted_text, 0)
        
        
        for i in range(1, 26): # 0 - 25, 
            shift = 26 - i

            decrypted_msg = self.apply_shift(shift)
            # print("i: " + str(i))
            # print("shift: " + str(shift))
            # print("decrypted_msg: " + decrypted_msg)
            
            if decrypted_msg.count(" ") > 0:
                decrypted_list = decrypted_msg.split(" ")
            
                count = 0
                for word in decrypted_list:
                    if word.lower() in word_list:
                        count += 1
                
                decrypted_dict[shift] = ((count, decrypted_msg),)
                
                            
            else:
                if decrypted_msg.lower() in word_list:
                    decrypted_dict[shift] = ((1, decrypted_msg),)

                    
                else:
                    decrypted_dict[shift] = ((0, decrypted_msg),)
                    
        # print(decrypted_dict)

                
        max_val = 0      
        for j in decrypted_dict.keys():
            # if j > 1:

            ((i, text),) = decrypted_dict[j]
            max_val = max(i, max_val)
            
            if (max_val == i):
                decrypt_tuple = (j, text)
                    
    
        
        for j in decrypted_dict.keys():
            ((i, text),) = decrypted_dict[j]
            
            # print("decrypt_tuple[0]: " + str(decrypt_tuple[0]))
            # print("decrypted_dict[j]: " + str(decrypted_dict[j]))
            
            # print(len(decrypt_tuple))
            if (len(decrypt_tuple) == 2):
                if (i >= max_val) and (decrypt_tuple[1] != text):
                    decrypt_tuple = (decrypt_tuple,) + decrypted_dict[j]
            else:
                ((k, sub_text),) = decrypt_tuple[0]
                if (i >= max_val) and (sub_text != text):
                    decrypt_tuple = (decrypt_tuple,) + decrypted_dict[j]
        
        
        return decrypt_tuple
        

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    # plaintext = PlaintextMessage('hello', 2)
    # print('Expected Output: jgnnq')
    # print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    # ciphertext = CiphertextMessage('jgnnq')
    # print('Expected Output:', (24, 'hello'))
    # print('Actual Output:', ciphertext.decrypt_message())
    # print()
    
    #TODO: WRITE YOUR TEST CASES HERE
    
    #Example test case (PlaintextMessage)
    # plaintext = PlaintextMessage('HeLlO', 2)
    # print('Expected Output: JgNnQ')
    # print('Actual Output:', plaintext.get_message_text_encrypted())
    
    #Example test case (CiphertextMessage)
    # ciphertext = CiphertextMessage('JGNNQ')
    # print('Expected Output:', (24, 'HELLO'))
    # print('Actual Output:', ciphertext.decrypt_message())

    #TODO: best shift value and unencrypted story 
    
    # story_file = open("story.txt", "r")
    # story_text = story_file.read()
    # story_file.close()
    
    text = get_story_string()
    ciphertext = CiphertextMessage(text)
    
    print("CiphertextMessage(text).decrypt_message(): " + str(ciphertext.decrypt_message()))
    
    # print("CiphertextMessage(text).get_message_text_encrypted()" + ciphertext.get_message_text_encrypted()) #AttributeError: 'CiphertextMessage' object has no attribute 'get_message_text_encrypted'
    
    #TEST RESULT
    # Loading word list from file...
    #    55901 words loaded.
    # CiphertextMessage(text).decrypt_message(): (12, 'Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed aclass. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.')
        
    
