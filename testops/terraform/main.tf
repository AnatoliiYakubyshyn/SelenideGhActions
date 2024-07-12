provider "github" {
  token = var.gh_token
}

provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "runner" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Name = "GitHubActionsRunner"
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install -y docker
              sudo service docker start
              sudo usermod -a -G docker ec2-user
              sudo curl -o /usr/local/bin/runner https://github.com/actions/runner/releases/download/v2.281.1/actions-runner-linux-x64-2.281.1.tar.gz
              sudo tar xzf ./runner -C /usr/local/bin
              sudo ./config.sh --url https://github.com/your-username/your-repo --token "${var.gh_token}"
              sudo ./svc.sh install
              sudo ./svc.sh start
              EOF

  lifecycle {
    ignore_changes = [user_data]
  }
}
