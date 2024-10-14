#include <stdio.h>

int main()
{
        int nb = 21;
        int temp = 0;
        while (temp != 20)
        {
                for(int i = 1; i <= 20; i++)
                {
                        temp = i;
                        if (nb % i != 0)
                        {
                                break;
                        }
                }
                nb++;
        }
        printf("%d\n", nb - 1);
        return 0;
}
