
public class c4 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int count=0;
		int i,j;
		boolean isPrime;
		for(i=2;i<=100;i++){
			isPrime=true;
			int g=(int)Math.sqrt(i);
			for(j=2;j<=g;j++){
				if(i%j==0){
					isPrime=false;
					break;
				}
			}
		if(isPrime){
			System.out.print(i+"    ");
			count++;
		}
		}
		System.out.println();
		System.out.println("找到的质数个数："+count);
	}

}
