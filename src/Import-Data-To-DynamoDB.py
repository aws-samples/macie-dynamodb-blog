import json, boto3, os, csv, codecs, sys

s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')

# location where import files exist
s3_bucket_name = os.environ['s3_import_bucket_name'] 

def lambda_handler(event, context):
    # Object array that stores key/value pair of csv file and 
    # the dynamoDB table where csv data will be imported.
    # Converts string value to json object
    data_import_export_location = json.loads(os.environ['data_import_export_location'])

    #loops through array of objects
    for data in data_import_export_location:
        # loads dynamodb table and csv file name
        dynamoDB_table_name = data['table_name']
        csv_data_filename = data['csv_name'] 
        
        # # sets batch writing size
        batch_size = 100
        batch_data = []
        
        try:
            # gets s3 csv content
            obj = s3.Object(s3_bucket_name, csv_data_filename).get()['Body']
        except:
            print("Problem acessing S3 object")
    
        try:
            # reference to dynamodb table
            table = dynamodb.Table(dynamoDB_table_name)
        except:
            print("Problem accessing DynamoDB table.")
    
        # Loops through CSV data and batch writes 100 items at a time
        for row in csv.DictReader(codecs.getreader('utf-8')(obj)):
            if len(batch_data) >= batch_size:
                write_data_to_dynamo(batch_data, dynamoDB_table_name)
                batch_data.clear()
    
            batch_data.append(row)
        
        if batch_data:
            write_data_to_dynamo(batch_data, dynamoDB_table_name)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data imported into DynamoDB Table')
    }
                                
# function that writes data to DynamoDB table       
def write_data_to_dynamo(rows, table_name):
    try:
        dynamodb_table = dynamodb.Table(table_name)
    except:
        print("Problem accessing DynamoDB table.")

    try:
        with dynamodb_table.batch_writer() as batch:
            for i in range(len(rows)):
                batch.put_item(
                    Item=rows[i]
                )
    except:
        print("There was a problem loading data into DynamoDB table")
