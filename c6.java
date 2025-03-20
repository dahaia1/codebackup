
public class c6 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int cock,hen,chick;
		for(cock=0;cock<=20;cock++){
			for(hen=0;hen<=33;hen++){
				for(chick=3;chick<=99;chick+=3){
					if(5*cock+3*hen+chick/3==100){
						if(cock+hen+chick==100){
							System.out.println("¹«¼¦£º"+cock+"\tÄ¸¼¦£º"+hen+"\tÐ¡¼¦£º"+chick);
						}
					}
				}
			}
		}
	}

}
