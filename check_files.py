#!/usr/bin/python

import os
import sys
import hashlib


def _generate_file_hash(path):
    f = open(path, 'rb')
    buffer = f.read()
    h = hashlib.md5()
    h.update(buffer)
    f.close()
    return h.hexdigest()


def print_duplicated_files(results):
    if len(results) > 0:
        for result in results:
            print('{}'.format(result))

    else:
        print('No duplicate files found.')


def check_duplication(path):
    files = set()
    duplicated_files = set()

    for filename in os.listdir(path):
        hash = None
        p = os.path.join(path, filename)

        if os.path.isdir(p):
            check_duplication(p)
        else:
            hash = _generate_file_hash(p)
        if hash is not None and hash not in files:
            files.add(hash)
        elif hash is not None:
            duplicated_files.add(p)
    print_duplicated_files(duplicated_files)


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        if not os.path.exists(path):
            print('%s is not a valid path, please verify' % path)
            sys.exit()
    except IndexError:
        print "Usage: myprogram.py <directory>"
        sys.exit(1)

    # check_file function
    check_duplication(path)
