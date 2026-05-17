class Solution {
    public boolean hasDuplicate(int[] nums) {
        int len = nums.length;
        HashMap <Integer, Integer> hm = new HashMap<>(); 
        for(int i = 0; i<len; i++){
            if(hm.containsKey(nums[i]) == false){
                hm.put(nums[i], 1);
            } else
            {
                return true;
            }
        }
        return false;
    }
}