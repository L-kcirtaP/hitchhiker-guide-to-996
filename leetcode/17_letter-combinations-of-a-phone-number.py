class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        mapping = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }
        n_letters = 1
        for digit in digits:
            n_letters *= len(mapping[digit])
        ret = [''] * n_letters
        for digit in digits:
            mapping_list = [letter for letter in mapping[digit]] * int(n_letters / len(mapping[digit]))
            ret.sort()
            for i in range(n_letters):
                ret[i] = ret[i] + mapping_list[i]
        return sorted(ret)
