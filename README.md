# S3-Duplicate-File-Identifier
## Requires Python3 and boto3 SDK.

Must configure AWS credentials before running in CLI or embed them within the boto3 statement.

Simple functional python script demonstrating how to identify duplicate files across buckets and prefixes.  Outputs CSV file where the first of each row is the unique object name and the subsequent rows are the duplicate object addresses.



Example code demonstrates looking for duplicate files in all of bucket1 and only in the given prefix for bucket2.  Code can be modified to work accorss as many buckets/prefixes as necessary.  


###### Example duplicate files accross 2 buckets:
```
s3://bucket1/foo/bar/FILE.txt
s3://bucket2/baz/qux/FILE.txt
```
###### Row output in CSV:
```
FILE.txt, s3://bucket1/foo/bar/FILE.txt, s3://bucket2/baz/qux/FILE.txt
```
