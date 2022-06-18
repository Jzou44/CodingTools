# Website coding.tools

### 配置nginx
```
35.239.243.94

apt-get install -y nginx
rm -rf /etc/nginx/sites-enabled/*
cp Config/mysite.conf /etc/nginx/sites-enabled/codingtools.conf
systemctl restart nginx
service nginx restart 
```
### 安装docker
```
https://docs.docker.com/engine/install/ubuntu/

apt-get install -y zip
mkdir -p /app
mkdir -p /app/log
mkdir -p /app/IP2Location
```
### 用ftp上传 ip_4_20210626.db

### build 并运行docker
```
git clone https://github.com/Jzou44/CodingTools.git

docker build -t codingtools:v20220618 .

docker run --rm -it -v /mnt/c/app:/app -v /mnt/c/tmp:/tmp -p 8080:8080 codingtools:v20220618 bash


docker run -d -v /mnt/c/app:/app -v /mnt/c/tmp:/tmp -p 8080:8080 codingtools:v20220618


docker run -d --restart=always -v /app:/app -v /tmp:/tmp -p 8080:8080 codingtools:v20220618


docker run --rm -it -v /app:/app -v /tmp:/tmp -p 8080:8080 codingtools:v20220618 bash
```

### 配置dns


### other
```
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890

git config --global --unset http.proxy
git config --global --unset https.proxy
```