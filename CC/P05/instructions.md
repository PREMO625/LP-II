## HDFS Simulation Using Python

### Project Name (Use in Viva)

- Mini Cloud Storage System using HDFS Simulation
- Simple SaaS File Storage using Python

---

## What This Project Does

The program:

- Takes a file as input.
- Divides it into fixed-size blocks.
- Encrypts each block.
- Stores blocks in a cloud folder.
- Downloads and reconstructs the original file.

This satisfies the assignment requirement for HDFS-style storage and SaaS over LAN.

---

## Why This Counts as HDFS (Educational Simulation)

**Real HDFS** splits large files into blocks and stores them separately.

**This simulation** does the same on a local machine to demonstrate the concept without installing Hadoop.

---

## Core Code (cloud_storage.py)

```python
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
```

---

## How the Program Works (Step-by-Step)

1. Creates `cloud_storage/` folder.
2. Reads `sample.txt`.
3. Splits the file into blocks of size `BLOCK_SIZE`.
4. Encrypts each block using reverse-string logic.
5. Stores each encrypted block inside `cloud_storage/`.
6. Reads blocks back in order, decrypts, and reconstructs the file.

---

## Input and Output Explanation

### Input

- `sample.txt` contains:

```text
This is LP2 cloud computing mini project.
```

### Output

- Encrypted block files are created in `cloud_storage/`.
- Reconstructed file `downloaded_sample.txt` matches the original input.

Console output example:

```text
===== MINI CLOUD STORAGE =====

File uploaded successfully!
Blocks created: ['block_0.txt', 'block_1.txt', 'block_2.txt']

File downloaded successfully!
Reconstructed file: downloaded_sample.txt
```

---

## File Roles (Why Each File Exists)

- `cloud_storage.py`: Controller script that performs upload, encryption, storage, and download.
- `sample.txt`: Input file for testing block splitting and encryption.
- `downloaded_sample.txt`: Output file after reconstruction.
- `cloud_storage/`: Folder that simulates cloud storage containing encrypted blocks.

---

## How to Run

1. Open terminal in the project folder.
2. Run:

```bash
python cloud_storage.py
```

---

## What to Show to the Examiner

- Code in `cloud_storage.py`.
- `cloud_storage/` folder with block files.
- `sample.txt` and `downloaded_sample.txt`.
- Terminal output showing upload and download.

---

## Important Note for Viva

Say: **"This is a simplified HDFS simulation for educational purposes."**

Do not claim it is a full Hadoop implementation.

WITHOUT making your life miserable.