SCHEMA = {
    "PolicyName": str,
    "PolicyDocument": {
        "Version": str,
        "Statement":
            {
                "Sid": str,
                "Effect": str,
                "Action": str,
                "Resource": str
            }
    }
}
