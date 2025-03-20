import java.util.Scanner;
public class ArraySort {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("输入要排序数列的数的个数");
		Scanner sc=new Scanner(System.in);
		int len=sc.nextInt();
		int a[]=new int[len];
		System.out.println("成员个数为"+len);
		for(int i=0;i<len;i++){
			a[i]=(int)(Math.random()*20);
		}
		System.out.println("显示数组值");
		for(int i=0;i<len;i++){
			System.out.print(a[i]+" ");
		}
		System.out.println("");
		for(int i=0;i<len;i++){
			for(int j=i+1;j<len;j++){
				if(a[i]<a[j]){
					int temp=a[i];
					a[i]=a[j];
					a[j]=temp;
				}
			}
		}
		System.out.println("显示排序数组值");
		for(int i=0;i<len;i++){
			System.out.print(a[i]+" ");
		}
		System.out.println("");
	}

}
