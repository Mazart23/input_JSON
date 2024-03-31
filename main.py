from argparse import ArgumentParser
import os
from schema import SCHEMA
from parser import setup_subparsers
from validation import *


def run(args):
    inp_json(
        filepath=args.filepath.strip(),
        schema=SCHEMA,
        look_value=args.field.strip(),
        contains=args.contains.strip()
    )


def run_test(args):
    directory = args.dirpath.strip()

    for test in os.listdir(directory):
        filepath = os.path.join(directory, test)

        print('\n', str(test), '- Expected: ', end='')

        if str(test).startswith('asterisk'):
            print(False)
        elif str(test).startswith('valid'):
            print(True)
        elif str(test).startswith('invalid'):
            print('Exception raised')
        else:
            print('Indeterminate test')

        inp_json(
            filepath=str(filepath),
            schema=SCHEMA,
            look_value=DEFAULT_LOOK_VALUE,
            contains=DEFAULT_CONTAINS
        )


def main() -> None:
    parser_obj = ArgumentParser(description="AWS::IAM::Role Policy JSON Validator")
    setup_subparsers(parser_obj, func_run=run, func_test=run_test)
    arguments = parser_obj.parse_args()
    arguments.callback(arguments)


if __name__ == '__main__':
    main()
