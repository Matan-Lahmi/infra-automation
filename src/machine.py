import logging

class Machine:
    def __init__(self, name, os, cpu, ram):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram

    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }

    def log_creation(self):
        print(f"Provisioning {self.name}: {self.os}, {self.cpu}, {self.ram}")
        logging.info(f"Provisioning {self.name}: {self.os}, {self.cpu}, {self.ram}")