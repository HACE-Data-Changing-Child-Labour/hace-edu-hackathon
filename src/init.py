from dotenv import load_dotenv
from resources.s3_resource import S3Resource
from modules.example.batch_download_object import print_objects


def main():
    load_dotenv()
    s3 = S3Resource()

    print_objects(
        self=s3,
        batch_size=20,
    )


if __name__ == "__main__":
    main()
