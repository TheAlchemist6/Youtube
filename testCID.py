from multiformats import CID
from multiformats import multibase
from multiformats import multihash

data = "I Like Pie."
data_bytes = data.encode("utf-8")

encoded = multibase.encode(data_bytes, "base32")
digest = multihash.digest(data_bytes, "sha2-256")
cidv1 = CID("base32", 1, "raw", digest)
print(cidv1)