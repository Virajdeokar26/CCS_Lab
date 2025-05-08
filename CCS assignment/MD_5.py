import hashlib

input_string = "Hello World!"
md5_hash = hashlib.md5(input_string.encode())  
hash_result = md5_hash.hexdigest()         

print(f"MD5 hash of '{input_string}' is: {hash_result}")
