class Solution {
    public void moveZeroes(int[] nums) {
        int l = 0;
        int n = nums.length;
        int temp = 0;
        for(int r = 0;r < n;r++){
            if(nums[r]!=0){
                temp = nums[r];
                nums[r] = nums[l];
                nums[l] = temp;
                l+=1;
            }
        }
        for(int num:nums){
            System.out.print(num);
        }
    }
}