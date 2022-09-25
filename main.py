import os
import re
import shutil
import sys

CONTENT_TYPES_DIR = "content-types"
EXTENSIONS_DIR = "extensions"


def main() -> None:
    shutil.rmtree(CONTENT_TYPES_DIR)
    shutil.rmtree(EXTENSIONS_DIR)
    os.makedirs(CONTENT_TYPES_DIR, exist_ok=True)
    os.makedirs(EXTENSIONS_DIR, exist_ok=True)

    data = sys.stdin.read()
    match = re.match(r"^\s*types\s*{(.*)}\s*$", data, re.MULTILINE | re.DOTALL)
    assert match
    data_inner: str = match.group(1)
    rules = data_inner.strip().strip(";").split(";")
    for rule in rules:
        content_type, *extensions = rule.strip().split()
        #
        # content-type => extension
        #
        assert content_type.count("/")
        main_type = content_type.split("/")[0]
        os.makedirs(f"{CONTENT_TYPES_DIR}/{main_type}", exist_ok=True)
        with open(f"{CONTENT_TYPES_DIR}/{content_type}", "w") as f:
            print(extensions[0], file=f)

        #
        # extension => content-type
        #
        for extension in extensions:
            with open(f"{EXTENSIONS_DIR}/{extension}", "w") as f:
                print(content_type, file=f)


if __name__ == "__main__":
    main()
