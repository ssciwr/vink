"""
This script generates 2 lists of NSIS commands (install&uninstall)
for all files in a given directory.

Usage:
    gen_list_files_for_nsis.py <dir src>
Where
    <dir src>       :   dir with sources; must exist
"""

import os
import sys

# Input:
ROOT = sys.argv[1]

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
                    f'Delete "$INSTDIR{os.path.sep}{root}{os.path.sep}{fname}"', file=u
                )
            print(f'RMDir "$INSTDIR{os.path.sep}{root}"', file=u)
