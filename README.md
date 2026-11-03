# AWS Mass Email Automation Using S3, Lambda & SES

## 📌 Project Overview
This project automates email delivery using AWS services. When a CSV file containing recipient details is uploaded to an Amazon S3 bucket, an AWS Lambda function is triggered to process the file and send emails using Amazon Simple Email Service (SES).

## 🎯 Objective
To automate bulk email delivery without manually sending individual emails.

## ☁️ AWS Services Used
- **Amazon S3:** Stores the CSV recipient file.
- **AWS Lambda:** Processes the CSV file automatically.
- **Amazon SES:** Sends emails to verified recipients.
- **AWS IAM:** Provides permissions to Lambda.
- **Amazon CloudWatch:** Monitors Lambda execution logs.

## 🔄 Project Workflow
1. Upload a CSV file containing recipient email addresses to S3.
2. S3 triggers the Lambda function.
3. Lambda reads and processes the CSV file.
4. Lambda uses Amazon SES to send emails.
5. CloudWatch records execution logs.

## 🛠️ Implementation
- Created an S3 bucket.
- Uploaded a CSV recipient file.
- Created a Lambda function using Python.
- Configured an S3 event trigger.
- Created an IAM role with required permissions.
- Configured Amazon SES for email delivery.
- Checked execution logs using CloudWatch.

## ✅ Result
Successfully tested automated email delivery using Amazon S3, Lambda and SES.

## 📚 Skills Demonstrated
AWS Cloud, Serverless Computing, Python, IAM, Event-Driven Automation and Cloud Monitoring.

## 👩‍💻 Author
Velupula Mounika




## 🏗️ AWS Architecture

```text
Recipient CSV File
       |
       v
   Amazon S3
       |
       | S3 Event Trigger
       v
   AWS Lambda
   (Python)
       |
       v
   Amazon SES
       |
       v
  Email Delivery

Amazon CloudWatch
(Monitors Lambda Logs)
```


