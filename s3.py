import boto3

session = boto3.Session()
s3 = session.resource('s3')

print("Listing S3 Buckets:")
for bucket in s3.buckets.all():
    print(bucket.name)

bucket_name = 'prithesh-bucket-17'
s3.create_bucket(Bucket=bucket_name)
print(f"Bucket {bucket_name} created.")

s3.Bucket(bucket_name).upload_file('./ss1.png', 'image1.png')
print("File uploaded.")

s3.Bucket(bucket_name).download_file('image1.png', 'newimage.png')
print("File downloaded.")

s3.Object(bucket_name, 'image1.png').delete()
print("File deleted.")

s3.Bucket(bucket_name).delete()
print(f"Bucket {bucket_name} deleted.")
