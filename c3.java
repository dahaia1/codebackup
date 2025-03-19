import java.util.Scanner;
public class c3 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a,b,c;
		System.out.println("请输入三角形三条边：");
		Scanner sc=new Scanner(System.in);
		System.out.println("a=：");
		a=sc.nextInt();
		System.out.println("b=：");
		b=sc.nextInt();
		System.out.println("c=：");
		c=sc.nextInt();
		if((a+b)>c&&(a+c)>b&&(b+c)>a){System.out.println(a+","+b+","+c+"能构成三角形");}else{System.out.println(a+","+b+","+c+"能构成三角形");}
	}

}
