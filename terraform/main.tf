provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  region     = var.aws_region
}

terraform {
  backend "s3" {
    bucket         = "your-terraform-bucket"
    key            = "your-terraform-state-file"
    region         = var.aws_region
    dynamodb_table = "your-dynamodb-lock-table"
  }
}

# Define resources
resource "aws_instance" "example" {
  ami           = var.instance_ami
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = var.subnet_id
  security_group_ids = [var.security_group_id]
}
