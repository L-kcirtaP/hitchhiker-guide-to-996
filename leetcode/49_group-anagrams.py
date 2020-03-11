alpha2prime = {
    'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19,
    'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53,
    'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89,
    'y': 91, 'z': 101,
}

from functools import reduce

def groupAnagrams(strs):
    from functools import reduce
    if len(strs) == 0:
        return [[]]

    anagram_dict = {} 

    for string in strs:
        hash_val = 1
        for char in string:
            hash_val *= alpha2prime[char]
        anagram_dict[hash_val] = anagram_dict.get(hash_val, []) + [string]

    return [anagram_dict[key] for key, _ in anagram_dict.items()]
