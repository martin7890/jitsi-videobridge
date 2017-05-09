#! /bin/bash

## @Author : Martin Sebastian ##

# Rum mvn command for creating zip file.
mvn clean install -f ../pom.xml -Dmaven.test.skip=true

# Unzip the created zip.
unzip ../target/jitsi-videobridge-linux-x64*.zip

# Cleaning up the existing code copy.
rm -rf centos/jitsi_videobridge_centos/usr/share/jitsi-videobridge/*

# Copying new code from new zip.
cp -r jitsi-videobridge-linux-x64*/* centos/jitsi_videobridge_centos/usr/share/jitsi-videobridge/.

# Creating tar file for RPM creation.
cd centos/
rm -rf jitsi_videobridge_centos.tar.gz
tar -cvzf jitsi_videobridge_centos.tar.gz jitsi_videobridge_centos
cd ../

# Is rpm-build is installed ?
# If no - Install it.
if [ "rpm -q rpm-build | wc -l" = 0 ]; then
    yum -y install rpm-build
fi

DIR=`pwd`

# Is the rpmbuild directory structure present ?
# If no - Create the directory structure.
if [ ! -d "$DIR/rpmbuild/" ]; then
    mkdir $DIR/rpmbuild/
    mkdir $DIR/rpmbuild/SOURCES/
    mkdir $DIR/rpmbuild/SPECS
else
    if [ ! -d "$DIR/rpmbuild/SOURCES/" ]; then
         mkdir $DIR/rpmbuild/SOURCES/
    fi
    if [ ! -d "$DIR/rpmbuild/SPECS/" ]; then
         mkdir $DIR/rpmbuild/SPECS/
    fi
fi

# Cleaning the sources and specs before copying new ones.
rm -rf $DIR/rpmbuild/SOURCES/*
rm -rf $DIR/rpmbuild/SPECS/*
cp centos/jitsi_videobridge_centos.tar.gz $DIR/rpmbuild/SOURCES/.
cp centos/RPM_SPEC/jitsi_videobridge_centos_install.spec $DIR/rpmbuild/SPECS/.

# Creating RPM.
rpmbuild --define "_topdir $DIR/rpmbuild" -ba $DIR/rpmbuild/SPECS/jitsi_videobridge_centos_install.spec

# Moving the created RPM to the project folder.
mv $DIR/rpmbuild/RPMS/x86_64/jitsi_videobridge*.rpm ../.

## Cleanup
rm -rf $DIR/rpmbuild/SOURCES/*
rm -rf $DIR/rpmbuild/SPECS/*
rm -rf $DIR/rpmbuild/RPMS/*
rm -rf centos/jitsi_videobridge_centos/usr/share/jitsi-videobridge/*
rm -rf jitsi-videobridge-linux-x64*/
rm -rf centos/jitsi_videobridge_centos.tar.gz
