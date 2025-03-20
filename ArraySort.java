
public class ArraySort {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] array=new int[]{3,2,5,10,4};
		java.util.Arrays.sort(array);
		for(int i=0;i<array.length;i++){
			System.out.print(array[i]+"  ");
		}
	}

}
