#include<stdio.h>
#include<math.h>
int main()
{
	int a,b,c,area;
	printf("enter values of a,b,c:\n");
	scanf("%d %d %d",&a,&b,&c);
	if (a+b>c && b+c>a && a+c>b)
	{
	area=(a+b+c)/2;
	printf("area of triangle of given sides:%d",area);
    }
	else
	printf("inputs invalid");
	return 0;
	
}
