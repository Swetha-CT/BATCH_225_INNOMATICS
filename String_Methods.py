class stringm:
    def __init__(self):
        pass

    #Ruthvi Gurram
    #upper
    def Upper(self,word):
        result = ""
        for char in word:
            if ord('a') <= ord(char) <= ord('z'):
                result += chr(ord(char) - 32)
            else:
                result += char
        return result
    
    #lower
    def Lower(self,word):
        result = ""
        for char in word:
            if ord('A') <= ord(char) <= ord('Z'):
                result += chr(ord(char) + 32)
            else:
                result += char
        return result
    
    #swapcase
    def Swapcase(word):
        result = ""
        for char in word:
            if ord('a') <= ord(char) <= ord('z'):
                result += chr(ord(char) - 32)
            elif ord('A') <= ord(char) <= ord('Z'):
                result += chr(ord(char) + 32)
            else:
                result += char
        return result
    
    #capitalize
    def Capitaliz(word):
        first_letter = word[0]
        second_letter =word[1::]
        if 'a' <= first_letter <= 'z':
            first_letter = chr(ord(first_letter) - 32)
        return first_letter + second_letter
    
    #Title
    def Title(word):
        result = ""
        text = True
        for char in word:
            if text and ord('a') <= ord(char) <= ord('z'):
                result += chr(ord(char) - 32)
                text = False
            elif char in [' ', '\t', '\n']:
                result += char
                text = True
            else:
                result += char.lower()
        return result
 
    #count
    def s_count(word,find_to):
        count = 0
        sub_len = len(find_to)
        str_len = len(word)
        for i in range(str_len - sub_len + 1):
            if word[i:i+sub_len] == find_to:
                count += 1
        return count
    
    #casefold
    def Casefold(word):
        casefolded_string = ''
        for char in word:
            if 'A' <= char <= 'Z':
                 # Convert uppercase letter to lowercase
                char = chr(ord(char) + 32)
            casefolded_string += char
        return casefolded_string
    
    #center
    def Center(word,wdt,fillin):
        if wdt <= len(word):
            return word
        pad = wdt - len(word)
        lp = pad// 2
        rp = pad - lp
        return fillin * lp + word + fillin * rp
    
    
    #startswith
    def Startw(word,pf):
        pfl = len(pf)
        sl = len(word)
        if pfl > sl:
            return False
        return word[:pfl] == pf
    
    #endswith
    def Endsw(word,sf):
        slen = len(sf)
        len_wrd = len(word)
        if slen > len_wrd:
            return False
        return word[len_wrd - slen:] == sf
    
    #expandtab
    def Exptab(word,tab_size):
        expanded_string = ''

        for char in word:
            if char == '\t':
                spaces_to_insert = tab_size - (len(expanded_string) % tab_size)
                expanded_string += ' ' * spaces_to_insert
            else:
                expanded_string += char

        return expanded_string
    
    #find
    def s_find(word,s_string):
        main_len = len(word)
        sub_len = len(s_string)

        for i in range(main_len - sub_len + 1):
            found = True
            for j in range(sub_len):
                if word[i+j] != s_string[j]:
                    found = False
                    break
            if found:
                return i
        return -1
    #index         
    def Index(self,word,subs:int):
        '''-------------- Mouni'''
        for i in range(len(word) - len(subs) + 1):
                if word[i:i+len(subs)] == subs:
                    return i
        raise ValueError('substring not found')
    #isalnum
    def Isaln(self,word):
        '''-------------- Mouni'''
        for ele in word:

            if not (65 <= ord(ele) <= 90 or 97 <= ord(ele) <= 122 or 48 <= ord(ele) <= 57):
                return False
        return True
    # isascii
    def Isascii(self,word):
        '''-------------- Manoj'''
        for ele in word:
            if ord(ele) > 127:
                return False
        return True
    #isalpha
    def Isalpha(self,word):
        '''-------------- Manoj'''
        for ele in word:
            if not (65 <= ord(ele) <= 90 or 97 <= ord(ele) <= 122):
                return False
        return True
    #isdigit
    def s_isdigit(self,word):
        '''-------------- Sai'''
        for ele in word:
            if not (48 <= ord(ele) <= 57):
                return False
        return True
    #islower
    def s_islower(self,word):
        '''-------------- Sai'''
        for ele in word:
            if not (97 <= ord(ele) <= 122):
                return False
        return True
    #isupper
    def s_isupper(self,word):
        '''-------------- Sonu'''
        for ele in word:
            if not (65 <= ord(ele) <= 90):
                return False
        return True
    # isnumeric
    def s_isnumaric(self,word):
        '''-------------- Sonu'''
        for ele in word:
            if not (48 <= ord(ele) <= 57):
                return False
        return True
    #join
    def Join(self,word,sep):
        '''-------------- Swetha'''
        result = ""
        for i in range(len(word)):
            result += word[i]
            if i != len(word) - 1:
                result += sep
        return result
    #ljust
    def Ljust(self,word,width):
        '''-------------- Swetha'''
        while len(word) < width:
            word += " "
        return word
    
    
    


















 #input area  
my_str = stringm() 
