## Macie DynamoDB Blog

The purpose of this repo is to store all content related to the Macie DynamoDB blog found here <Blog URL will go here>

### CloudFormation

The cft.yaml in the /src folder is the Cloudformation template used to deploy the blog

### Python Lambda Code

**src/Import-Data-To-DynamoDB.py**
Python file that handles the import of test CSV datasets to DynamoDB

**src/Export-DynamoDB-Data-To-S3.py**
Python file that handles the export of DynamoDB table data into S3

### Test Datasets

Location: /datasets

accounts.csv - Test dataset that will be loaded into the DynamoDB table by the Import-Data-To-DynamoDB lambda function
people.csv - Test dataset that will be loaded into the DynamoDB table by the Import-Data-To-DynamoDB lambda function

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
