

import os
from detector import find_duplicates


folder_path = input("Enter folder path: ")

if not os.path.isdir(folder_path):

    print("Invalid folder path!")

else:

    duplicates = find_duplicates(folder_path)

    if not duplicates:

        print("\nNo duplicate files found.")

    else:

        print("\nDuplicate files found:\n")

        for group in duplicates:

            print("Duplicate Group:")

            for file in group:
                print(" -", file)

            print()

        print("Total duplicate groups:", len(duplicates))

        extra_copies = sum(
            len(group) - 1 for group in duplicates
        )

        print("Extra duplicate files:", extra_copies)
