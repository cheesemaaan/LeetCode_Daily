class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_idx = word.find(ch)
        answer = word
        if ch_idx != -1:
            answer = word[ch_idx::-1]+word[ch_idx+1::]

        return answer