//2b
//public class Digisum{
//	public static void main(String args[]){
//	int n=Integer.parseInt(args[0]);
//	System.out.println("Input:"+n);
//	System.out.print("Output:");
//	int sum=0,r=0;
//		while(n!=0){
//			r= n%10;
//			sum=sum+r;
//			n=n/10;
//		}
//	System.out.println(sum);
//	}
//}




//LAB WEEK 1
//1
import java.util.*;
	public class Digisum{
		public static void main(String args[]){
		Scanner scn=new Scanner(System.in);
		System.out.print("Input:");
		int n=scn.nextInt();
		System.out.print("Output:");
		int sum=0,r=0;
		while(n!=0){
			r= n%10;
			sum=sum+r;
			n=n/10;
		}
	System.out.println(sum);
	}
}