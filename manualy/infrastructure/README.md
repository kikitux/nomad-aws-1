# create 3 vms in AWS
- all resources will be created in region `eu-north-1`

## AWS Region
- Select AWS region
![](screenshots/2022-04-02-17-27-51.png)

## VPC: vpc
- search vpc services
![](screenshots/2022-04-02-17-32-10.png)

- caunch VPC
![](screenshots/2022-04-02-17-35-17.png)

- create VPC
![](screenshots/2022-04-02-17-39-58.png)

- enable DNS hostnames on vpc
![](screenshots/2022-04-02-18-25-58.png)
![](screenshots/2022-04-02-18-26-49.png)
![](screenshots/2022-04-02-18-27-37.png)

## VPC: Internet Gateway
- create internet gateway
![](screenshots/2022-04-02-18-30-56.png)
![](screenshots/2022-04-02-18-32-51.png)
![](screenshots/2022-04-02-18-33-49.png)

- attach internet gateway to VPC
![](screenshots/2022-04-02-18-35-49.png)
![](screenshots/2022-04-02-18-36-47.png)
![](screenshots/2022-04-02-18-56-57.png)

## VPC: Route Table default route to internet
- access VPC created
![](screenshots/2022-04-02-18-59-33.png)
- access route table associated with vpc
![](screenshots/2022-04-02-19-00-47.png)
- select routes
![](screenshots/2022-04-02-19-01-42.png)
- edit routes
![](screenshots/2022-04-02-19-02-30.png)
- add route button
![](screenshots/2022-04-02-19-03-25.png)
- enter route details, point default route to internet gateway
![](screenshots/2022-04-02-19-07-24.png)
![](screenshots/2022-04-02-19-08-25.png)
![](screenshots/2022-04-02-19-09-12.png)


## VPC: Subnet
- create a net subnet
![](screenshots/2022-04-02-19-10-25.png)
![](screenshots/2022-04-02-19-12-13.png)
![](screenshots/2022-04-02-19-12-44.png)


## EC2: ec2
- access ec2 services
![](screenshots/2022-04-02-19-14-25.png)

## EC2: Security Groups
- access security group menu
![](screenshots/2022-04-02-19-15-41.png)
- create security group
![](screenshots/2022-04-02-19-16-35.png)
- select vpc created earlier and allow all traffic in and out
    - this is only temporary to demonstrate a working scenario
![](screenshots/2022-04-02-19-27-49.png)
![](screenshots/2022-04-02-19-29-44.png)

## EC2: Key Pairs
- access EC2 `Key Pairs` service
![](screenshots/2022-04-02-19-36-50.png)
![](screenshots/2022-04-02-19-37-59.png)
- private key is automatically downloaded
![](screenshots/2022-04-02-19-42-45.png)

## IAM: policy and role
- access Identity and Access Management services
![](screenshots/2022-04-02-20-15-25.png)

### IAM policy to describe EC2 instances and tags
![](screenshots/2022-04-02-20-23-07.png)
- select EC2 service with `DescribeInstances` and `DescribeTags`
![](screenshots/2022-04-02-20-33-20.png)
- JSON policy looks like this
![](screenshots/2022-04-02-20-34-58.png)
- optionally add tags
![](screenshots/2022-04-02-20-48-06.png)
- attach to policy and create the policy
![](screenshots/2022-04-02-20-52-25.png)
- policy `ec2-describe-instance-describe-tags` is created

### IAM policy allows write complete lifecycle actions on EC2 auto scaling
- create a new policy
![](screenshots/2022-04-02-21-00-29.png)
![](screenshots/2022-04-02-21-03-37.png)
- how policy looks like in JSON format
![](screenshots/2022-04-02-21-04-25.png)
- optionally assign tags
![](screenshots/2022-04-02-21-05-27.png)
- give policy a name `ec-autoscaling-write-complete-lifecycle`
![](screenshots/2022-04-02-21-07-29.png)
- policy created
![](screenshots/2022-04-02-21-08-54.png)

### IAM role to be assumed by an EC2 instance
- create role named `ec2-iam-nomad-consul`
![](screenshots/2022-04-02-20-17-42.png)
- use AWS service and EC2 instance
![](screenshots/2022-04-02-20-19-09.png)
- Add Permissions
    - select policy `ec2-describe-instance-describe-tags`
![](screenshots/2022-04-02-21-17-05.png)
    - select policy `ec-autoscaling-write-complete-lifecycle`
![](screenshots/2022-04-02-21-19-48.png)

- give role a name, `ec2-iam-nomad-consul`
![](screenshots/2022-04-02-21-22-25.png)

- iam role created
![](screenshots/2022-04-02-21-23-41.png)

## EC2: Instances
- select `eu-north-1`
![](screenshots/2022-04-02-21-25-21.png)

### consul-server
- access and Launch an EC2 instance menu
![](screenshots/2022-04-02-19-44-55.png)
- attach to the ec2 instance all components created earlier
![](screenshots/2022-04-02-21-33-30.png)
- consul-server is created
![](screenshots/2022-04-02-21-35-17.png)
- verify IPs attached to consul-server
![](screenshots/2022-04-02-21-39-25.png)
![](screenshots/2022-04-02-21-40-49.png)

### nomad-server
- access and Launch an EC2 instance menu
![](screenshots/2022-04-02-19-44-55.png)

- instance details: nomad-server
    - attach all details created earlier
    ![](screenshots/2022-04-02-21-46-54.png)
- nomad-server is created
![](screenshots/2022-04-02-21-48-20.png)
- verify IPs attached to nomad-server
![](screenshots/2022-04-02-21-49-43.png)
![](screenshots/2022-04-02-21-50-43.png)


### nomad-client
- access and Launch an EC2 instance menu
![](screenshots/2022-04-02-21-51-56.png)

- instance details: nomad-client
    -   attach all details created earlier
    ![](screenshots/2022-04-02-21-57-20.png)
- nomad-client is created
![](screenshots/2022-04-02-21-59-00.png)
- verify IPs nomad-client
![](screenshots/2022-04-02-22-00-08.png)
![](screenshots/2022-04-02-22-00-45.png)

### Verify there is connectivity
### From nomad-client
![](screenshots/2022-04-02-22-03-54.png)
![](screenshots/2022-04-02-22-05-10.png)
![](screenshots/2022

### From nomad-server
![](screenshots/2022-04-02-22-09-13.png)
![](screenshots/2022-04-02-22-09-57.png)
![](screenshots/2022-04-02-22-12-20.png)

### From consul-server
![](screenshots/2022-04-02-22-13-17.png)
![](screenshots/2022-04-02-22-13-47.png)
![](screenshots/2022-04-02-22-15-20.png)
