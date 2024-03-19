from dotenv import load_dotenv
from resources.s3_resource import S3Resource
from modules.example.batch_download_object import batch_download_objects


def main():
    load_dotenv()
    s3 = S3Resource()

    batch_download_objects(
        s3Client=s3,
        batch_size=20,
        output_dir="example"
    )


if __name__ == "__main__":
    main()
