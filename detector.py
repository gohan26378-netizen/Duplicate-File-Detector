
import os
import hashlib


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def find_duplicates(folder_path):

    hash_map = {}

    for root, dirs, files in os.walk(folder_path):

        for filename in files:

            file_path = os.path.join(root, filename)

            try:
                file_hash = calculate_hash(file_path)

                if file_hash not in hash_map:
                    hash_map[file_hash] = []

                hash_map[file_hash].append(file_path)

            except OSError as error:
                print("Cannot read:", file_path, error)

    duplicates = []

    for file_list in hash_map.values():

        if len(file_list) > 1:
            duplicates.append(file_list)

    return duplicates
