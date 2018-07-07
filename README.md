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
    #### install python 3.6
    https://www.rosehosting.com/blog/how-to-install-python-3-6-4-on-centos-7/
    ```
    sudo yum groupinstall -y "Development Tools"
    sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
    sudo yum update
    sudo yum install -y python36u python36u-libs python36u-devel python36u-pip
    python3.6 -V
    ```

    #### install java
    https://tecadmin.net/install-java-8-on-centos-rhel-and-fedora/
    ```
    cd /opt/
    wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.tar.gz" tar xzf jdk-8u171-linux-x64.tar.gz
    cd /opt/jdk1.8.0_171/
    alternatives --install /usr/bin/java java /opt/jdk1.8.0_171/bin/java 2
    alternatives --config java
    alternatives --install /usr/bin/jar jar /opt/jdk1.8.0_171/bin/jar 2
    alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_171/bin/javac 2
    alternatives --set jar /opt/jdk1.8.0_171/bin/jar
    alternatives --set javac /opt/jdk1.8.0_171/bin/javac
    java -version
    export JAVA_HOME=/opt/jdk1.8.0_171
    export JRE_HOME=/opt/jdk1.8.0_171/jre
    export PATH=$PATH:/opt/jdk1.8.0_171/bin:/opt/jdk1.8.0_171/jre/bin
    ```
    #### instal libs
    ```
    sudo yum python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 virtualenv libsox-fmt-mp3 sox libjpeg-dev swig
    https://centos.pkgs.org/7/forensics-x86_64/antiword-0.37-9.el7.x86_64.rpm.html
    wget https://forensics.cert.org/cert-forensics-tools-release-el7.rpm
    rpm -Uvh cert-forensics-tools-release*rpm
    yum --enablerepo=forensics install antiword
    sudo yum install pulseaudio-libs-devel
    ```

    ### install packages
    pip install -r requirements.txt
    python -m spacy download en_core_web_lg
