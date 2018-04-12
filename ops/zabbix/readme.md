
## dell_idrac_zbx_template.xml

dell idrac snmp 模板，里面有一个bak原版，一个做了一些修改，修改了部分获取时间。另外增加了一个system Power State，开机为4，关机为3，其他状态未知
增加了voltage enum discovery的trigger的依赖，主机关机的情况下，这些状态都会取不到而引起报警，增加一个依赖以防止这个情况发生