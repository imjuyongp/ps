import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int h = sc.nextInt();
    int m = sc.nextInt();
    int t = sc.nextInt();

    if(0<=h && h<=23 && 0<=m && m<=59){
      h = h + (t/60);
      if(h>23) {
        h = h - 24;
      }
      m = m + (t%60);
      if(m >= 60) {
        h = h + (m/60);
        if(h>23) {
          h = h - 24;
        }
        m = m % 60;
      }else if(m == 60) {
        h = h + 1;
        m = 0;
      }
    }

    System.out.println(h + " " + m);
  }
}