import os
import time
from send2trash import send2trash

PATH = 'C:\\Users\\proje\\Downloads'
DOWNLOADS_DIR = os.chdir(PATH)
DOWNLOADS_LIST = os.listdir(DOWNLOADS_DIR)
LIST_EXTENSIONS = ['.zip', '.rar', '.7z', '.jpg', '.png']
EXTENSIONS = tuple(LIST_EXTENSIONS)


def get_removed_list(_downloads_list):
    return [dl for dl in _downloads_list if dl.endswith(EXTENSIONS)]


def get_removed_paths(_removed_list):
    _removed_paths = [os.path.join(PATH, i) for i in _removed_list]
    return _removed_paths


def main():
    print('Listing files to be removed: \n')
    time.sleep(1)

    removed_list = get_removed_list(DOWNLOADS_LIST)
    number_of_removed = len(removed_list)
    removed_paths = get_removed_paths(removed_list)

    for i in removed_list:
        print(i)

    if number_of_removed == 0:
        print('Nothing to remove!')
        time.sleep(2)
        exit()
    else:
        print('\nNumber of files to be removed is:', number_of_removed)
        time.sleep(2)

    while True:
        choice = input('\nWould you like to remove these files? y/n: ')

        if choice == 'y' or choice == 'Y':
            print('Sending', number_of_removed, 'file(s) to the trash!')
            send2trash(removed_paths)
            time.sleep(2)
            break

        if choice == 'n' or choice == 'N':
            print('Exiting now...')
            time.sleep(1)
            break


if __name__ == '__main__':
    main()
