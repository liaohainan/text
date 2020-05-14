- 登录
```shell
docker login
docker build -t testnginx .

docker image ls | grep testnginx

docker run -p 3000:80 -d --name app4 test2

docker tag nginx:latest nginx:1.0.0
docker push nginx:1.0.0

运行镜像
docker run -itd --name node-test node

根据id构建镜像
docker commit 0b19f417a1db node-cnpm:12.12

还可以通过dockerfile创建

FROM centos:7
RUN yum install -y vim

docker build -t chanmufeng/centos-vim2 .

```
