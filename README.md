## Detecting Sensitive Data In Dynamodb with Macie - Blog

Repo contains all source code and Cloudformation templates for Macie DynamoDB blog located here https://aws.amazon.com/blogs/security/detecting-sensitive-data-in-dynamodb-with-macie/

<hr/>

### CloudFormation

The cft.yaml in the /src folder is the Cloudformation template used to deploy the blog

<hr/>

### Python Lambda Code

**Location:** in /src folder

**src/Import-Data-To-DynamoDB.py**
<br>
Python file that handles the import of test CSV datasets to DynamoDB

**src/Export-DynamoDB-Data-To-S3.py**
<br>
Python file that handles the export of DynamoDB table data into S3

<hr/>

### Test Datasets

**Location:** in /datasets folder

**accounts.csv** <br>Test dataset that will be loaded into the DynamoDB table by the Import-Data-To-DynamoDB lambda function

**people.csv** <br> Test dataset that will be loaded into the DynamoDB table by the Import-Data-To-DynamoDB lambda function

<hr/>

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
