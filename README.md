# resume_script

Parse:
    name (x)
    email (x)
    phone (x)
    location (x)
    language (x)
    skills (x)
    experience (x)

## Install

### install dependencies for Ubuntu
```
sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 virtualenv libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev
```

### install dependencies for centos

#### install apache
[Source!](https://www.liquidweb.com/kb/how-to-install-apache-on-centos-7/)

```
sudo yum install httpd
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --permanent --add-port=443/tcp
sudo firewall-cmd --reload
sudo systemctl start httpd
```

#### install python 3.6
[Source!](https://www.rosehosting.com/blog/how-to-install-python-3-6-4-on-centos-7/)
    
```
sudo yum groupinstall -y "Development Tools"
sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
sudo yum update
sudo yum install -y python36u python36u-libs python36u-devel python36u-pip
python3.6 -V
```

#### install java
[Source!](https://tecadmin.net/install-java-8-on-centos-rhel-and-fedora/)

```
sudo yum install wget
cd /opt/
sudo wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.tar.gz"
sudo tar xzf jdk-8u171-linux-x64.tar.gz
cd /opt/jdk1.8.0_171/
sudo alternatives --install /usr/bin/java java /opt/jdk1.8.0_171/bin/java 2
sudo alternatives --config java
sudo alternatives --install /usr/bin/jar jar /opt/jdk1.8.0_171/bin/jar 2
sudo alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_171/bin/javac 2
sudo alternatives --set jar /opt/jdk1.8.0_171/bin/jar
sudo alternatives --set javac /opt/jdk1.8.0_171/bin/javac
java -version
export JAVA_HOME=/opt/jdk1.8.0_171
export JRE_HOME=/opt/jdk1.8.0_171/jre
export PATH=$PATH:/opt/jdk1.8.0_171/bin:/opt/jdk1.8.0_171/jre/bin
```

#### instal libs

```
sudo yum install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 virtualenv libsox-fmt-mp3 sox libjpeg-dev swig
sudo wget https://forensics.cert.org/cert-forensics-tools-release-el7.rpm
sudo rpm -Uvh cert-forensics-tools-release*rpm
sudo yum --enablerepo=forensics install antiword
sudo yum install pulseaudio-libs-devel
```

#### permitions
```
sudo chown -R apache:apache NombreCarpeta
sudo chmod 777 NombreCarpeta
```

#### install packages for python script
```
sudo git clone https://github.com/Carlo1911/resume_script.git
cd resume_script
sudo pip3.6 install -r requirements.txt
python3.6 -m spacy download en_core_web_lg
```

#### install java script
```
git clone https://github.com/antonydeepak/ResumeParser.git
cd ResumeParser/ResumeTransducer
export GATE_HOME="..\GATEFiles"
```