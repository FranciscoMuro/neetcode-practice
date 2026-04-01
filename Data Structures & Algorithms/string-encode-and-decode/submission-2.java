class Solution {

    public String encode(List<String> strs) {
        if (strs.isEmpty()) return "";
        StringBuilder codedString = new StringBuilder();
        for (String str : strs) {
            codedString.append(str).append("/");
        }
        return codedString.toString();
    }

    public List<String> decode(String str) {
        if (str.length() == 0) {
            return new ArrayList<>();
        } else if (str.equals("/")) {
            return Arrays.asList("");
        }
        return Arrays.asList(str.split("/"));
    }
}
