import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();

    int a = n * (m%10);
    int b = n * (m%100/10);
    int c = n * (m/100);

    int result = a + b*10 + c*100;

    System.out.println(a);
    System.out.println(b);
    System.out.println(c);
    System.out.println(result);
  }
}