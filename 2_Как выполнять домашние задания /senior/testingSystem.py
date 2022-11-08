from os import listdir
from os.path import isfile, join
import re

class TestingSystem:
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

    def run_test(self, func) -> None:
        for in_f in self.files:
            print('-------------------------')
            out_f = in_f.replace('.in', '.out')
            try:
                with open(join(self.test_path, in_f), 'r') as f:
                    in_parameter = int(f.readline())
                with open(join(self.test_path, out_f), 'r') as f:
                    out_parameter = int(f.readline())
            except Exception as e:
                print('Ошибка при чтении файла:', str(e))
                self.test_failed += 1
                continue
            print(f'Тестовый входной файл: {in_f}, значение {in_parameter}')
            print(f'Тестовый выходной файл: {out_f}, значение {out_parameter}')
            out = func(in_parameter)
            print(f'Полученное значение {out}\nОжидаемое значние {out_parameter}')
            if out == out_parameter:
                print('Тест пройден')
                self.test_passed += 1
            else:
                print('Тест не пройден')
                self.test_failed += 1
        print('-------------------------')
        print(f'Итого:\nВсего тестов: {self.test_count}, пройдено: {self.test_passed}, завалено: {self.test_failed}')
