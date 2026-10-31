class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=''
        char_store=[]
        length=[]
        for i in s :
            while i in char:
                index=char.index(i)
                char=char[index+1::]
            char=char+i
            char_store.append(char)
        #print(char_store)
        for i in char_store:
            length.append(len(i))
        try:
            return (max(set(length)))
        except Exception as e: 
            return 0
            




