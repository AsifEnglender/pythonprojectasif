import boto3
import uuid
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
#second_object = s3_resource.Object('asiftestbucket19345839459', '456.txt')
#third_object = s3_resource.Object('asiftestbucket19345839459', '123.txt')
first_bucket = s3_resource.Bucket(name='asiftestbucket19345839459')




#def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
#    return ''.join([bucket_prefix, str(uuid.uuid4())])

#s3_resource.create_bucket(Bucket='asifsecondtestbucket19345839459',
#                           CreateBucketConfiguration={
#                               'LocationConstraint': 'eu-west-2'})


# s3_resource.meta.client.upload_file(
#     Filename='123.txt', Bucket='asiftestbucket19345839459',
#     Key='123.txt')

#s3_resource.Object(asiftestbucket19345839459, '123.txt').download_file(
#    'C:\\Users\\Hagai\\AppData\\Local\\Temp\\123.txt')


#def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
#    copy_source = {
#        'Bucket': bucket_from_name,
#        'Key': file_name
#    }
#    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)
#
#copy_to_bucket('asiftestbucket19345839459', 'asifsecondtestbucket19345839459', '123.txt')



#s3_resource.Object('asifsecondtestbucket19345839459', '123.txt').delete()


#second_object.upload_file('456.txt', ExtraArgs={
#                          'ACL': 'public-read'})

#second_object_acl = second_object.Acl()

#print(second_object_acl.grants)


#third_object.upload_file('3rdfile.txt', ExtraArgs={
#                         'ServerSideEncryption': 'AES256'})


#print(third_object.server_side_encryption)


#third_object.upload_file('3rdfile.txt', ExtraArgs={
#                         'ServerSideEncryption': 'AES256',
#                         'StorageClass': 'STANDARD_IA'})

#third_object.reload()
#print(third_object.storage_class)


# def enable_bucket_versioning(bucket_name):
#     bkt_versioning = s3_resource.BucketVersioning(bucket_name)
#     bkt_versioning.enable()
#     print(bkt_versioning.status)
#
# enable_bucket_versioning('asiftestbucket19345839459')


#third_object.upload_file('123.txt')


#for bucket in s3_resource.buckets.all():
#    print(bucket.name)


#for obj in first_bucket.objects.all():
#    print(obj.key)


# for obj in first_bucket.objects.all():
#     subsrc = obj.Object()
#     print(obj.key, obj.storage_class, obj.last_modified,
#          subsrc.version_id, subsrc.metadata)






# def delete_all_objects(bucket_name):
#     res = []
#     bucket=s3_resource.Bucket(bucket_name)
#     for obj_version in bucket.object_versions.all():
#         res.append({'Key': obj_version.object_key,
#                     'VersionId': obj_version.id})
#     print(res)
#     bucket.delete_objects(Delete={'Objects': res})
#
# delete_all_objects('asiftestbucket19345839459')




#s3_resource.Bucket('asiftestbucket19345839459').delete()

#s3_resource.meta.client.delete_bucket(Bucket='asifsecondtestbucket19345839459')








