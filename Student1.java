
public class Student1 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][]a=new int[3][];
		for(int i=0;i<a.length;i++){
			int data=(int)(10*Math.random());
			a[i]=new int[data];
			System.out.println("***��"+(i+1)+"�꼶��"+a[i].length+"���༶��***");
			for(int j=0;j<data;j++){
				a[i][j]=(int)(5*Math.random()+25);
				System.out.print((j+1)+"����"+a[i][j]+"��ѧ��");
			}
		System.out.print("\n");
		}
		
		
	}	

}
