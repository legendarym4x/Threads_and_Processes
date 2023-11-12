from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

source = Path(input('Enter the source folder1 path: '))
output = Path(input('Enter the output folder1 path (default is "sorted"): '))

folders = []


def parse_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            parse_folder(el)


def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = output / ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder / el.name)
            except OSError as err:
                logging.error(err)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')

    folders.append(source)
    parse_folder(source)
    print(folders)

    threads = []
    for folder in folders:
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print(f'The folder1 >>>{source}<<< can be deleted!')
