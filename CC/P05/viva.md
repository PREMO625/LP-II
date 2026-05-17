# Oral Viva Guide - CC P05 (Mini Cloud Storage / HDFS Simulation)

## Quick One-Liners

- **SaaS**: Software delivered over network/cloud.
- **HDFS**: Hadoop Distributed File System, stores files in blocks.
- **Simulation**: Educational block storage on local system.
- **Encryption**: Simple reversible transform for demo.

---

## Basic Questions

1. What is SaaS?
   - Software accessed over the network instead of local installation.
2. What is HDFS?
   - Hadoop Distributed File System that stores files in blocks.
3. Why is this project called HDFS simulation?
   - It splits files into blocks and stores them separately.
4. What is the main goal of this practical?
   - Demonstrate file segmentation, storage, and reconstruction.
5. What is the input file in this project?
   - `sample.txt`.
6. What is the output file?
   - `downloaded_sample.txt`.
7. What does the cloud_storage folder represent?
   - Simulated cloud storage.
8. What is BLOCK_SIZE?
   - Size of each block in characters.
9. What is the encryption used here?
   - Reverse-string encryption.
10. Why use encryption?
    - To demonstrate secure storage concept.

---

## Code-Oriented Questions

11. Why create the cloud_storage folder automatically?
    - To ensure storage exists before uploading blocks.
12. Why use `os.path.exists`?
    - To check if the folder is already present.
13. Why use `range(0, len(data), BLOCK_SIZE)`?
    - To split the file into fixed-size blocks.
14. How are block names created?
    - Using `block_{index}.txt` naming.
15. Why use `sorted(os.listdir(...))` in download?
    - To reconstruct blocks in correct order.
16. Why read and write in text mode?
    - The input is text data in this project.
17. What happens if BLOCK_SIZE is changed?
    - The number and size of blocks change.
18. Why is decrypt the same as encrypt?
    - Reverse of reverse gives original data.
19. Why print block list after upload?
    - To show segmentation result.
20. Why reconstruct into a new file?
    - To verify upload and download integrity.

---

## Intermediate Questions

21. How is this similar to real HDFS?
    - It splits files into blocks and stores them separately.
22. How is this different from real HDFS?
    - It is local and does not replicate or distribute blocks across nodes.
23. What is the role of a controller in this project?
    - The Python script manages upload and download operations.
24. What is meant by cloud in this project?
    - The local folder simulates centralized storage.
25. Can this handle binary files?
    - Not as written; it reads text mode.
26. Why not use real Hadoop?
    - Too heavy for a lab mini project.
27. Can you add compression?
    - Yes, by compressing blocks before storage.
28. What if a block is missing?
    - Reconstruction will be incomplete or corrupted.
29. How to improve security?
    - Use real encryption algorithms like AES.
30. How to improve reliability?
    - Add block checksums and replication.

---

## External Examiner Questions

31. Is this a real cloud implementation?
    - No, it is a simplified simulation for educational purposes.
32. How does this demonstrate SaaS?
    - Users access storage via software instead of local manual file handling.
33. Why is block storage important?
    - Enables large file handling and parallel access in real systems.
34. Can this scale to multiple users?
    - Not in the current design; would need user isolation and access control.
35. What is the biggest limitation of this project?
    - It runs locally and lacks distributed storage features.

---

## Quick Memory Sheet

- SaaS = software over network
- HDFS = file blocks
- cloud_storage = simulated cloud
- upload = split + encrypt
- download = decrypt + join
