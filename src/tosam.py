import argparse

def main():
    argparser = argparse.ArgumentParser(description="To Simple-SAM converter")
    argparser.add_argument(
        "mas",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()
    print(args)
    for line in args.mas:
        chrom, read_name, read_str, pos = line.split('\t')

        print(read_name, chrom, pos.strip(), read_str, sep = '\t')
        # Output as Simple-SAM


if __name__ == '__main__':
    main()
