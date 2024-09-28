import os
import hashlib

def calculate_md5(file_path):
    md5_hash = hashlib.md5()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096),b""):
            md5_hash.update(chunk)

    return md5_hash.hexdigest()


def verify_file(file_path, known_md5):
    calculated_md5 = calculate_md5(file_path)

    if calculated_md5 == known_md5:
        print(f"{file_path}: MD5 checksum is valid.")
    else:
        print(f"{file_path}: MD5 checksum does not match.")


file_path = "example.txt"
known_md5 = "5d41402abc4b2a76b9719d911017c592"

print(os.getcwd())
os.chdir("md5_practice")
print(os.getcwd())

verify_file(file_path, known_md5)
