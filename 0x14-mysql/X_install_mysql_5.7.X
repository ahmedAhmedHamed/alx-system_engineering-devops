#!/usr/bin/env bash
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C
sudo apt update
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf


CHANGE REPLICATION SOURCE TO
SOURCE_HOST = '54.88.164.246',
SOURCE_USER = 'replica_user',
SOURCE_PASSWORD = 'amongus',
SOURCE_LOG_FILE = 'mysql-bin.000001',
SOURCE_LOG_POS = 154;

+++

CHANGE MASTER TO 
MASTER_HOST='54.88.164.246',
MASTER_USER='replica_user',
MASTER_PASSWORD='amognus',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=154;