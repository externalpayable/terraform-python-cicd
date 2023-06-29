import subprocess
import json

# Function to execute Terraform commands
def execute_terraform_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing Terraform command: {e}")
        raise

# Function to parse Terraform output
def parse_terraform_output(output_file):
    try:
        with open(output_file, "r") as file:
            output_data = json.load(file)
            # Process the output as needed
            # Example: Extract relevant information from the output
            instance_id = output_data["instance_id"]
            public_ip = output_data["public_ip"]
            # Perform further actions with the parsed output
    except FileNotFoundError:
        print(f"Output file '{output_file}' not found")
        raise
    except json.JSONDecodeError as e:
        print(f"Error parsing Terraform output: {e}")
        raise

# Define the main function
def main():
    # Execute Terraform commands
    execute_terraform_command("terraform init")
    execute_terraform_command("terraform plan -out=tfplan")
    execute_terraform_command("terraform apply tfplan")

    # Parse Terraform output
    parse_terraform_output("terraform_output.json")

# Call the main function
if __name__ == "__main__":
    main()
