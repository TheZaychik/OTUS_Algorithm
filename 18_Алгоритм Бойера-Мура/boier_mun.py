class Search:
    @staticmethod
    def search_full_scan(text: str, mask: str) -> int:
        t = 0
        while t <= (len(text) - len(mask)):
            m = 0
            while (m < len(mask)) and (text[t + m] == mask[m]):
                m += 1
            if m == len(mask):
                return t
            t += 1
        return -1

    @staticmethod
    def search_reverse_scan(text: str, mask: str) -> int:
        t = 0
        while t <= (len(text) - len(mask)):
            m = len(mask) - 1
            while (m >= 0) and (text[t + m] == mask[m]):
                m -= 1
            if m < 0:
                return t
            t += 1
        return -1

    @staticmethod
    def search_bmh(text: str, mask: str) -> int:
        shift = Search.create_shift(mask)
        t = 0
        while t <= (len(text) - len(mask)):
            m = len(mask) - 1
            while (m >= 0) and (text[t + m] == mask[m]):
                m -= 1
            if m < 0:
                return t
            t += shift[ord(text[t + len(mask) - 1])]
        return -1

    @staticmethod
    def create_shift(mask: str) -> list:
        shift = [len(mask)] * 128
        for m in range(len(mask) - 1):
            shift[ord(mask[m])] = len(mask) - m - 1
        return shift


if __name__ == '__main__':
    text = 'STRONGSTRING'
    # text = 'ABC@ABBDABCABABCD'
    mask = 'RING'
    # mask = 'ABCD'
    print(Search.search_bmh(text, mask))
