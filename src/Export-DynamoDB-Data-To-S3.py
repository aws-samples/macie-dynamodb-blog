import boto3, json, os, datetime

def lambda_handler(event, context):
    # retrieves environment variable that contains the dynamoDB tables data that will be exported
    tables = os.environ['dynamo_db_tables'].split(',')
    table_count = len(tables)

    # current date and time will be added as part of the file name that is exported
    current_time = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

    # loops through dynamodb tables
    for table in tables:
        print(f'Exporting sample data for {table} table')

        dynamodb = boto3.resource('dynamodb')

        current_table = dynamodb.Table(table)

        # scans current dynamodb table to get sample data
        response = current_table.scan()['Items']

        s3 = boto3.client('s3')

        ''' creates new S3 object with dynamoDB sample data
            filename format is dynamodb-<tablename>-<region>-<current_datetime>.json
        '''
        s3.put_object(
            Bucket=str(os.environ['bucket_to_export_to']),
            Key=f"dynamodb-{table}-{os.environ['AWS_REGION']}-{current_time}.json",
            Body=str(response)
        )

    return 'DynamoDB data has been exported to S3'
