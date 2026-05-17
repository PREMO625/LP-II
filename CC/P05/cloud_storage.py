import os

# Create cloud folder automatically
CLOUD_FOLDER = "cloud_storage"

if not os.path.exists(CLOUD_FOLDER):
    os.makedirs(CLOUD_FOLDER)

BLOCK_SIZE = 10   # characters per block


# Simple encryption function
def encrypt(data):
    return data[::-1]


# Simple decryption function
def decrypt(data):
    return data[::-1]


# Upload file to cloud
def upload_file(filename):

    with open(filename, "r") as file:
        data = file.read()

    blocks = []

    # Divide file into blocks
    for i in range(0, len(data), BLOCK_SIZE):
        block = data[i:i + BLOCK_SIZE]
        encrypted_block = encrypt(block)

        block_name = f"block_{i//BLOCK_SIZE}.txt"

        with open(os.path.join(CLOUD_FOLDER, block_name), "w") as bf:
            bf.write(encrypted_block)

        blocks.append(block_name)

    print("\nFile uploaded successfully!")
    print("Blocks created:", blocks)


# Download and reconstruct file
def download_file(output_filename):

    files = sorted(os.listdir(CLOUD_FOLDER))

    final_data = ""

    for file in files:

        with open(os.path.join(CLOUD_FOLDER, file), "r") as bf:
            encrypted_data = bf.read()

        decrypted_data = decrypt(encrypted_data)

        final_data += decrypted_data

    with open(output_filename, "w") as output:
        output.write(final_data)

    print("\nFile downloaded successfully!")
    print("Reconstructed file:", output_filename)


# Main program
print("===== MINI CLOUD STORAGE =====")

# Create sample file
with open("sample.txt", "w") as f:
    f.write("This is LP2 cloud computing mini project.")

# Upload
upload_file("sample.txt")

# Download
download_file("downloaded_sample.txt")