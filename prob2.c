#include<stdio.h>
#include<time.h>

int main(void)
{

long c = 0;
long res = 0;
struct timeval t;


long a=0;
long b=1;

while(c<4000000)
{
c= a+b;
a=b;
b=c;

if(c%2 == 0)
{
res = res+c;
}
}
printf("sum of even no %ld\n",res);
printf("time elapsed %d\n",t.tv_usec);
}

//best solution. :-)
