import java.util.Scanner;
public class a6 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int x=2,n=1;
		System.out.println("请输入要计算的幂数：");
		int end=sc.nextInt();
		while(n<end){x=x*2;n++;System.out.println("2的"+n+"次幂是："+x);}
	}

}
