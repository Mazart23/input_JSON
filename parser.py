from argparse import ArgumentParser
from defaults import *


def setup_subparsers(parser: ArgumentParser, func_run, func_test) -> None:
    """
    Initial subparsers with arguments
    """
    subparser = parser.add_subparsers(dest="command")
    run_parser = subparser.add_parser(
        "run",
        help="The parser used to run algorithm for specific case",
    )
    run_parser.add_argument(
        "-f",
        "--filepath",
        type=str,
        default=DEFAULT_FILEPATH,
        help=f"Specify the path to the JSON file to validate, default: {DEFAULT_FILEPATH}",
    )
    run_parser.add_argument(
        "--field",
        type=str,
        default=DEFAULT_LOOK_VALUE,
        help=f"Specify the field for validation, default: {DEFAULT_LOOK_VALUE}",
    )
    run_parser.add_argument(
        "--contains",
        type=str,
        default=DEFAULT_CONTAINS,
        help=f"Specify the value to validate whether the field does not contain it, default: {DEFAULT_CONTAINS}",
    )
    run_parser.set_defaults(callback=func_run)

    test_parser = subparser.add_parser(
        "test", help="The parser used to run tests"
    )
    test_parser.add_argument(
        "-d",
        "--dirpath",
        default=DEFAULT_PATH_OF_TEST_DIR,
        type=str,
        help="Specify the path to directory containing the tests to run"
    )
    test_parser.set_defaults(callback=func_test)
