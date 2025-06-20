import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int sum = 0;

    while(true) {
      int a = sc.nextInt();
      int b = sc.nextInt();
      sum = a + b;
      if(sum == 0) break;
      System.out.println(sum);
    }

  }
}
