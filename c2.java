import java.util.Scanner;
public class c2 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a,b,max;
		Scanner sc=new Scanner(System.in);
		System.out.println("�������һ��������");
		a=sc.nextInt();
		System.out.println("������ڶ���������");
		b=sc.nextInt();
		if(a>b){max=a;}else{max=b;}
		System.out.println("���ֵ�ǣ�"+max);
	}

}
