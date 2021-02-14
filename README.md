# python-Defense-dos
简单的Linux+python防御dos

适合Linux简单的防御dos，自己可以调整连接数阈值(默认500)
解除方法
iptables -D INPUT -s ***.***.***.*** -j DROP
