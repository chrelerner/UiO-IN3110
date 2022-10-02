"""This file is used when invoked as `python -m instapy`"""

def main():
    from .cli import main
    main()

if __name__ == "__main__":
    from .cli import main

    main()
