terraform {
  backend "s3" {
    bucket = "terraform-state-rog"
    key    = "prod/terraform.tfstate"
    region = "us-west-2"
  }
}