#include <stdio.h>
#include <math.h>

int main(void)
{
long num = 600851475143;
long st = 600851475143/6;

while(1)
{

if(  ((num % (6*st-1)) == 0 ) || ((num % (6*st+1)   ) == 0 )) 
break;

st--;

}
printf("no is %ld",6*st+1);
}
