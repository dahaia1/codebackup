import java.util.Scanner;
public class sum1 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i=1,sum=0,n;
		Scanner sc=new Scanner(System.in);
		System.out.println("请输入一个正整数：");
		n=sc.nextInt();
		while(i<=n){sum+=i;i++;}
		System.out.println("1到"+n+"之间的累加和为："+sum);

	}

}
