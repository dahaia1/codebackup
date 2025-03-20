import java.util.*;
public class c5 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n1=1,n2=1,temp;
		Scanner sc=new Scanner(System.in);
		System.out.print("请输入要查看第n个数中的n值：");
		int num=sc.nextInt();
		System.out.print(n1+",");
		for(int i=2;i<num;i++){
			n1=n1+n2;
			temp=n1;
			n1=n2;
			n2=temp;
			System.out.print(n1+",");
		}
		System.out.println("第"+num+"个数为"+n2);
	}

}
