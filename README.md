# input_JSON
App verifying the input JSON data.

## Description

The goal of the app is to validate the format of JSON file. Default format is AWS::IAM::Role Policy.

[AWS::IAM::Role Policy description and example](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html)

You can specify:
* File to validate
* JSON Schema as Python dictionary
* JSON field to check whether its contains forbidden value
* Value that is forbidden in specified field

Establishments:
* If file has incompatible format with schema, the program display information about handled exception
* If file has compatible format with schema and specified JSON field contains forbidden value, the program return logical False
* If file has compatible format with schema and specified JSON field do not contains forbidden value, the program return logical True

## Getting Started

### Dependencies

* Python 2.12.2 with built-in libraries

### Installing

Download whole project and place it in new directory anywhere on the disk. 

### Executing program

Program can be executed via command line:

* Enter the command line (e.g. cmd or PowerShell on Windows)
* Enter the directory with project files (e.g. using 'cd' command)

There are 2 modes to run program:
1. Run - check whether the file has valid format based on JSON schema and field to search the specified forbidden value
2. Test - run prepared tests in sequence

For every mode, validation is performed due to comparison with JSON schema in schema.py. 
This file contains the python dictionary in which there are string values to check keys names and types to check proper type of values. If you want to make validation according to another JSON schema, then make changes in schema.py file without changing its location.
Changing schema.json has influence not only on running specific file, but also testing.
Program allows to check multiple field and multiple values that are stored in lists, despite lack of containing lists in schema.py. 
Then, in case of apperance a list in validating JSON file, every element from a list is checking according to the same root element of list and corresponding root in schema.

Choice of mode is possible by parsers. Here is explanation how to use parsers for every mode:


__1. Run__

The base command is:
```
python main.py run
```
Then the program would be executed with default values for every argument. 
These arguments are:
* '--filepath' or '-f' -> path to the JSON file to validate 
* '--field' -> field for validation the forbidden value
* '--contains' -> value to check whether field contains it

Default values for arguments above are set to ensure validation according to AWS::IAM::Role Policy and check whether Resource field do not contain single asterisk.

There is example of usage (with specified default values):
```
python main.py run -f 'examples/example.json' --field 'Resource' --contains '*'
```
For more specific information about usage and arguments, execute in command line:
```
python main.py run -h
```


__2. Test__

The base command is:
```
python main.py test
```
Then the program would be executed with default value of argument:
* '--dirpath' or '-d' -> path to the directory containing test files to run

For this case, every file from passed path to directory is validated in sequence according to AWS::IAM::Role Policy and check whether Resource field do not contain single asterisk. 
Every file in directory have proper name, which is informed the program about expected value to display by inp_json function (either contains asterisk or valid or invalid).

There is example of usage (with specified default value of dirpath):
```
python main.py test -d 'examples/test'
```
For more specific information about usage and arguments, execute in command line:
```
python main.py test -h
```


## Version History

* 0.1
    * Initial Release
    * tests based on printing
