import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(); // 바구니 개수
    int m = sc.nextInt(); // 공을 넣을 횟수
    int[] arr = new int[n];
    int[] input = new int[3];
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < 3; j++) {
        input[j] = sc.nextInt();
      }
      for (int j = input[0]-1; j <= input[1]-1; j++) {
        arr[j] = input[2];
      }
    }

    for (int i = 0; i < n; i++) {
      System.out.print(arr[i] + " ");
    }
  }
}
