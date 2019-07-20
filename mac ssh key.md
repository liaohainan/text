## 步骤1.检查是否已经存在SSH Key
打开电脑终端，输入以下命令：
```
ls -al ~/.ssh
```
会出现两种情况
## 步骤2. 生成/设置SSH Key

继续上一步可能出现的情况

- （1）情况一：终端出现文件id_rsa.pub 或 id_dsa.pub，则表示该电脑已经存在SSH Key，此时可继续输入命令：

//将公钥放到剪切板
```
pbcopy < ~/.ssh/id_rsa.pub
```
这样你需要的SSH Key 就已经复制到粘贴板上了，然后进行步骤3
- （2）情况二：终端未出现id_rsa.pub 或 id_dsa.pub文件，表示该电脑还没有配置SSH Key，此时需要输入命令：
```
ssh-keygen -t rsa -C "your_full_name@xxxxx.com"
```
（注意，这里的 your_full_name@xxxxx.com 是你自己的公司邮箱） 默认会在相应路径下（/your_home_path）生成id_rsa和id_rsa.pub两个文件，此时终端会显示：
Generating public/private rsa key pair.

Enter file in which to save the key (/your_home_path/.ssh/id_rsa):

连续回车即可，也可能会让你输入密码，密码就是你的开机密码

此时再输入命令：ls -al ~/.ssh 就会出现id_rsa.pub 和 id_dsa.pub两个文件，然后重复情况一的步骤即输入以下命令再进行步骤3即可：
```
pbcopy < ~/.ssh/id_rsa.pub
```
## 步骤3.将SSH Key添加到GitLab中

打开GitLab, 登录，找到左边栏有一个的按钮，点击“ADD SSH KEY”按钮添加，将已经获得的SSH Key粘贴到“Key”，下边的标题可以随便取，点击加入项目，这样就保持了本地与服务器端的联系.
""已替换为 Profile Setting里的"SSH Key"
