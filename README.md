# UNIT6_RPM
Creating own rpm from python source

### 1. Cоздать свой RPM (можно взять свое приложение, либо собрать к примеру апач с определенными опциями)

***- Запустим [Vagrantfile](https://github.com/ChurikovAnatolii/UNIT6_RPM/blob/main/Vagrantfile), установим rpmdevtools, rpm-build***

> yum install rpmdevtools rpm-build  
> rpmdev-setuptree **- Создадим окружение для сборки пакета**  

***- Скопируем [bash-script из предыдушего урока ](https://github.com/ChurikovAnatolii/Vagant_soft_RAID/blob/main/raid_add.sh) в папку /SOURCE, упакуем в tar.gz***  

> wget https://github.com/ChurikovAnatolii/Vagant_soft_RAID/archive/refs/heads/main.zip  
> unzip main.zip  
> cp main raid_create-1.0  
> tar -czf raid_create-1.0.tar.gz /raid_create-1.0

***- Создадим [spec-файл](https://github.com/ChurikovAnatolii/UNIT6_RPM/blob/main/raid.spec) в папке /SPECS, создадим [RPM-пакет]()***  

> rpmbuild -bb raid.spec 

>  rpm -qi raid_create-1.0-1.el8.noarch.rpm ** - Посмотрим информацию о пакете  
>> Name        : raid_create  
>> Version     : 1.0  
>> Release     : 1.el8  
>> Architecture: noarch  
>> Install Date: (not installed)  
>> Group       : Unspecified  
>> Size        : 640  
>> License     : GPLv3+  
>> Signature   : (none)  
>> Source RPM  : raid_create-1.0-1.el8.src.rpm  
>> Build Date  : Mon 29 Aug 2022 05:21:41 PM UTC  
>> Build Host  : server  
>> Relocations : (not relocatable)  
>> Summary     : bash script  
>> Description :  
>> Create raid in via Vagrantfile in virtualbox machine  
