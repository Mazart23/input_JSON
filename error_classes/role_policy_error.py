class JSONDecodeIAMRoleError(Exception):
    def __init__(self, msg):
        msg = 'Invalid JSON AWS::IAM::Role Policy format: ' + msg
        super().__init__(msg)
