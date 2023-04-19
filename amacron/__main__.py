from argparse import ArgumentParser
from .amacron import AmacronConverter
from .language_support import LanguageSupport


def get_argument_parser():
    parser = ArgumentParser(description="Returns a cron expression from a input of english formatted cron.",
                            prog='amacron')
    parser.add_argument("--version",
                        action="version",
                        version="%(prog)s 0.2.4")
    parser.add_argument("-i",
                        "--input_cron",
                        help="convert amacron to cron expression and exit")
    parser.add_argument("-l",
                        "--language",
                        action=LanguageSupport,
                        nargs=0,
                        help="show language support and exit",
                        default=False)
    return parser


def process_arguments(parser):
    args = parser.parse_args()
    # first level validation before processing
    return args


def main():
    parser = get_argument_parser()
    input_arg = process_arguments(parser)
    if input_arg.input_cron:
        return AmacronConverter.convert(input_arg.input_cron)
    elif not input_arg.language:
        parser.print_usage()
        print("Try 'amacron --help' for more information.")


if __name__ == '__main__':
    main()
