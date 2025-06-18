import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int[] array = new int[a];

    for (int i = 0; i < a; i++) {
      int n = sc.nextInt();
      int m = sc.nextInt();
      int k = n + m;
      array[i] = k;
    }

    for(int i = 0; i < array.length; i++){
      System.out.println(array[i]);
    }



  }
}
