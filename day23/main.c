#include <stdio.h>

int main(int argc, char **argv)
{
    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;
    int e = 0;
    int f = 0;
    int g = 0;
    int h = 0;

    a = 1;
    b = 84;
    c = b;

    b = b * 100;
    b = b + 100000;
    //b = 108553 - 17; <- first prime in list
    c = b;
    c = c + 17000;

start:
    f = 1;
    d = 2;

innerloop:
    e = 2;

    while (e != b)
    {
        if (b == (d * e))
        {
            printf("b = %d, d = %d, e = %d\n", b, d, e);
            f = 0;
        }

        e++;
    }

    d++;
    if (d != b)
        goto innerloop;
    if (f == 0) // if b isn't prime, increase h
    {
        h++;
    }
    printf("%d %d %d %d %d %d %d %d\n", a, b, c, d, e, f, g, h);

    if (b == c)
        goto end;

    b += 17;
    goto start;

end:
    printf("%d\n", h);

    return 0;
}