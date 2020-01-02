class Solution {
    public List<String> generateParenthesis(int n) {
        
        List<List<String>> parens = new ArrayList<>();
        List<String> zero_list = Arrays.asList("");

        if (n < 1) { return zero_list; }

        parens.add(zero_list);
        for (int i = 1; i < n + 1; i++) {
            List<String> n_list = new ArrayList<>();
            for (int start = 0; start < i; start++) {
                for (String s1: parens.get(start)) {
                    for (String s2: parens.get(i - start - 1)) {
                        n_list.add('('+s1+')'+s2);
                    }
                }
            }
            parens.add(n_list);
        }

        return parens.get(n);
    }
}
