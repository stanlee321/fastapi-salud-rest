from minio import Minio
from minio.error import S3Error


def create_bucket(client: Minio, bucket_name:str):

    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
    else:
        print(f"Bucket '{bucket_name}' already exists")

def put_object(client: Minio, src_file:str, dst_filename:str, bucket_name:str):

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
    client.fput_object(
        bucket_name, dst_filename, src_file,
    )
    print(
        f"'{src_file}' is successfully uploaded as "
        f"object '{dst_filename}' to bucket '{bucket_name}'. 😃"
    )

def get_minio_client(host:str, key:str, secret:str, secure:bool = False):

    client = Minio(
        host,
        access_key=key,
        secret_key=secret,
        secure=secure
    )

    return client

def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.

    client = get_minio_client(host = "localhost:9000",
        key = "minio-access-key",
        secret="minio-secret-key"
    )

    create_bucket(client = client , bucket_name = "sicoes")

    put_object(client = client,
                src_file = "../data/TABLE_3.csv",
                dst_filename = "topicX/TABLA_3_test.csv" ,
                bucket_name = "sicoes" )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)