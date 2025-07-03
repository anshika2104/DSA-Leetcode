class Solution {
    public boolean canThreePartsEqualSum(int[] arr) {
         int s=0;
        for(int i:arr){
            s+=i;
        }
        if(s%3!=0){
            return false;
        }
        int each=s/3,t=0,count=0;
        for(int i=0;i<arr.length;i++){
            t=t+arr[i];
            if(t==each){
                t=0;
                count++;
            }
        }
        if(count>=3){
            return true;
        }
        return false;
    }
}