class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        lookup = set()
        for u, v in similarPairs:
            lookup.add((u, v))
            lookup.add((v, u))
            
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            elif (w1, w2) in lookup:
                continue
            else:
                return False
        return True


"""
Input: sentence1 = ["great"], sentence2 = ["great"], similarPairs = []
Output: true

Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
Output: true

Input: sentence1 = ["great"], sentence2 = ["great"], similarPairs = []
Output: False

"""