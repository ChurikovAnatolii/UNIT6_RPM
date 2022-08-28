# UNIT6_RPM
Creating own rpm from python source

### 1. Cоздать свой RPM (можно взять свое приложение, либо собрать к примеру апач с определенными опциями)

***- Запустим [Vagrantfile](https://github.com/ChurikovAnatolii/UNIT6_RPM/blob/main/Vagrantfile), установим rpmdevtools, rpm-build***

> yum install rpmdevtools rpm-build  
> rpmdev-setuptree **- Создадим окружение для сборки пакета**  

***- Скопируем [исходники проекта на python](https://github.com/ChurikovAnatolii/Packet-Tracer) в папку /SOURCE, упакуем файлы в tar.gz***  

> wget https://github.com/ChurikovAnatolii/Packet-Tracer/archive/refs/heads/master.zip  
> unzip master.zip  
> tar -czvf PT.tar.gz  

> tar -tf PT.tar.gz **- Проверим, что все на месте**  
>> ./  
>> ./DLE_RAW_CRC.py  
>> ./main.py  
>> ./README.md  
>> ./tracer.py  
>> ./tracer.ui  
>> ./UDP_socket.py  

> 
