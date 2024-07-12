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
  provisioner "local-exec" {
    #!/bin/bash
    # Create a folder
    command = <<EOT
    sudo mkdir actions-runner && cd actions-runner# Download the latest runner package
    sudo curl -o actions-runner-linux-x64-2.317.0.tar.gz -L https : //github.com/actions/runner/releases/download/v2.317.0/actions-runner-linux-x64-2.317.0.tar.gz# Optional: Validate the hash
    sudo echo "9e883d210df8c6028aff475475a457d380353f9d01877d51cc01a17b2a91161d  actions-runner-linux-x64-2.317.0.tar.gz" | shasum -a 256 -c# Extract the installer
    sudo tar xzf ./actions-runner-linux-x64-2.317.0.tar.gz
    ./config.sh --url https : //github.com/AnatoliiYakubyshyn/SelenideGhActions --token "${var.gh_token}"
    ./run.sh
  EOT
    interpreter = ["bash", "-c"]

  }
}
