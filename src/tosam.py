import argparse

# HELP PLEASE! I don't understand what format this is supposed to be outputted in.
# From the test-tosam.sh file i gather that the result will be compared to 
# mississippi.sam. The sam-file has an extra column with the CIGAR which isn't
# available in mississippi.mas. I'm not sure what to do.

def main():
    argparser = argparse.ArgumentParser(description="To Simple-SAM converter")
    argparser.add_argument(
        "mas",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()
    # print(args)
    for line in args.mas:
        chrom, read_name, read_str, pos = line.split('\t')

        print(read_name.strip(), chrom.strip(), str(int(pos)+1), cigar = f"{len(read_str.strip())}M", read_str.strip(), sep = '\t')
        # Output as Simple-SAM


if __name__ == '__main__':
    main()
