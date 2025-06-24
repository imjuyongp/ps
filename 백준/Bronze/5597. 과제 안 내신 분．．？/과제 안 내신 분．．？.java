import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int[] arr = new int[30];
    for (int i = 0; i < 28; i++) {
      int x = sc.nextInt();
      for (int j = 0; j < arr.length; j++) {
        arr[x-1] = x;
      }
    }
    for (int i = 0; i < 30; i++) {
      if(arr[i] == 0){
        System.out.println(i+1);
      }
    }
  }
}
