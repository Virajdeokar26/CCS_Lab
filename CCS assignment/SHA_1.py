import hashlib

input_string = "Hello World!"
sha1_hash = hashlib.sha1(input_string.encode())  
hash_result = sha1_hash.hexdigest()         

print(f"SHA-1 hash of '{input_string}' is: {hash_result}")
