#include<stdio.h>

int main(void)
{
int i=0;
int s3=0;
int s5=0;
int s15=0;
int res=0;

while(s3<1000)
{
i++;
s3 = s3+3;
sum= sum+s3;
}

printf("multiple of 3 %d\n",i-1);
printf("sum of 3 %d\n",s3);
i=0;

while(s5<1000)
{
i++;
s5 = s5+5;

}

printf("multiple of 5 %d\n",i-1);

i=0;

while(s15<1000)
{
i++;
s15 = s15+15;


}

printf("multiple of 15 %d\n",i-1);

i=0;

res= s3+s5-s15;

printf("result--> %d",res);


}
