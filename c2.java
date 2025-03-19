import java.util.Scanner;
public class c2 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a,b,max;
		Scanner sc=new Scanner(System.in);
		System.out.println("请输入第一个整数：");
		a=sc.nextInt();
		System.out.println("请输入第二个整数：");
		b=sc.nextInt();
		if(a>b){max=a;}else{max=b;}
		System.out.println("最大值是："+max);
	}

}
