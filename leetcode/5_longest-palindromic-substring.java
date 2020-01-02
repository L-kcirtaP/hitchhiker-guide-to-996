class Solution {
    
    public String longestPalindrome(String s) {
        String s_with_sharp = "#";
        String LPS_with_sharp = "#";
        int len = s.length();
        for (int i = 0; i < len; i++) {
            s_with_sharp += s.charAt(i) + "#";
        }
        int start, end;
        for (int i = 1; i < 2 * len; i++){
            start = i - 1;
            end = i + 1;
            while (start >= 0 && end <= 2 * len && s_with_sharp.charAt(start) == s_with_sharp.charAt(end)) {
                if (s_with_sharp.substring(start, end + 1).length() > LPS_with_sharp.length()) {
                    LPS_with_sharp = s_with_sharp.substring(start, end + 1);
                }
                start -= 1;
                end += 1;
            }
        }
        String LPS = "";
        for (int i = 1; i < LPS_with_sharp.length(); i += 2) {
            LPS += LPS_with_sharp.charAt(i);
        }
        return LPS;
    }
}
