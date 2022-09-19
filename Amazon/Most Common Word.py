class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        #To remove puntuation
      
        paragraph=re.sub(r'[^\w\s]', ' ', paragraph).split()
            
          
        word_tracker = {}
        banned_words_dict={}
        
        for i in paragraph:
                word_tracker[i]=word_tracker.get(i,0)+1
        for i in banned:
            if banned and word_tracker.get(i):
                word_tracker.pop(i)
            
        max=0
        max_word = ''
        for i in list(word_tracker.keys()):
            if max < word_tracker[i]:
                max=word_tracker[i]
                max_word = i
        return max_word     
       
