from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class PublicMediaStorage(S3Boto3Storage):
    base_url = settings.AWS_S3_ENDPOINT_URL
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    file_overwrite = False

    def get_full_url(self):
        return f'{self.base_url}/{self.bucket_name}/{self.location}'