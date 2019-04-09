import os,sys
import boto3
from collections import defaultdict
import csv

returnDict = {}
returnDict = defaultdict(list)

s3 = boto3.resource('s3')

#<<<SET FIRST BUCKET HERE>>>
bucket = 'bucket1'
mybucket = s3.Bucket(bucket)

for obj in mybucket.objects.all():
	objectValue = bucket + obj.key
	key = obj.key.split('/')[-1]
	returnDict[key].append(objectValue)
	print(objectValue)


#<<<SET SECOND BUCKET HERE>>>
bucket = 'bucket2'
mybucket = s3.Bucket(bucket)

for obj in mybucket.objects.filter(Prefix='qux/'): # <<<Example of setting a prefix filter for bucket2>>>
  objectValue = bucket + obj.key
	key = obj.key.split('/')[-1]
	returnDict[key].append(objectValue)
	print(objectValue)
  
  
with open("DUPLICATE_RESULTS.csv", "a") as fp:
	wr = csv.writer(fp)
	for key, value in returnDict.items():
		if len(value) == 1:
			pass
		else:
			if key == '':
				pass
			else:
				print([key] + value)
				temp_list = [key] + value
				wr.writerow(temp_list)
