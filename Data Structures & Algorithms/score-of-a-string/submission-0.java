class Solution {
    public int scoreOfString(String s) {
     int sum=0;
     for (int i=0;i<s.length()-1;i++){
        int a=i;
       int b=i+1;
        char first =s.charAt(a);
        char second =s.charAt(b);
        int a_ascii= first;
        int b_ascii=second;
        int temp=Math.abs(a_ascii-b_ascii);
        sum=sum+temp;
     }
     return sum;
    }
}