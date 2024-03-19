from resources.s3_resource import S3Resource
from defaults import catch_error


@catch_error
def print_objects(self: S3Resource, batch_size: int):
    """Downloads a batch of files from bucket."""

    objects = self.list_objects_paginated(
        batch_size
    )

    for obj in objects:
        print("Found object: ", obj)
