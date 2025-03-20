import java.util.Scanner;
public class c2 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		float[] a=new float[10];
		float sum,ave,max,min;
		Scanner sc=new Scanner(System.in);
		System.out.println("请依次输入十位同学的数学成绩：");
		for(int i=0;i<a.length;i++){
			a[i]=sc.nextFloat();
		}
		sum=0;
		max=a[0];
		min=a[0];
		for(int i=0;i<a.length;i++){
			sum+=a[i];
			if(a[i]>max){
				max=a[i];
			}
			if(a[i]<min){
				min=a[i];
			}
		}
		ave=sum/a.length;
		System.out.println("平均分"+ave+"最高分"+max+"最低分"+min);
	}

}
