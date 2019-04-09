#include <stdio.h>
#include <math.h>

double trianglen(int n)
{
  return (n*(n+1))/2;
}

int main(void)
{
  double trianglen(int n);
  double alotn[20000];
  int arrayofnumbers[20000], numdivisor[20000];
  int i, id;
  for ( i = 0; i < 20000; ++i )
  arrayofnumbers[i] = i + 1;
  for ( i = 0; i < 20000; ++i )
  alotn[i] = trianglen(arrayofnumbers[i]);
  for ( i = 0; i < 20000; ++i )
  numdivisor[i] = 0;
  for ( i = 0; i < 20000; ++i ){
  for ( id = 1; id<=((int) sqrt(alotn[i])); ++id )
  if ( (int) alotn[i]%id==0 )
  ++numdivisor[i];
  }
  for (i = 0; i < 20000; ++i)
  if (numdivisor[i]>250) // imperfect if the triangular number is a perfect square
  printf("%f\n", alotn[i]);
  return 0;
  }
