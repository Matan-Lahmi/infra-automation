import json
import jsonschema
import subprocess
import logging
from machine import Machine
from logger import setup_logging

logger = setup_logging()

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "os": {"type": "string", "enum": ["Ubuntu", "CentOS", "Windows"]},
        "cpu": {"type": "string"},
        "ram": {"type": "string"}
    },
    "required": ["name", "os", "cpu", "ram"]
}

def validate_instance_input(data):
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except jsonschema.ValidationError as e:
        logging.error(f"Invalid input: {e.message}")
        print(f"[ERROR] Invalid input: {e.message}")
        return False

def run_setup_script():
    try:
        subprocess.run(["bash", "scripts/setup_nginx.sh"], check=True)
        logging.info("Nginx installation completed.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to install Nginx: {e}")

def get_user_input():
    machines = []
    logging.info("Provisioning started.")

    while True:
        name = input("Enter machine name (or 'done' to finish): ")
        if name.lower() == "done":
            break

        os = input("Enter OS (Ubuntu/CentOS/Windows): ")
        cpu = input("Enter CPU (e.g., 2vCPU): ")
        ram = input("Enter RAM (e.g., 4GB): ")

        instance_data = {"name": name, "os": os, "cpu": cpu, "ram": ram}

        if validate_instance_input(instance_data):
            machine = Machine(name, os, cpu, ram)
            machine.log_creation()
            machines.append(instance_data)
        else:
            print("Try again...")

    logging.info("Provisioning completed.")
    return machines

if __name__ == "__main__":
    instances = get_user_input()

    with open("configs/instances.json", "w") as f:
        json.dump(instances, f, indent=4)

    print("Saved successfully to configs/instances.json")
    logging.info("Instances saved to configs/instances.json")