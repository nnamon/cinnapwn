// Monitor flags for correction. Then rectify that.
// by amon (amon@nandynarwhals.org)

#include <stdlib.h>
#include <unistd.h>

int main() {
    while (1) {
        system("chattr -i /srv/www/htdocs/index.html");
        system("cat /srv/www/htdocs/index.html | md5sum | grep fa477c36d6c52d52bbd9b6af7df708fa && sed -i 's/service\\./service. /g' /srv/www/htdocs/index.html");
        system("chattr +i /srv/www/htdocs/index.html");
        system("chattr -i /var/ftp/welcome.msg");
        system("cat /var/ftp/welcome.msg | md5sum | grep df35704116608a3ed56f6710fe7e3b07 && sed -i 's/,//g' /var/ftp/welcome.msg");
        system("chattr +i /var/ftp/welcome.msg");
        system("chattr -i /home/public/file");
        system("cat /home/public/file | md5sum | grep 4d91498a12508cd7f51fe6d5265ee521 && sed -i 's/ts/t/g' /home/public/file");
        system("chattr +i /home/public/file");
        sleep(2);
    }
}
