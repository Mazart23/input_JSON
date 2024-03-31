import json
from defaults import *
from error_classes.role_policy_error import JSONDecodeIAMRoleError


def validate_json(file, schema, root=None,
                  look_value=DEFAULT_LOOK_VALUE, contains=DEFAULT_CONTAINS, is_found=False) -> bool:

    if isinstance(file, list):
        for file_elem in file:
            if not validate_json(file_elem, schema, root, look_value, contains, is_found):
                return False

    elif isinstance(file, dict) and isinstance(schema, dict):

        if len(file) != len(schema):
            raise JSONDecodeIAMRoleError(f'invalid number of keys in {root = }: {len(file) = }, '
                                         f'while the proper is: {len(schema) = }')

        for file_key in file:

            # keys checking
            if file_key not in schema:
                raise JSONDecodeIAMRoleError(f'invalid key in {root = }: {file_key}')

            if not validate_json(file[file_key], schema[file_key],
                                 file_key, look_value, contains, file_key == look_value):
                return False

    elif isinstance(schema, type):

        if not isinstance(file, schema):
            raise JSONDecodeIAMRoleError(f'invalid type of element {file}: {type(file) = }, '
                                         f'while the proper is: {schema}')

        elif is_found:

            if file == contains:
                return False

    else:
        raise JSONDecodeIAMRoleError(f'invalid type of element {file}: {type(file) = }, '
                                     f'while the proper is: {type(schema) = }')

    return True


def inp_json(filepath: str, schema: dict, look_value: str, contains: str) -> None:
    try:
        with open(filepath, 'r') as f:
            file_json = json.load(f)

        isvalid = validate_json(file_json, schema, look_value=look_value, contains=contains)
        print(f'{isvalid = }')

    except FileNotFoundError as e:
        print(str(e))

    except JSONDecodeIAMRoleError as e:
        print(str(e))

    except json.JSONDecodeError as e:
        print('Invalid JSON Decode:', str(e))

    except Exception as e:
        print('Other exception:', str(e))
