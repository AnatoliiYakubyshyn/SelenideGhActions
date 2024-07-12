variable "gh_token" {
  description = "The GitHub token for authentication"
  type        = string
}

variable "aws_region" {
  description = "The AWS region to deploy resources in"
  default     = "us-west-2"
}

variable "instance_type" {
  description = "The type of instance to create"
  default     = "t3.micro"
}

variable "ami_id" {
  description = "The AMI ID to use for the instance"
  default     = "ami-0249211c9916306f8"
}
