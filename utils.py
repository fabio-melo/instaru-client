import hashlib
import logging as log


def check_sha256(filename):

  sha256_hash = hashlib.sha256()
  with open(filename,"rb") as f:
      # Read and update hash string value in blocks of 4K
      for byte_block in iter(lambda: f.read(4096),b""):
          sha256_hash.update(byte_block)
      log.info(f"SHA256 HASH: {sha256_hash.hexdigest()}")
      return sha256_hash.hexdigest()

