# Create 3 EC2 in AWS
- all resources will be created in region `eu-north-1`

## Diagram
![](../../diagram/nomad-aws-diagram.png)

<br>



**Access by section:**
- [VPC](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#vpc-vpc)
- [internet-gateway](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#vpc-internet-gateway)
- [route table add default route](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#vpc-route-table)
- [create subnet](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#vpc-subnet)
- [security groups](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#ec2-security-groups)
- [key pairs](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#ec2-key-pairs)
- [IAM](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#iam-policy-and-role)
    - [policy: describe EC2 instances and EC2 tags](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#Create-iam-policy-to-describe-ec2-instances-and-ec2-tags)
    - [policy: EC2 autoscaling](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#create-iam-policy-that-allows-write-complete-lifecycle-actions-on-ec2-auto-scaling)
    - [IAM role](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#iam-role)
- [EC2 instances](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#ec2-instances)
    - [EC2 consul server](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#ec2-consul-server)
    - [EC2 nomad server](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#ec2-nomad-server)
    - [EC2 nomad client](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#ec2-nomad-client)
- [Verify Conectivity](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#verify-connectivity)
    - [from nomad-client](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#from-nomad-client)
    - [from nomad-server](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#from-nomad-server)
    - [from consul-server](https://github.com/ion-onboarding/nomad-aws/edit/main/manualy/infrastructure/README.md#from-consul-server)

## Select AWS Region
- Select AWS region where resources will be created
![](screenshots/2022-04-02-17-27-51.png)

## VPC: vpc
- search and access the vpc service

![](screenshots/2022-04-02-17-32-10.png)

- launch VPC
    - access Virtual Private Cloud
    - click Launch VPC Wizzard

![](screenshots/2022-04-02-17-35-17.png)

- create VPC
    - select `VPC only` option and provide a name
    - for CIDR choose a big enough network to allow growth in future
    - optionally add tags
    - click `Create VPC`

![](screenshots/2022-04-02-17-39-58.png)

- enable DNS hostnames on vpc
    - click `Actions` > `Edit DNS hostnames`

![](screenshots/2022-04-02-18-25-58.png)

- enable check box under `DNS hostnames`
    
![](screenshots/2022-04-02-18-26-49.png)

- verify that VPC is displayed
    - choose `Virtual Private Cloud` > `Your VPCs`
    - search for the VPC `Name` and `VPC ID` created

![](screenshots/2022-04-02-18-27-37.png)

## VPC: Internet Gateway
- create internet gateway
    - select VPC services > `Virtual Private Cloud` > `Internet Gateway`
    - click `Create internet gateway` button

![](screenshots/2022-04-02-18-30-56.png)
- give the internet gateway a `Name tag`
- optionally enter tags lebels
- click `Create internet gateway`

![](screenshots/2022-04-02-18-32-51.png)

- verify the details of the internet gateway created
    - after creation details of the VPC will be displayed

![](screenshots/2022-04-02-18-33-49.png)

### Attach internet gateway to VPC

- select `Actions` > `Attach to VPC`

![](screenshots/2022-04-02-18-35-49.png)

- choose VPC to which to attach this internet gatway
    - search for the VPC created earlier
    - click `Attach internet gateway`

![](screenshots/2022-04-02-18-36-47.png)

- verify that internet gateway was attached to VPC
    - in the VPC details page verify the `State` displays `Attached`

![](screenshots/2022-04-02-18-56-57.png)

## VPC: Route Table

### Point `default route` to `internet gateway`
- access VPC created

![](screenshots/2022-04-02-18-59-33.png)

- access route table associated with vpc

![](screenshots/2022-04-02-19-00-47.png)

- select routes
    - in the new route table page select `Routes`

![](screenshots/2022-04-02-19-01-42.png)

- edit routes
    - click `Edit Routes` button

![](screenshots/2022-04-02-19-02-30.png)
- add route button
    - in the new menu click `Add route` button

![](screenshots/2022-04-02-19-03-25.png)

- add route details
    - destination `0.0.0.0/0`
    - at Target type `internet gateway`
    - in the dropdown select `Internetg Gateway`

![](screenshots/2022-04-02-19-07-24.png)

- add Target
    -   select the `internet gateway id` created at earlier step

![](screenshots/2022-04-02-19-08-25.png)

- verify 
    - route `0.0.0.0/0` points to `internet gateway`
    - status is `Active`

![](screenshots/2022-04-02-19-09-12.png)


## VPC: Subnet
- create a new subnet
    - under VPC service, select `Virtual Private Cloud` > `Subnets`
    - click `Create Subnet` button
    
![](screenshots/2022-04-02-19-10-25.png)

- enter subnet details
    - choose VPC where this subet will be attached
    - enter the `Subnet name`, `Availability Zone` and `IPv4 CIDR block`
    - optionaly add `Tags`
    - click `Create Subnet` button

![](screenshots/2022-04-02-19-12-13.png)

- verify that subnet is created
    -   right after subet creation new subnet is automatically filtered
    -   check that subnet lists `Available` and attached to the correct VPC

![](screenshots/2022-04-02-19-12-44.png)


## EC2: Security Groups

- access ec2 services
    - click search button and search `ec2`
    - click `EC2`

![](screenshots/2022-04-02-19-14-25.png)

- access `Network & Security` > `Security Groups`

![](screenshots/2022-04-02-19-15-41.png)

- create a new `security group`
    - click `Create security group`

![](screenshots/2022-04-02-19-16-35.png)

- add new `security group` details
    - enter a `Security group name` and `Description`
    - search and add VPC created earlier
    - inbound rules (allow any in)
        - Type: `All traffic`
        - Source Type: `Anywhere-IPv4`
    - output rules (allow any out)
        - Type: `All traffic`
        - Destination type: `Custom`
        - Destination: `0.0.0.0/0`
     - click `Create security group`
 
![](screenshots/2022-04-02-19-27-49.png)

- verify
    - check the `inbound` and `output` rules added and correct

![](screenshots/2022-04-02-19-29-44.png)

## EC2: Key Pairs
- access EC2 `Key Pairs` service
    - select `Network & Security` > `Key Pairs`
    - click `Create key pair` button
   
![](screenshots/2022-04-02-19-36-50.png)

- enter `Key pair` details
    - give a name,
    - Key Pair type: `RSA`
    - Priavte key file format: `.pem`
    - click `Create key pair` button
   
![](screenshots/2022-04-02-19-37-59.png)

- private key is automatically downloaded

![](screenshots/2022-04-02-19-42-45.png)

## IAM: policy and role

- access Identity and Access Management services
    -   in search bar type `iam
    -   click `IAM Manage access to AWS resources`
    
![](screenshots/2022-04-02-20-15-25.png)

### Create IAM policy to describe EC2 instances and EC2 tags
- select `Access Management` > `Policies`
    - click `Create Policy` button
    
![](screenshots/2022-04-02-20-23-07.png)

- add policy elements
    - select EC2 service
    - choose `DescribeInstances` and `DescribeTags`
    
![](screenshots/2022-04-02-20-33-20.png)

- optionally view policy details in JSON format
    - click `JSON` tab
    - then `Next Tags` button
    
![](screenshots/2022-04-02-20-34-58.png)

- optionally add tags
    - click Next Review
    
![](screenshots/2022-04-02-20-48-06.png)

- Review policy details
    - give policy a `Name` and `Description`
    - click `Create policy`
    - verify the policy details
        - Service
        - Access level
        - Resource
     - click `Create Policy button`
     
![](screenshots/2022-04-02-20-52-25.png)


### Create IAM policy that allows write complete lifecycle actions on `EC2 auto scaling`
- select `Access Management` > `Policies`
    - click `Create Policy`
   
![](screenshots/2022-04-02-21-00-29.png)

- select
    - service: `EC2 Ato Scaling`
    - Actions: Write > `CompleteLifecycleAction`
    - Resources: `All resources`
    - click `Next: Tags` button
   
![](screenshots/2022-04-02-21-03-37.png)

- view policy created in `JSON` format
    - click `JSON` tab
    - click `Next:Tags` button
    
![](screenshots/2022-04-02-21-04-25.png)

- optionally assign tags
    - click `Next: Review` button
    
![](screenshots/2022-04-02-21-05-27.png)

- Review Policy
    - give policy a `Name` and `Description`
    - verify the policy details
        - Service
        - Access level
        - Resource
       
![](screenshots/2022-04-02-21-07-29.png)

- policy created
    - verify under `Access Management` > `Policies` the new policy
    
![](screenshots/2022-04-02-21-08-54.png)

### IAM role
- access `Access Management` > `Roles`
    - click `Create role` button
    
![](screenshots/2022-04-02-20-17-42.png)

- role details
    - use `AWS service`
    - select `EC2`
    - click `Next` button
    
![](screenshots/2022-04-02-20-19-09.png)

- Add role Permissions, that means policies created earlier
    - search policy name `ec2-describe-instance-describe-tags`
    - select the policy
    - click `Next` button
    
<!-- ![](screenshots/2022-04-02-21-17-05.png) -->

   
![](screenshots/2022-04-02-21-19-48.png)

- role name, review and create
    - give this role a name
    - review details (who will assume the role)
    - select the two policies created earlier
        - one for `EC2`
        - one for `EC2 auto scaling`

![](screenshots/2022-04-02-21-22-25.png)

- iam role was created
    - in the new should automatically have selected the role name
    
![](screenshots/2022-04-02-21-23-41.png)

## EC2: Instances

- access ec2 services
    - click search button and search `ec2`
    - click `EC2`

![](screenshots/2022-04-02-19-14-25.png)

- select the region
    - click the region where resources should be created
    
![](screenshots/2022-04-02-21-25-21.png)

### EC2 consul-server
- access `EC2 Instances` > `Instacnes`
    - click `Launch instances` button
    
![](screenshots/2022-04-02-19-44-55.png)

- configure ec2 instance ( add components created earlier)
    - give a `Name`
    - use `Ubuntu` OS
    - instance type
    - search for the `Key pair`
    - search for VPC and subnet
    - Auto-assign public IP: Enabled
        - this public IP will be used to access the instance
    - select the security group
    - IAM instance profile
        - use iam role created earlier
    - review the Summary
    - click `Launch instance` button
    
![](screenshots/2022-04-02-21-33-30.png)

- view the consul-server
    -  access under `EC2 instances` > `Instances`
    -  search `consul-serevr`
    
![](screenshots/2022-04-02-21-35-17.png)

- verify IPs attached to consul-server
    -  select `consul-server`
    -  click `Actions` > `View details`
    
![](screenshots/2022-04-02-21-39-25.png)

-  note the public/private IPs

![](screenshots/2022-04-02-21-40-49.png)

### EC2 nomad-server

- access `EC2 Instances` > `Instances`
    - click `Launch instances` button

![](screenshots/2022-04-02-19-44-55.png)

- configure ec2 instance ( add components created earlier)
    - give a `Name`
    - use `Ubuntu` OS
    - instance type
    - search for the `Key pair`
    - search for VPC and subnet
    - Auto-assign public IP: Enabled
        - this public IP will be used to access the instance
    - select the security group
    - IAM instance profile
        - use iam role created earlier
    - review the Summary
    - click `Launch instance` button

![](screenshots/2022-04-02-21-46-54.png)

- view the nomad-server
    -  access under `EC2 instances` > `Instances`
    -  search `nomad-server`
    
![](screenshots/2022-04-02-21-48-20.png)

- verify IPs attached to consul-server
    -  select `consul-server`
    -  click `Actions` > `View details`

![](screenshots/2022-04-02-21-49-43.png)

-  note the public/private IPs

![](screenshots/2022-04-02-21-50-43.png)


### EC2 nomad-client

- access `EC2 Instances` > `Instances`
    - click `Launch instances` button
    
![](screenshots/2022-04-02-21-51-56.png)

- configure ec2 instance ( add components created earlier)
    - give a `Name`
    - use `Ubuntu` OS
    - instance type
    - search for the `Key pair`
    - search for VPC and subnet
    - Auto-assign public IP: Enabled
        - this public IP will be used to access the instance
    - select the security group
    - IAM instance profile
        - use iam role created earlier
    - review the Summary
    - click `Launch instance` button

![](screenshots/2022-04-02-21-57-20.png)

- view the nomad-server
    -  access under `EC2 instances` > `Instances`
    -  search `nomad-client`

![](screenshots/2022-04-02-21-59-00.png)

- verify IPs attached to consul-server
    -  select `consul-server`
    -  click `Actions` > `View details`

![](screenshots/2022-04-02-22-00-08.png)

-  note the public/private IPs

![](screenshots/2022-04-02-22-00-45.png)

### Verify connectivity
### From nomad-client

- select the ec2 instance
    - click `Actions` > `Connect`

![](screenshots/2022-04-02-22-03-54.png)

- select `EC2 Instance Connect`
    - click `Connect` button

![](screenshots/2022-04-02-22-05-10.png)

- verify connectivity with ping
    - ping `consul-server`
    - ping `nomad-server`

![](screenshots/2022-04-02-22-07-34.png)

### From nomad-server
- select the ec2 instance
    - click `Actions` > `Connect`

![](screenshots/2022-04-02-22-09-13.png)

- select `EC2 Instance Connect`
    - click `Connect` button

![](screenshots/2022-04-02-22-09-57.png)

- verify connectivity with ping
    - ping `consul-server`
    - ping `nomad-client`

![](screenshots/2022-04-02-22-12-20.png)

### From consul-server

- select the ec2 instance
    - click `Actions` > `Connect`

![](screenshots/2022-04-02-22-13-17.png)

- select `EC2 Instance Connect`
    - click `Connect` button

![](screenshots/2022-04-02-22-13-47.png)

- verify connectivity with ping
    - ping `nomad-server`
    - ping `nomad-client`

![](screenshots/2022-04-02-22-15-20.png)
