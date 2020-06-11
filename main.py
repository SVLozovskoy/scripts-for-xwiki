import os

def pkg_install():
    os.system('apt-get install docker docker.io docker-compose')
    os.system('apt-get install openssl')

def ssl_generate():
    os.system('mkdir cert')
    os.system('sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./cert/nginx.key -out cert/nginx.crt -subj "/C=US/ST=Ohio/L=Columbus/O=Widgets Inc/OU=Some Unit"')


def change_right():
    os.system('chmod -R 777 cert')
    print('done')

def run_docker():
    os.system('docker-compose up')

pkg_install()
ssl_generate()
change_right()
run_docker()
