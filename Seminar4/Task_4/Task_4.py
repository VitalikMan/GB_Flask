# Задание:
# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# Используйте потоки.
import os.path
import threading
import time


PATH = "test"
count = 0


def get_amount_worlds(filename: str) -> None:
    global count
    with open(filename, encoding="utf-8") as f:
        count += len(f.read().split())
        time.sleep(0.1)
    print(f"Сейчас значение счётчика на файле {filename}: {count}")


def main():
    threads = []
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            thread = threading.Thread(target=get_amount_worlds, args=(file_path,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    print(f"Финальное значение счётчика: {count}")


if __name__ == "__main__":
    main()
