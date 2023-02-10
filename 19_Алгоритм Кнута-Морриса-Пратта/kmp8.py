from ext import Ext


class KMP:
    pi = []

    def create_pi_slow(self, pattern: str) -> None:
        self.pi = [0] * (len(pattern) + 1)
        for q in range(len(pattern) + 1):
            line = Ext.left(pattern, q)
            for l in range(q):
                if Ext.left(line, l) == Ext.right(line, l):
                    self.pi[q] = l

    def create_pi_fast(self, pattern: str) -> None:
        self.pi = [0] * (len(pattern) + 1)
        self.pi[1] = 0
        for q in range(1, len(pattern)):
            l = self.pi[q]
            while l > 0 and pattern[l] != pattern[q]:
                l = self.pi[l]
            if pattern[l] == pattern[q]:
                l += 1
            self.pi[q + 1] = l


if __name__ == '__main__':
    auto = KMP()
    auto.create_pi_fast('AABAABAAABA')
    print(auto.pi)
