# Output the AMI ID used
output "ami_id" {
  value = data.aws_ami.ubuntu.id
}


# Output the public IP of the api EC2 instance
output "api_instance_ip" {
  value = aws_instance.api.public_ip
}

# Output the public IP of the training  EC2 instance
output "training_instance_ip" {
  value = aws_instance.training.public_ip
}
