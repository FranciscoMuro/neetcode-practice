class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> storeCount = new HashMap<>();
        for (int number : nums) {
            if (storeCount.containsKey(number)) {
                storeCount.put(number, storeCount.get(number) + 1);
            } else {
                storeCount.put(number, 1);
            }
        }

        // Convert HashMap to List of Map.Entry
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(storeCount.entrySet());

        // Sort the list by keys
        list.sort(Map.Entry.comparingByValue());

        int[] result = new int[k];
        int resultIndex = 0;
        while (k > 0) {
            result[resultIndex] = list.get(list.size() - k).getKey();
            resultIndex++;
            k--;
        }
        return result;
    }
}
