# F5-BIG-IP-RCE-vul_check
F5-BIG-IP-RCE漏洞检测脚本


# 免责声明
使用本程序请自觉遵守当地法律法规，出现一切后果均与作者无关。

本工具旨在帮助企业快速定位漏洞修复漏洞,仅限授权安全测试使用!

严格遵守《中华人民共和国网络安全法》,禁止未授权非法攻击站点!

由于用户滥用造成的一切后果与作者无关。

切勿用于非法用途，非法使用造成的一切后果由自己承担，与作者无关。


# F5-BIG-IP-RCE漏洞检测脚本

### 食用方法

```
python .\f5-big-ip-rce.py -u https://xx.xx.xx.xx
```

效果图

未发现漏洞

![image](https://github.com/FeiNiao/F5-BIG-IP-RCE-vul_check/assets/66779835/09fee2fa-03b8-4d14-bec4-a3361164edac)


疑似发现漏洞，漏洞存在会返回执行id命令的结果

![image](https://github.com/FeiNiao/F5-BIG-IP-RCE-vul_check/assets/66779835/be3a6e42-aa0b-49dc-be1e-aa411d07d21d)


