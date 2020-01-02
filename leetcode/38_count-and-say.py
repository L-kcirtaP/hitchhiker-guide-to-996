class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        last_seq = self.countAndSay(n - 1)
        seq = ""
        count = 0
        length = len(last_seq)
        for i, char in enumerate(last_seq):
            count += 1
            if i < length - 1 and last_seq[i + 1] != char:
                seq += str(count) + str(char)
                count = 0
            if i == length - 1:
                seq += str(count) + str(char)
        return seq
