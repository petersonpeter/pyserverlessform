import boto3
from botocore.exceptions import ClientError


def ses_send_email(SENDER, RECIPIENT, SUBJECT, BODY_TEXT, AWS_REGION, CHARSET):
    client = boto3.client('ses',region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [RECIPIENT],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )

    except ClientError as e:
        return e.response['Error']['Message']
    else:
        return response['ResponseMetadata']['RequestId']
