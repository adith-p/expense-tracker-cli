import argparse

def main():
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers()

    add_parsers = sub_parsers.add_parser("add")
    add_parsers.add_argument("-d","--description")
    add_parsers.add_argument("--amount",type=int)

    args = parser.parse_args()

    print(args.description)

if __name__ == "__main__":
    main()