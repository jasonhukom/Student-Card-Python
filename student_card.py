import sys

def main():
    args = sys.argv
    if len(args) < 2:
        sys.exit("Too few arguments! Please read README.md")
    
    len_args = 6
    for arg in args:
        len_args += len(arg[1:])

    line = "=" * len_args

    print(f"""{line}
Name: {" ".join(args[1:])}
{line}""")

if __name__ == "__main__":
    main()