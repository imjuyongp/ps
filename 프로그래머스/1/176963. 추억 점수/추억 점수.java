import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] result = new int[photo.length];
        HashMap<String,Integer> map = new HashMap<>();
        
        for (int i=0; i<name.length; i++) {
            map.put(name[i], yearning[i]); // 이름 : 추억 점수 HashMap으로 저장
        }
        
        for (int i=0; i<photo.length; i++) {
            int sum=0;
            for(int j=0; j<photo[i].length; j++) {
                if(map.containsKey(photo[i][j])) {
                    sum += map.get(photo[i][j]);
                }
            }
            result[i] += sum;
        }
        
        return result;
    }
}