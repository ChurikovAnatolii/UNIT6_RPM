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

>  rpm -qi raid_create-1.0-1.el8.noarch.rpm **- Посмотрим информацию о пакете**    
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

### 3. создать свой репо и разместить там свой RPM;
реализовать это все либо в вагранте, либо развернуть у себя через nginx и дать ссылку на репо.  

***- Создадим свой репо в Vagrant, скопируем в него свой rpm, проверим установку, удаление***

> mkdir /mnt/repo  
> cp ~/rpmbuild/RPMS/noarch/raid_create-1.0-1.el8.noarch.rpm /mnt/repo  
> cd mnt/repo/  

> createrepo .  
>> Directory walk started  
>> Directory walk done - 1 packages  
>> Temporary output repo path: ./.repodata/  
>> Preparing sqlite DBs  
>> Pool started (with 5 workers)  
>> Pool finished  

>ll
>> -rw-r--r--. 1 root root 7040 Aug 31 08:13 raid_create-1.0-1.el8.noarch.rpm  
>> drwxr-xr-x. 2 root root 4096 Aug 31 08:15 repodata  

> nano local.repo **- Создадим [файл](https://github.com/ChurikovAnatolii/UNIT6_RPM/blob/main/local.repo) со своим репо**  

> yum repolist **-Проверим, что он в списке репо**
>> almalinux-ha.repo                almalinux-powertools.repo        almalinux-rt.repo  
>> almalinux-nfv.repo               almalinux.repo                   **local.repo**  
>> almalinux-plus.repo              almalinux-resilientstorage.repo    

***- Проверим, что YUM находит наш RPM и может его установить и удалить**  
> yum search raid_create
>> Last metadata expiration check: 0:12:25 ago on Wed Aug 31 08:23:30 2022.  
>> ================================= Name Exactly Matched: raid_create =================================  
>> raid_create.noarch : bash script  

> yum install -y raid_create  
>> Last metadata expiration check: 0:13:37 ago on Wed Aug 31 08:23:30 2022.  
>> Dependencies resolved.  
>> =====================================================================================================  
>> Package                   Architecture         Version                    Repository           Size  
>> =====================================================================================================  
>> Installing:  
>>  raid_create               noarch               1.0-1.el8                  local               6.9 k  
>>  
>> Transaction Summary  
>> =====================================================================================================  
>> Install  1 Package  
>>
>> Total size: 6.9 k  
>> Installed size: 640  
>> Downloading Packages:  
>> Running transaction check  
>> Transaction check succeeded.  
>> Running transaction test  
>> Transaction test succeeded.  
>> Running transaction  
>>  Preparing        :                                                                             1/1   
>>  Installing       : raid_create-1.0-1.el8.noarch                                                1/1   
>>  Verifying        : raid_create-1.0-1.el8.noarch                                                1/1   
>>
>> Installed:  
>>  raid_create-1.0-1.el8.noarch                                                                         
>>
>> Complete!  






