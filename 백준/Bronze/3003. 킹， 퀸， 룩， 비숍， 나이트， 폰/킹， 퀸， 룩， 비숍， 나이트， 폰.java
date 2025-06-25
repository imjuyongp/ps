import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int[] chess = new int[6];
    chess[0] = 1;
    chess[1] = 1;
    chess[2] = 2;
    chess[3] = 2;
    chess[4] = 2;
    chess[5] = 8;
    int[] arr = new int[6];
    for (int i = 0; i < arr.length; i++) {
      arr[i] = sc.nextInt();
    }
    for (int i = 0; i < arr.length; i++) {
      int count = chess[i] - arr[i];
      System.out.print(count + " ");
    }

  }
}
