import os

# Directory containing the .bin files
directory_path = os.getcwd()

# List of byte values in hexadecimal format
bytes_list = [0x73, 0x63, 0x72, 0x65, 0x65, 0x6e, 0x43, 0x6f, 0x6e, 0x66, 0x69, 0x67, 0x0B]  # Replace this with your list of byte values

# Convert hexadecimal byte values to bytes
data_to_append = bytes(bytes_list)
# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".bin"):
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'ab') as file:  # 'ab' opens the file in append binary mode
            file.write(data_to_append)
            print(f"Appended data to {filename}")