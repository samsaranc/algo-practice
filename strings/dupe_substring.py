def rev_ll_rec(head):
    
    if head.next == None:
        return head.val

    else: 
        head.val = rev_ll_rec(head.next)

def dupe_substr (substr):

    #pairwise comparison
    for k in range(0, len(substr)-1):
        for l in range(k+1, len(substr)):
            if (substr[k] == substr[l]):
                flag = False
                break;

            else:
                flag = True
        if (flag == False): break;

    return flag

def BRUTE_lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if (len(s) == 0 or len(s) ==1 ): return len(s);
    
    flag = False
    longest = 1
    
    for window in range(2,len(s)+1):
        for i in range(0, len(s)-window+1):
            j = i + window
            substr = s[i:j]
            
            #pairwise comparison
            for k in range(0, len(substr)-1):
                for l in range(k+1, len(substr)):
                    if (substr[k] == substr[l]):
                        flag = False
                        break;

                    else:
                        flag = True
                if (flag== False): break;
            
            if flag:
                longest = len(substr)
                flag = False
                break;
                
    return longest

 #returns true if chars in substr are unique
def set_allUnique(s,start, end):
    flag = True

    if (len(s) > 1) :
        st = {s[start]}
        for i in range(start+1 , end+1):
            if ({s[i]}.issubset(st)):
                flag = False
                break;
            else:
                st.add(s[i])
    
    return flag;

def lengthOfLongestSubstring( s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 0 or len(s) ==1 ): return len(s);

        longest = 1
        
        for i in range(0,len(s)):
            for j in range(i+1, len(s)):
                f = allUnique(s,i,j)
                print (s, i ,j,f )
                if f:
                    longest = max(longest, j-i+1)
                    print(j , i, j-i)
        
        return longest

#assumes end is NOT a valid index
#returns true if chars in substr are unique
def allUnique(s,start, end):
    
    flag = True

    if (len(s) > 1) :
        st = {s[start]}
        for i in range(start +1 , end+1):
            # print({s[i]}.issubset(st),s[i],st)
            if ({s[i]}.issubset(st)):
                # print("oooooooo",s[i],st)
                flag = False
                break;
            else:
                st.add(s[i])

    return flag;

def gold(word):
    if not word: return 0

    currentLength = 1
    longest = 1
    last_seen = {word[0] : 0}
    i = 1

    while i < len(word):
        letter = word[i]
        if letter in last_seen:
            i = last_seen[letter] + 1
            last_seen.clear()
            longest = max(longest, currentLength)
            currentLength = 0
        else:
            last_seen[letter] = i
            currentLength += 1
            i += 1

    longest = max(longest, currentLength)

    return longest

if __name__ == '__main__':
    # print(dupe_substr("yello"))
    # print(dupe_substr("hi"))
    # print(set_allUnique("yel", 0, 2))

    # print(set_allUnique("hi", 0,1))
    # print(set_allUnique("bmafwsahcpwthjqmajrtlaykcwidwoixcifadfjfwgafrquscllpmlaoiktgacgdmlfpsrwozxvqppirbthphjfr", 0,87))
    print(lengthOfLongestSubstring("yelllo"))
    print(lengthOfLongestSubstring("yelo"))

    print(lengthOfLongestSubstring("zuvckrvtmihlhnbbgycnxthqtskcjgakbypnrkhduqqcdsfksjzscjivbtzmbzxezosrabwurnywhdizmktqtcnuxmjyoidpwxg"))
    print(gold("zuvckrvtmihlhnbbgycnxthqtskcjgakbypnrkhduqqcdsfksjzscjivbtzmbzxezosrabwurnywhdizmktqtcnuxmjyoidpwxg"))

    # print(lengthOfLongestSubstring("bmafwsahcpwthjqmajrtlaykcwidwoixcifadfjfwgafrquscllpmlaoiktgacgdmlfpsrwozxvqppirbthphjfr"))
    # print(len("bmafwsahcpwthjqmajrtlaykcwidwoixcifadfjfwgafrquscllpmlaoiktgacgdmlfpsrwozxvqppirbthphjfr"))