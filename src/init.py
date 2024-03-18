from dotenv import load_dotenv
from resources.s3_resource import S3Resource


def main():
    load_dotenv()
    s3 = S3Resource()

    print(s3.list_objects_paginated(page_size=10))

    # s3.download_file("20150310133000-305")
    # buffer = s3.load_file()


if __name__ == "__main__":
    main()
