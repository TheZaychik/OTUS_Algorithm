from ext import Ext


class Auto:
    alphabet = 'ABC'
    pattern = ''
    delta = []

    def create_delta(self, pattern: str):
        self.pattern = pattern
        self.delta = [[0] * len(self.alphabet)] * len(pattern)
        for q in range(0, len(pattern)):
            for c in self.alphabet:
                line = Ext.left(pattern, q) + c
                k = q + 1
                while Ext.left(pattern, k) != Ext.right(line, k):
                    k -= 1
                self.delta[q][ord(c) - ord(self.alphabet[0])] = k

    def search(self, text: str) -> int:
        q = 0
        for i in range(0, len(text)):
            q = self.delta[q][ord(text[i]) - ord(self.alphabet[0])]
            if q == len(self.pattern):
                return i - len(self.pattern) + 1
        return -1


if __name__ == '__main__':
    auto = Auto()
    auto.create_delta('AABAABAAABA')
    x = auto.search('AABAABAAABA')
    print(x)
