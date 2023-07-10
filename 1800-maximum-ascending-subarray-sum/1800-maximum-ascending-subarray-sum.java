class Solution {
    public int maxAscendingSum(int[] nums) {
        int sum = nums[0], maxSum = sum;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                sum += nums[i];
            } else {
                if (maxSum < sum) {
                    maxSum = sum;
                }
                sum = nums[i];
            }
        }
        if (maxSum < sum) {
            maxSum = sum;
        }
        return maxSum;
    }
}