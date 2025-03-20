
public class c7 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int distance=0;
		int day=1;
		while(true){
			distance+=2;
			if(distance>=10){
				break;
			}
			distance-=1;
			day++;
		}
		System.out.println("蜗牛在第"+day+"天爬到了井口");
	}

}
