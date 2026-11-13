import hashlib
import os
import shutil
import struct
import sys


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as image_file:
        for chunk in iter(lambda: image_file.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message):
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(1)


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

    if source_size > 1048576:
        fail(f"artwork exceeds the 1 MiB size limit: {source_size} bytes")

    try:
        os.makedirs(output_dir, exist_ok=True)
        shutil.copyfile(source, destination)
    except OSError as error:
        fail(f"could not copy artwork to {destination}: {error}")

    try:
        with open(destination, "rb") as output_file:
            image_header = output_file.read(24)
    except OSError as error:
        fail(f"could not read copied artwork {destination}: {error}")

    is_png = image_header[:8] == b"\x89PNG\r\n\x1a\n"
    is_jpeg = image_header.startswith(b"\xff\xd8\xff")
    if not (is_png or is_jpeg):
        fail(f"copied file has an unsupported image format: {destination}")

    if is_png:
        if len(image_header) < 24 or image_header[12:16] != b"IHDR":
            fail(f"copied PNG has an invalid IHDR chunk: {destination}")
        width, height = struct.unpack(">II", image_header[16:24])
        if width > 1024 or height > 1024:
            fail(f"PNG dimensions exceed 1024 pixels: {width}x{height}")

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
