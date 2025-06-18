import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int h = sc.nextInt(); // 현재 시각 (시)
    int m = sc.nextInt(); // 현재 시각 (분)
    int t = sc.nextInt(); // 요리 시간 (분)

    m += t;            // 전체 분 계산
    h += m / 60;       // 시에 올려줌
    m = m % 60;        // 60분 넘어간 부분 잘라줌
    h = h % 24;        // 24시 넘어간 부분 조정

    System.out.println(h + " " + m);
  }
}
