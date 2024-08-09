/* C言語版 */

#include <stdio.h>

int main(void) {
    int a, b, c;
    char s[101];

    // 入力
    scanf("%d", &a);
    scanf("%d %d", &b, &c);
    scanf("%s", &s);

    // 出力
    printf("%d %s\n", a+b+c, s);

    return 0;
}