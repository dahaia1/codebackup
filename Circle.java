import java.util.Scanner;
public class Circle {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int r;
		float area,perimeter;
		final float PI=3.14f;
		System.out.println("请输入圆的半径：");
		Scanner sc=new Scanner(System.in);
		r=sc.nextInt();
		area=PI*r*r;
		perimeter=2*PI*r;
		System.out.println("圆的面积："+area);
		System.out.println("圆的周长："+perimeter);
	}

}
