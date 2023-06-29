import subprocess

# Function to execute Terraform validate command
def validate_terraform_config():
    try:
        subprocess.run("terraform validate", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Terraform configuration validation failed: {e}")
        raise

# Define the main function
def main():
    # Validate Terraform configuration
    validate_terraform_config()

# Call the main function
if __name__ == "__main__":
    main()
