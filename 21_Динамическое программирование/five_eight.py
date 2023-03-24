"""
Дано число N.
Выяснить сколько N-значных чисел можно составить
используя числа 5 и 8, в которых три одинаковые цифры не стоят друг за другом.
    Scanner con = new Scanner(System.in);

    int n = con.nextInt();

    m[1] = 2; m[2] = 4;

    for(int i = 3; i <= n; i++) m[i] = m[i-1] + m[i-2];

    System.out.println(m[n]);
"""


def five_eight(n: int) -> int:
    n_map = [0] * n
    n_map[0] = 2
    n_map[1] = 4
    for i in range(2, n):
        n_map[i] = n_map[i - 1] + n_map[i - 2]
    return n_map[n - 1]


if __name__ == '__main__':
    N = 4
    print(five_eight(N))
