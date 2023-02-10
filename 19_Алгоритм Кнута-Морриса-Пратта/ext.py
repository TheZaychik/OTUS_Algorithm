class Ext:
    @staticmethod
    def left(line: str, x: int) -> str:
        return line[0:x]

    @staticmethod
    def right(line: str, x: int) -> str:
        return line[len(line) - x: len(line)]