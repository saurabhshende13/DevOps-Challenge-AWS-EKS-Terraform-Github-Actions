variable "cluster_name" {
  description = "name of the EKS cluster"
  type        = string
}

variable "key_name" {
  description = "name of the Key Pair"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
}

variable "public_subnet" {
  description = "CIDR blocks for public subnets"
  type        = string
}

variable "private_subnets" {
  description = "CIDR blocks for private subnets"
  type        = list(string)
}


variable "environment" {
  description = "Environment Name"
  type        = string
} 