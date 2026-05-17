## Case Study: Amazon EC2 (Elastic Compute Cloud)

### Title

Case Study on Amazon EC2 and its Web Services

### Aim

To study Amazon EC2, its core services, and how it is used to deploy and scale applications in the cloud.

### Objectives

- Understand what Amazon EC2 is and why it is used.
- Learn the main components of EC2 (instances, AMI, EBS, security groups, key pairs).
- Study scaling, load balancing, and monitoring in EC2.
- Identify real-world use cases and best practices.
- Prepare viva questions for oral practical.

### Introduction

Amazon EC2 (Elastic Compute Cloud) is a core service of AWS that provides resizable virtual servers in the cloud. Users can launch servers (instances) in minutes, choose operating systems, configure storage, and scale up or down based on demand.

EC2 is pay-as-you-go, which means you pay only for the compute you use.

### Why EC2 Is Important

- Eliminates the need to buy physical servers.
- Provides flexibility in CPU, memory, and storage.
- Supports rapid scaling for traffic spikes.
- Integrates with other AWS services.

---

## EC2 Core Concepts (Easy to Remember)

### 1. EC2 Instance

A virtual server running in the AWS cloud.

### 2. AMI (Amazon Machine Image)

A template that includes OS, software, and configuration. You launch instances using an AMI.

### 3. EBS (Elastic Block Store)

Persistent storage attached to EC2. Data remains even if the instance stops.

### 4. Security Group

A virtual firewall that controls inbound and outbound traffic rules.

### 5. Key Pair

Public/private keys used for secure SSH access to the instance.

### 6. Instance Types

Different CPU/RAM combinations for different workloads:

- General purpose (t2, t3)
- Compute optimized (c5)
- Memory optimized (r5)
- Storage optimized (i3)

---

## EC2 Web Services Around It

### Elastic Load Balancer (ELB)

Distributes incoming traffic across multiple EC2 instances.

### Auto Scaling

Automatically adds or removes instances based on load.

### CloudWatch

Monitors metrics (CPU, memory, network) and triggers alarms.

### VPC (Virtual Private Cloud)

Creates a private network for EC2 resources.

### IAM (Identity and Access Management)

Controls who can access EC2 resources and what they can do.

---

## Case Scenario (External-Practical Worthy)

### Problem

A startup launches an e-commerce website. During sales, traffic spikes and the server crashes. They need a scalable, reliable hosting solution.

### EC2-Based Solution

1. **Launch EC2 instances** using an Amazon Linux AMI.
2. **Attach EBS volumes** for persistent product and order data.
3. **Create a security group** allowing HTTP/HTTPS and SSH access.
4. **Use an Elastic Load Balancer** to distribute traffic.
5. **Enable Auto Scaling** to add instances when CPU exceeds 70%.
6. **Monitor with CloudWatch** for performance and alerts.

### Outcome

- Website stays online during traffic spikes.
- Costs remain controlled due to pay-as-you-go.
- Performance improves and downtime is reduced.

---

## Step-by-Step EC2 Workflow (Exam Friendly)

```text
Create AWS account
-> Choose AMI
-> Choose instance type
-> Configure network (VPC/Subnet)
-> Add storage (EBS)
-> Set security group rules
-> Generate key pair
-> Launch instance
-> Connect via SSH/RDP
```

---

## Advantages of EC2

- Fast provisioning
- Flexible instance sizes
- Pay per use
- High availability with multi-AZ
- Easy scaling with Auto Scaling

## Limitations of EC2

- Requires server management (patching, updates)
- Costs can rise if not monitored
- Misconfiguration can lead to security risks

---

## Viva Questions (With Quick Answers)

### Basic Viva

**1. What is Amazon EC2?**
A web service that provides resizable virtual servers in the cloud.

**2. What is an EC2 instance?**
A virtual machine running on AWS infrastructure.

**3. What is an AMI?**
A template with OS and software used to launch instances.

**4. What is EBS?**
Persistent block storage for EC2 instances.

**5. What is a security group?**
A firewall that controls inbound and outbound traffic.

**6. What is a key pair?**
SSH credentials for secure instance login.

**7. What is Auto Scaling?**
A service that automatically adjusts the number of instances.

**8. What is ELB?**
A load balancer that spreads traffic across instances.

**9. What is CloudWatch?**
Monitoring service for metrics and logs.

**10. What is VPC?**
A private network in AWS for your resources.

### Intermediate Viva

**11. Why is EC2 called elastic?**
Because you can scale instances up or down based on demand.

**12. Difference between stop and terminate?**
Stop halts the instance but keeps EBS; terminate deletes the instance.

**13. What is the default port for SSH?**
22.

**14. What is the default port for HTTP/HTTPS?**
80 and 443.

**15. Why use multiple AZs?**
For high availability and fault tolerance.

**16. What is a public IP in EC2?**
An IP address for internet access to the instance.

**17. What is a private IP?**
An internal IP used inside the VPC.

**18. What is the role of IAM in EC2?**
Controls access and permissions for EC2 operations.

**19. What is an instance type?**
A predefined CPU/RAM/storage configuration.

**20. Why use EBS instead of instance store?**
EBS is persistent and survives instance stop.

### Advanced Viva

**21. Difference between horizontal and vertical scaling?**
Horizontal adds instances; vertical upgrades instance size.

**22. What is a user data script?**
Startup script executed when the instance launches.

**23. What is a snapshot in EC2?**
A backup of an EBS volume stored in S3.

**24. What is a placement group?**
Controls how instances are placed for low latency or high throughput.

**25. How do you secure EC2?**
Use security groups, IAM roles, key pairs, and patching.

**26. What is the benefit of spot instances?**
Lower cost but can be interrupted.

**27. What are reserved instances?**
Discounted pricing for long-term usage commitment.

**28. What is an Elastic IP?**
A static public IP address in AWS.

**29. What is the role of CloudWatch alarms?**
Trigger actions like auto scaling or notifications.

**30. Can EC2 host databases?**
Yes, but managed services like RDS reduce maintenance.

### External Examiner Trap Questions

**31. Can EC2 scale automatically without Auto Scaling?**
No, scaling must be managed manually or via Auto Scaling.

**32. Is EC2 serverless?**
No, it is server-based IaaS.

**33. Does EC2 provide built-in backup?**
No, backups are done using EBS snapshots.

**34. What happens if the instance fails?**
You can relaunch from AMI or use Auto Scaling and ELB to replace it.

**35. Why not host everything on one big instance?**
Single instance is a single point of failure and less scalable.

---

## Quick Memory Sheet

- **EC2 = Virtual servers**
- **AMI = Instance template**
- **EBS = Persistent disk**
- **SG = Firewall**
- **ELB = Traffic balancer**
- **Auto Scaling = Add/remove instances**
- **CloudWatch = Monitoring**

---

## Conclusion

Amazon EC2 provides flexible, scalable, and cost-effective compute resources. By combining EC2 with services like ELB, Auto Scaling, and CloudWatch, applications can remain highly available and performant. This case study highlights how EC2 is applied in real-world scenarios and prepares for common viva questions.
