class Solution {
    public String removeDigit(String number, char digit) {
        String s="";
        for(int i=0;i<number.length();i++){
            if(number.charAt(i)==digit){
                String st=number.substring(0,i)+number.substring(i+1);
                if(st.compareTo(s)>0){
                    s=st;
                }
            }
            }
            return s;
        }
        
    
}