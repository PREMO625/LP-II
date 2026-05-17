# Oral Viva Guide - CC P01 (Amazon EC2)

## Quick One-Liners

- **EC2**: Virtual servers in AWS.
- **AMI**: Template to launch instances.
- **EBS**: Persistent block storage.
- **Security Group**: Instance firewall.
- **ELB**: Load balancer.
- **Auto Scaling**: Adds/removes instances.

---

## Basic Questions

1. What is Amazon EC2?
   - A service that provides resizable virtual servers in the cloud.
2. What is an EC2 instance?
   - A virtual machine running on AWS.
3. What is an AMI?
   - A template with OS and software to create an instance.
4. What is EBS?
   - Persistent storage attached to EC2.
5. What is a security group?
   - A firewall controlling inbound and outbound traffic.
6. What is a key pair?
   - SSH credentials used to log in.
7. What is an Elastic IP?
   - A static public IP address.
8. What is VPC?
   - A private AWS network for your resources.
9. What is CloudWatch?
   - Monitoring service for metrics and logs.
10. What is ELB?
    - Load balancer that distributes traffic.

---

## Intermediate Questions

11. Why is EC2 called elastic?
    - You can scale up or down based on demand.
12. Difference between stop and terminate?
    - Stop keeps EBS; terminate deletes the instance.
13. Default port for SSH?
    - 22.
14. Default ports for HTTP/HTTPS?
    - 80 and 443.
15. What is Auto Scaling?
    - Automatically adjusts number of instances.
16. What is an instance type?
    - Predefined CPU/RAM configuration.
17. Why use multiple Availability Zones?
    - High availability and fault tolerance.
18. Public IP vs private IP?
    - Public is internet-facing, private is internal.
19. What is a snapshot?
    - Backup of an EBS volume.
20. EBS vs instance store?
    - EBS is persistent, instance store is temporary.

---

## Advanced Questions

21. Horizontal vs vertical scaling?
    - Horizontal adds instances; vertical increases instance size.
22. What is a placement group?
    - Controls instance placement for low latency or high throughput.
23. What is a user data script?
    - Startup script executed on launch.
24. What are reserved instances?
    - Discounted pricing for long-term usage.
25. What are spot instances?
    - Low-cost instances that can be interrupted.
26. How do you secure EC2?
    - Security groups, IAM, key pairs, patching.
27. Can EC2 host databases?
    - Yes, but RDS is preferred for managed databases.
28. Why not use a single large instance?
    - Single point of failure and less scalable.
29. What is an IAM role for EC2?
    - Temporary permissions without storing keys.
30. What is a scale-out event?
    - Adding instances during high load.

---

## External Examiner Questions

31. Is EC2 serverless?
    - No, it is IaaS with server management.
32. Can EC2 scale without Auto Scaling?
    - Only manually, not automatically.
33. How do you reduce EC2 cost?
    - Right-sizing, reserved instances, spot instances.
34. What happens if an instance fails?
    - Replace manually or via Auto Scaling.
35. Why use load balancing?
    - To distribute traffic and avoid overload.

---

## Quick Memory Sheet

- EC2 = compute
- AMI = image
- EBS = storage
- SG = firewall
- ELB = traffic balance
- Auto Scaling = elasticity
