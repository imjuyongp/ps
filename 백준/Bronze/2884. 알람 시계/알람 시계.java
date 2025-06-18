import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int H = sc.nextInt();
      int M = sc.nextInt();

      if(0<=H && H <= 23 && 0<=M && M <= 59) {
        if(M > 45) {
          M = M - 45;
        } else if(M < 45) {
          H = H - 1;
          if(H < 0) {
            H = 23;
          }
          M = M + 15;
        } else if(M == 45) {
          M = 0;
        }
      }
    System.out.println(H + " " + M);
    }

}