def reverse(self, x: int) -> int:
    if x == 0:
        return 0
    if x > 0:
        res = 0
        while x > 0:
            remian = x % 10
            x = x // 10
            res = remian + res * 10
        if res > pow(2, 31) - 1:
            return 0
        else:
            return res
    if x < 0:
        x = -x
        res = 0
        while x > 0:
            remian = x % 10
            x = x // 10
            res = remian + res * 10
        if -res < -pow(2, 31):
            return 0
        else:
            return -res
            