import java.util.Scanner;
public class sum1 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i=1,sum=0,n;
		Scanner sc=new Scanner(System.in);
		System.out.println("������һ����������");
		n=sc.nextInt();
		while(i<=n){sum+=i;i++;}
		System.out.println("1��"+n+"֮����ۼӺ�Ϊ��"+sum);

	}

}
