from dotenv import load_dotenv
from resources.s3_resource import S3Resource


def main():
    load_dotenv()
    s3 = S3Resource()

    print(s3.list_objects_paginated(page_size=10))


if __name__ == "__main__":
    main()
