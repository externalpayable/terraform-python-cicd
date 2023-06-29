variable "aws_access_key" {
  description = "AWS access key"
}

variable "aws_secret_key" {
  description = "AWS secret key"
}

variable "aws_region" {
  description = "AWS region"
}

variable "instance_ami" {
  description = "AMI ID of the instance"
}

variable "instance_type" {
  description = "Instance type"
}

variable "key_name" {
  description = "SSH key pair name"
}

variable "subnet_id" {
  description = "Subnet ID"
}

variable "security_group_id" {
  description = "Security Group ID"
}
