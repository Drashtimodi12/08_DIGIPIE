"""
b-string (Bytes String) = Prefix: b"..." or B"..."
A b-string is a bytes string — it represents binary data, not normal text.

Used in:- Networking, File I/O (binary files), Encoding operations

Important Rules of b-strings
Allowed characters: ASCII letters (a-z, A-Z), Numbers (0–9), Basic symbols
NOT Allowed: Non-ASCII characters (like Gujarati, Hindi, emojis)
"""

data = b"Drashti"
print(data, type(data))     # Output: b'Drashti' <class 'bytes'>

# Converting normal string → bytes.   Use .encode()
text = "Modi"
byte_data = text.encode()
print(byte_data)            # Output: b'Modi'



# Converting bytes → string
text = b"Drashti"
byte_data = text.decode()   # ✔ Convert bytes → string
print(byte_data)            # Output: Drashti