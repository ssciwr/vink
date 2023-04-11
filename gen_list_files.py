"""
This script generates 2 lists of NSIS commands (install & uninstall)
for all files in a given directory, which is passed on the command line.
"""

import os
import sys

# Input:
ROOT = sys.argv[1]

# Calculate total installation size
accumulated_size = 0

# Write the two scripts while crawling the file system
with open("install_files.nsh", "w") as i:
    with open("uninstall_files.nsh", "w") as u:
        for root, _, files in os.walk(ROOT, topdown=False):
            print(
                f'SetOutPath "$INSTDIR{os.path.sep}{os.path.relpath(root, ROOT)}"',
                file=i,
            )
            for fname in files:
                print(f'File "{root}{os.path.sep}{fname}"', file=i)
                print(
                    f'Delete "$INSTDIR{os.path.sep}{os.path.relpath(root, ROOT)}{os.path.sep}{fname}"',
                    file=u,
                )
                accumulated_size += os.stat(os.path.join(root, fname)).st_size
            print(f'RMDir "$INSTDIR{os.path.sep}{os.path.relpath(root, ROOT)}"', file=u)

        # Export the accumulated installation size
        print(f"!define INSTALLSIZE {accumulated_size // 1024}", file=i)
