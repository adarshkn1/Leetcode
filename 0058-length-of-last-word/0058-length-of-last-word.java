class Solution {
    public int lengthOfLastWord(String s) {
        String[] newone = s.trim().split(" ");
        int n = newone.length;

        return (newone[n-1].length());
    }
}