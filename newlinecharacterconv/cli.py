"""Console script for newlinecharacterconv."""
import argparse
import sys
from .newlinecharacterconv import crlf_to_lf

def main():
    """Console script for newlinecharacterconv."""
    parser = argparse.ArgumentParser(description='换行符转换',prog='换行符转换')
        #可传入多个文件，生成一个文件名列表
    parser.add_argument('file',nargs='+',help='源文件')
    args = parser.parse_args()
    crlf_to_lf(args.file)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover