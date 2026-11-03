```python
import boto3
import csv
import io
import os
import urllib.parse

s3 = boto3.client('s3')

ses = boto3.client(
    'ses',
    region_name='us-east-1'
)

SENDER = os.environ['SENDER_EMAIL']


def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key']
    )

    response = s3.get_object(Bucket=bucket, Key=key)

    csv_content = response['Body'].read().decode('utf-8-sig')
    reader = csv.DictReader(io.StringIO(csv_content))

    for row in reader:
        ses.send_email(
            Source=SENDER,
            Destination={
                'ToAddresses': [row['Email']]
            },
            Message={
                'Subject': {
                    'Data': 'Welcome'
                },
                'Body': {
                    'Text': {
                        'Data': (
                            f"Hello {row['Name']},\n\n"
                            "This is an automated email from AWS Lambda.\n\n"
                            "Regards,\nAWS Team"
                        )
                    }
                }
            }
        )

    return {
        'statusCode': 200,
        'body': 'Emails Sent Successfully'
    }
```

