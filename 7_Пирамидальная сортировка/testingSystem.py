from os import listdir
from os.path import isfile, join
import re

class TestingSystemMk2:
    """
    Класс для тестирования домашних заданий
    Формат работы - создание объекта с директорией тестов
    Название файлов теста - test.[0-9].in и test.[0-9].out
    Запуск теста с передачей тестируемой функции
    """

    def __init__(self, test_path: str) -> None:
        self.test_path = test_path
        self._setup_files()
        self.test_count = len(self.files)
        self.test_passed = 0
        self.test_failed = 0

    def _setup_files(self):
        self.files = [f for f in listdir(self.test_path) if isfile(join(self.test_path, f))]
        regex = re.compile(r'^test\.\d\.in$')
        self.files = list(filter(regex.search, self.files))
        self.files.sort()
        print(self.files)

    def run_test(self, testing_class, func: str) -> None:
        for in_f in self.files:
            print('-------------------------')
            out_f = in_f.replace('.in', '.out')
            try:
                with open(join(self.test_path, in_f), 'r') as f:
                    N = int(f.readline())
                    in_mas = [int(s) for s in str(f.readline()).split(' ')]
                with open(join(self.test_path, out_f), 'r') as f:
                    out_mas = [int(s) for s in str(f.readline()).split(' ')]
            except Exception as e:
                print('Ошибка при чтении файла:', str(e))
                self.test_failed += 1
                continue
            print(f'Тестовый входной файл: {in_f}')
            print(f'Тестовый выходной файл: {out_f}')
            t = testing_class(in_mas)
            getattr(t, func).__call__()
            if t.mas == out_mas:
                print('Тест пройден')
                self.test_passed += 1
            else:
                print('Тест не пройден')
                self.test_failed += 1
        print('-------------------------')
        print(f'Итого:\nВсего тестов: {self.test_count}, пройдено: {self.test_passed}, завалено: {self.test_failed}')
