from resources.s3_resource import S3Resource
from defaults import catch_error


@catch_error
def batch_download_objects(
        s3Client: S3Resource,
        batch_size: int,
        output_dir: str
):
    """Downloads a batch of files from bucket."""

    totalCount = s3Client.get_object_count()
    cursor = None

    for count in totalCount/batch_size:
        objects = s3Client.list_objects_paginated(
            page_size=batch_size,
            start_after=cursor
        )

        if cursor is None:
            cursor = objects[-1]

        for obj in objects:
            s3Client.save_file_batched(objects, output_dir)
