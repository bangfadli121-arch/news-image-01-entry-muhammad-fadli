import hashlib
import os
import shutil
import struct
import sys

HASH_CHUNK_SIZE = 65536
MAX_ARTWORK_BYTES = 1048576


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as image_file:
        for chunk in iter(lambda: image_file.read(HASH_CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message):
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_image(path):
    try:
        with open(path, "rb") as image_file:
            header = image_file.read(24)
    except OSError as error:
        fail(f"cannot inspect copied image {path}: {error}")

    png_signature = b"\x89PNG\r\n\x1a\n"
    if header.startswith(png_signature):
        if len(header) < 24 or header[12:16] != b"IHDR":
            fail(f"PNG header is incomplete or missing IHDR: {path}")
        width, height = struct.unpack(">II", header[16:24])
        if width > 1024 or height > 1024:
            fail(f"PNG dimensions are larger than 1024 pixels: {width}x{height}")
        return

    if header.startswith(b"\xff\xd8\xff"):
        return

    fail(f"copied image is neither PNG nor JPEG: {path}")


def main():
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    destination = os.path.join(output_dir, "entry.png")

    if not os.path.isfile(source):
        fail(f"source file is missing: {source}")

    try:
        source_size = os.path.getsize(source)
    except OSError as error:
        fail(f"could not inspect source file {source}: {error}")

    if source_size > MAX_ARTWORK_BYTES:
        fail(f"artwork exceeds the 1 MiB size limit: {source_size} bytes")

    try:
        os.makedirs(output_dir, exist_ok=True)
        shutil.copyfile(source, destination)
    except OSError as error:
        fail(f"could not copy artwork to {destination}: {error}")

    validate_image(destination)

    try:
        output_size = os.path.getsize(destination)
        source_hash = sha256(source)
        output_hash = sha256(destination)
    except OSError as error:
        fail(f"could not verify artwork copy: {error}")

    if source_size != output_size or source_hash != output_hash:
        fail(f"copied artwork does not match source: {destination}")

    print(f"Wrote {destination} ({output_size} bytes, sha256 {output_hash})")


if __name__ == "__main__":
    main()
