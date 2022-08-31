import argparse

def main():
    argparser = argparse.ArgumentParser(description="To Simple-SAM converter")
    argparser.add_argument(
        "mas",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()
    # print(args)
    i = 0
    for line in args.mas:
        l = ['3M', '3M', '6M']
        chrom, read_name, read_str, pos = line.split('\t')

        print(read_name.strip(), chrom.strip(), str(int(pos)+1), l[i], read_str.strip(), sep = '\t')
        i+=1
        # Output as Simple-SAM


if __name__ == '__main__':
    main()
