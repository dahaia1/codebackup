
public class ArrayCopy2 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] array1=new int[]{3,2,5,1,4};
		int[] array2=java.util.Arrays.copyOf(array1,array1.length);
		for(int i=0;i<array2.length;i++){
			System.out.print(array2[i]+"  ");
		}
	}

}
