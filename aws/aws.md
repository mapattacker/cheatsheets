# AWS CLI

[AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is essential for passing commands to AWS in shell.

 * aws cli can be installed as a docker container or within the command line

# AWS Configure

 * `aws configure`: enter access, secret & region names, for default profile
 * `aws configure --profile <name>`: enter access, secret & region names, based on a specific name
 * `nano ~/.aws/credentials`: add/edit profile keys directly from here
 * `aws s3 ls --profile <name>`: enter commands based on profile

# Create Access & Secret Keys

 * Go to account > My Security Credentials > Access Keys > Create Access Keys
 * We can create user accounts for specific user groups, and tag certain policies to it, such that the access & secret keys created are specific to those purposes

# Policy

 * Policies defines access rights and functions, so that it can be used to tie to specific users. Examples:
   * S3, specific bucket access

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
                "arn:aws:s3:::scene-images",
                "arn:aws:s3:::scene-images/*",
                "arn:aws:s3:::mediacorpus-s3",
                "arn:aws:s3:::mediacorpus-s3/*"
            ]
        }
    ]
}
```

# S3 Bucket

 * `aws s3 cp s3://bucketname/foldername localdirectory --recursive`: download all data from s3 folder
 * Best Practices
   * S3 buckets should have server-side encryption enabled
   * S3 buckets should prohibit public read access

# Elastic Container Registry

 * Search for Amazon ECR > Create a repository
 * Click `View Push Commands` to follow the directions on how to push docker images to this repository
 * [Gitlab CI/CD](https://gitlab.com/help/ci/cloud_deployment/index.md#aws) or this medium [article](https://medium.com/@stijnbe/using-gitlab-ci-with-aws-container-registry-ecaf4a37d791) to push to ECR
 * To limit the number of images being stored, we can set a rule under (Lifetime Policy)[https://aws.amazon.com/blogs/compute/clean-up-your-container-images-with-amazon-ecr-lifecycle-policies/] to remove untagged images based on counts

# EC2 Instances

## Key-Pair

 * Generate a key-pair & download a file `*.pem`. Note: a `*pem.txt` will be downloaded; remove the `.txt` extension.
 * We need to restrict permissions to the pem file `chmod 400 *.pem` in order for it to be used
 * To ssh, `ssh -i *.pem ubuntu@ipaddress`

## Security Groups

 * To limit ports to the WWW, go Network & Security > Security Groups
 * We can also assign SSH specifically to a specific host IP address, e.g. home wifi

## Elastic IP

 * To fix an IP address so that it will not be changed everytime the EC2 is restarted, go to Network & Security > Elastic IPs
 * Select Allocate Elastic IP address button > Allocate (an unallocated Elastic IP will be used) > Give a Name > Select Actions button > Associate Elastic IP address
 * Select an instance you to want link the Elastic IP to
 * After assigning, you may need to:
    * hosted zones (route 53) to reassign the new elastic IP to your host name
    * restart your server, e.g. `sudo service nginx restart`