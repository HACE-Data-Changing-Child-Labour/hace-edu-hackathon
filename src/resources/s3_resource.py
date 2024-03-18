import boto3
import os
from typing import List
from defaults import catch_error
from defaults import data_path
from io import BytesIO


class S3Resource:
    """Default class to interact with AWS S3"""
    s3 = None
    bucket_name = None

    @catch_error
    def __init__(self):
        """Initializes the S3 resource."""

        session = boto3.Session(
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
            region_name="eu-west-2",
        )
        self.s3 = session.resource('s3')
        self.bucket_name = os.environ.get("S3_BUCKET_NAME")

    @catch_error
    def list_objects(self) -> List[str]:
        """Lists all objects in the S3 bucket."""

        object_keys = list()

        bucket = self.s3.Bucket(self.bucket_name)
        for obj in bucket.objects.all():
            object_keys.append(obj.key)

        return object_keys

    @catch_error
    def load_file(
            self,
            object_name: str
    ) -> BytesIO:
        """Loads a file from S3 into a bytes buffer."""

        response = self.s3.meta.client.get_object(
            Bucket=self.bucket_name,
            Key=object_name
        )

        return BytesIO(response['Body'].read())

    @catch_error
    def save_file(
            self,
            object_name: str,
    ) -> str:
        """Downloads a file from the S3 bucket."""

        self.s3.meta.client.download_file(
            self.bucket_name,
            object_name,
            os.path.join(data_path, f"{object_name}.txt")
        )

        return object_name

    @catch_error
    def save_file_batched(
            self,
            object_names: List[str],
            output_dir: str
    ) -> List[str]:
        """Downloads a batch of files from the S3 bucket."""

        output_files = list()
        newpath = f"{data_path}/{output_dir}"
        os.makedirs(newpath, exist_ok=True)

        for i in range(len(object_names)):
            self.s3.meta.client.download_file(
                self.bucket_name,
                object_names[i],
                os.path.join(newpath, f"{object_names[i]}.txt")
            )

            output_files.append(output_dir + "/" + object_names[i])

        return output_files

    @ catch_error
    def list_objects_paginated(
            self,
            page_size: int = 20,
            start_after: str = None
    ) -> List[str]:
        """Lists all objects in the S3 bucket with pagination,
        starting after a specified key, but limits the results to page_size."""

        paginator = self.s3.meta.client.get_paginator('list_objects_v2')
        pagination_args = {
            'Bucket': self.bucket_name,
        }
        if start_after is not None:
            pagination_args['StartAfter'] = str(start_after)

        all_keys = list()

        pages = paginator.paginate(**pagination_args)
        for page in pages:
            contents = page.get('Contents', [])
            for obj in contents:
                print(obj['Key'])
                all_keys.append(obj['Key'])
                if len(all_keys) >= page_size:
                    return all_keys

        return all_keys
