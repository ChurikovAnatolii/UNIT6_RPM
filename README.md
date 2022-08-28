# UNIT6_RPM
Creating own rpm from python source

### 1. Cоздать свой RPM (можно взять свое приложение, либо собрать к примеру апач с определенными опциями)

***- Запустим [Vagrantfile](https://github.com/ChurikovAnatolii/UNIT6_RPM/blob/main/Vagrantfile), установим rpmdevtools, rpm-build***

> yum install rpmdevtools rpm-build  
> rpmdev-setuptree **- Создадим окружение для сборки пакета**  

***- Скопируем [bash-script из предыдушего урока ](https://github.com/ChurikovAnatolii/Vagant_soft_RAID/blob/main/raid_add.sh) в папку /SOURCE, упакуем в tar.gz***  

> wget https://github.com/ChurikovAnatolii/Vagant_soft_RAID/archive/refs/heads/main.zip  
> unzip main.zip  
> cp raid_add.sh ~/rpmbuild/SOURCES/  
> tar -czf raid_create-0.0.1.tar.gz raid_add.sh

***- Создадим [spec-файл]() в папке /SPECS, создадим RPM-пакет***  

>

