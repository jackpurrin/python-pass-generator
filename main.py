import time
import base64

shred1 = str(hash(time.time()))
shred1bytes = shred1.encode("ascii")
shred2 = base64.b64encode(shred1bytes)
print(shred1)
print(shred2)

