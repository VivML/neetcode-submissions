class Solution {
    public boolean isAnagram(String s, String t) {
        // length same undha ledha chusukunna
        if(s.length()!=t.length()){
            return false;
        }
        // rendu strings ni same cases chesina
        s=s.toLowerCase();
        t=t.toLowerCase();
        //sort cheyyali char array ki marchi 
        // first char array and then sort
        char a1[]=s.toCharArray();
        char a2[]=t.toCharArray();
        // sort
        Arrays.sort(a1);
        Arrays.sort(a2);
        // compare to sorted arrays
        return Arrays.equals(a1,a2);
        
        }
    }

