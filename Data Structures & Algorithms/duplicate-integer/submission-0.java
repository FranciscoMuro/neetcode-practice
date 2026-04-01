class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> storeCount = new HashMap<>();
        if(nums.length == 0) return false;
        if(nums.length == 1) return false;

        for (int j : nums) {
            if (storeCount.containsKey(j)) {
                storeCount.put(j, storeCount.get(j) + 1);
            } else {
                storeCount.put(j, 1);
            }
        }
        for(Map.Entry<Integer, Integer> entry : storeCount.entrySet()) {
            if(entry.getValue() > 1) {
                return true;
            }
        }
        return false;
    }
}
