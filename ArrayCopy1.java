
public class ArrayCopy1 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] array1=new int[]{3,2,5,1,4};
		int[] array2=new int[5];
		System.arraycopy(array1,0,array2,0,array1.length);
		for(int i=0;i<array2.length;i++){
			System.out.print(array2[i]+"  ");
		}
	}

}
