class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> storeIndex = new HashMap<>();

        for (int i = 0 ; i < nums.length; i++) {
            if (storeIndex.containsKey(target - nums[i])) {
                result[0] = storeIndex.get(target - nums[i]);
                result[1] = i;
                return result;
            }
            storeIndex.put(nums[i], i);
        }



        return result;
    }
}
