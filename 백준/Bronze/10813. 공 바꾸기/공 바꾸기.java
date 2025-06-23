import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(); // 바구니 개수
    int m = sc.nextInt(); // 공을 바꿀 횟수
    int[] arr = new int[n];
    for (int i = 0; i < arr.length; i++) {
      arr[i] = i+1;
    }
    for (int i = 0; i < m; i++) {
      int a = sc.nextInt();
      int b = sc.nextInt();
      int k = arr[a-1];
      arr[a-1] = arr[b-1];
      arr[b-1] = k;
    }
    for (int i = 0; i < arr.length; i++) {
      System.out.print(arr[i] + " ");
    }
  }
}
