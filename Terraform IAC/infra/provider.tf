terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

//Precisa pegar os dados da AWS, SG e criar um Bucket S3
provider "aws" {
    profile = "default"
    region  = "us-east-1"
}
