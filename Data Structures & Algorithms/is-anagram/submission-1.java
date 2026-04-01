class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        Map<String, Integer> storeLettersS = new HashMap<>();
        Map<String, Integer> storeLettersT = new HashMap<>();
        String[] sArray = s.split("");
        String[] tArray = t.split("");
        for (int i = 0; i < s.length(); i++) {
            if (storeLettersS.containsKey(sArray[i])) {
                storeLettersS.put(sArray[i], storeLettersS.get(sArray[i]) + 1);
            } else {
                storeLettersS.put(sArray[i], 1);
            }
        }
        for (int i = 0; i < s.length(); i++) {
            if (storeLettersT.containsKey(tArray[i])) {
                storeLettersT.put(tArray[i], storeLettersT.get(tArray[i]) + 1);
            } else {
                storeLettersT.put(tArray[i], 1);
            }
        }

        for (Map.Entry<String, Integer> entry : storeLettersS.entrySet()) {
            if(storeLettersT.containsKey(entry.getKey()) && Objects.equals(storeLettersT.get(entry.getKey()), entry.getValue())){
                continue;
            } else {
                return false;
            }
        }

        return true;
    }
}
