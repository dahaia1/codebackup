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
		System.out.println("������Բ�İ뾶��");
		Scanner sc=new Scanner(System.in);
		r=sc.nextInt();
		area=PI*r*r;
		perimeter=2*PI*r;
		System.out.println("Բ�������"+area);
		System.out.println("Բ���ܳ���"+perimeter);
	}

}
