class Solution:

    def encode(self, strs: List[str]) -> str:
        image = ""
        for word in strs:
            len_of_word = len(word)
            image += f"{len_of_word}#{word}"
            # image += str(len(word)) + "#" + word
        return image


    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j+1+length
        
        return res

