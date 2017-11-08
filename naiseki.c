#include <stdio.h>
#include <math.h>
int main() {
  double a0,a1,a2,b0,b1,b2;
    scanf("%lf %lf %lf %lf %lf %lf",&a0,&a1,&a2,&b0,&b1,&b2);
    printf("%f\n",(a0 * b0 + a1 * b1 + a2 * b2)/sqrt(a0*a0 + a1*a1 + a2*a2)/sqrt(b0*b0 + b1*b1 + b2*b2));
}
    
