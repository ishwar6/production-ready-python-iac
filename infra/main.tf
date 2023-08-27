terraform {
  backend "s3" {
    bucket         = "django-api-prod-ready"
    key            = "app.tfstate"
    region         = "us-west-2"
    encrypt        = true
    dynamodb_table = "django-api-prod-ready-lock"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.41.0"
    }
  }
}

provider "aws" {
  region = "us-west-2"
}

locals {
  prefix = "${var.prefix}-${terraform.workspace}"
  common_tags = {
    Environment = terraform.workspace
    Project     = var.project
    Owner       = var.contact
    ManagedBy   = "Ishwar"
  }
}

data "aws_region" "current" {}
