Summary: Jitsi Videobridge is an XMPP server component that allows for multiuser video communication
Name: jitsi_videobridge_centos7.1
Version: 2.0.8
Release: 0
Source: jitsi_videobridge_centos.tar.gz
License: GPL
Group: Development/Tools
%description
Jitsi Videobridge does not mix the video channels into a composite video stream, but only relays the received video channels to all call participant.
%prep
# xrtc smpp prosody patch install
rm -rf $RPM_BUILD_DIR/jitsi_videobridge_centos
zcat $RPM_SOURCE_DIR/jitsi_videobridge_centos.tar.gz | tar -xvf -
%build
%install
mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/etc/jitsi
mkdir -p $RPM_BUILD_ROOT/etc/jitsi/videobridge
mkdir -p $RPM_BUILD_ROOT/usr/share
mkdir -p $RPM_BUILD_ROOT/usr/share/jitsi-videobridge
mkdir -p $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/.sip-communicator
mkdir -p $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib
mkdir -p $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/native
mkdir -p $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/native/linux-64
#/etc/init.d
install -m 755 jitsi_videobridge_centos/etc/init.d/jitsi-videobridge $RPM_BUILD_ROOT/etc/init.d/
#/etc/jitsi/videobridge
install -m 755 jitsi_videobridge_centos/etc/jitsi/videobridge/config.default $RPM_BUILD_ROOT/etc/jitsi/videobridge/
#/usr/share/jitsi-videobridge
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/jitsi-videobridge.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/jvb.sh $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/
#/usr/share/jitsi-videobridge/.sip-communicator
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/.sip-communicator/sip-communicator.properties $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/.sip-communicator/
#/usr/share/jitsi-videobridge/lib
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/agafua-syslog.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/async-http-client.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/bcprov-jdk15on.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/bccontrib.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/bcpkix-jdk15on.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/callstats-java-sdk.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/commons-codec.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/commons-lang3.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/commons-logging.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/commons-lang.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/concurrentlinkedhashmap-lru.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/core.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/dnsjava.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/dom4j.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/fmj.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/gson.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/guava.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/httpasyncclient.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/httpclient.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/httpcore.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/httpcore-nio.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/ice4j.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jain-sip-ri-ossonly.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/java-sdp-nist-bridge.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/javax.servlet-api.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jcip-annotations.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jetty-client.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jetty-http.jar	 $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jetty-io.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jetty-proxy.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jetty-rewrite.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jetty-security.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jetty-server.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jetty-servlet.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jetty-util.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jetty-webapp.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jetty-xml.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jicoco.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-android-osgi.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-configuration.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-dnsservice.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-fileaccess.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
#install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-lgpl-dependencies.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-netaddr.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-packetlogging.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-protocol-jabber.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-protocol.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-protocol-media.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-resourcemanager.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-ui-service.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jitsi-util.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jna.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jnsapi.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/json-simple.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/libidn.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/libjitsi.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/log4j-api.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/log4j-core.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/log4j.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/logging.properties $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/netty.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/orange-extensions.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/org.apache.felix.framework.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/org.apache.felix.main.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/org.osgi.core.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/sdes4j.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/sdp-api.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/sigar.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/slf4j-api.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/slf4j-jdk14.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/slf4j-simple.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/smack.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/smackx.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/tinder.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/videobridge.rc $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/weupnp.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/xml-apis.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/xmlpull.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/xpp3.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/zrtp4j-light.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
#install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/influxdb-java.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/jzlib.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
#install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/okhttp.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
#install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/okio.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
#install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/retrofit.jar $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/
#/usr/share/jitsi-videobridge/lib/native/linux-64
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/native/linux-64/libhwaddressretriever.so $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/native/linux-64/
install -m 755 jitsi_videobridge_centos/usr/share/jitsi-videobridge/lib/native/linux-64/libsigar-amd64-linux.so $RPM_BUILD_ROOT/usr/share/jitsi-videobridge/lib/native/linux-64/
%files
#/etc/init.d
/etc/init.d/jitsi-videobridge
#/etc/jitsi/videobridge
/etc/jitsi/videobridge/config.default
#/usr/share/jitsi-videobridge/.sip-communicator
/usr/share/jitsi-videobridge/.sip-communicator/sip-communicator.properties
#/usr/share/jitsi-videobridge
/usr/share/jitsi-videobridge/jitsi-videobridge.jar
/usr/share/jitsi-videobridge/jvb.sh
#/usr/share/jitsi-videobridge/lib
/usr/share/jitsi-videobridge/lib/agafua-syslog.jar
/usr/share/jitsi-videobridge/lib/async-http-client.jar
/usr/share/jitsi-videobridge/lib/bccontrib.jar
/usr/share/jitsi-videobridge/lib/bcpkix-jdk15on.jar
/usr/share/jitsi-videobridge/lib/bcprov-jdk15on.jar
/usr/share/jitsi-videobridge/lib/callstats-java-sdk.jar
/usr/share/jitsi-videobridge/lib/commons-codec.jar
/usr/share/jitsi-videobridge/lib/commons-lang3.jar
/usr/share/jitsi-videobridge/lib/commons-lang.jar
/usr/share/jitsi-videobridge/lib/commons-logging.jar
/usr/share/jitsi-videobridge/lib/concurrentlinkedhashmap-lru.jar
/usr/share/jitsi-videobridge/lib/core.jar
/usr/share/jitsi-videobridge/lib/dnsjava.jar
/usr/share/jitsi-videobridge/lib/dom4j.jar
/usr/share/jitsi-videobridge/lib/fmj.jar
/usr/share/jitsi-videobridge/lib/gson.jar
/usr/share/jitsi-videobridge/lib/guava.jar
/usr/share/jitsi-videobridge/lib/httpasyncclient.jar
/usr/share/jitsi-videobridge/lib/httpclient.jar
/usr/share/jitsi-videobridge/lib/httpcore.jar
/usr/share/jitsi-videobridge/lib/httpcore-nio.jar
/usr/share/jitsi-videobridge/lib/ice4j.jar
/usr/share/jitsi-videobridge/lib/jain-sip-ri-ossonly.jar
/usr/share/jitsi-videobridge/lib/java-sdp-nist-bridge.jar
/usr/share/jitsi-videobridge/lib/javax.servlet-api.jar
/usr/share/jitsi-videobridge/lib/jcip-annotations.jar
/usr/share/jitsi-videobridge/lib/jetty-client.jar
/usr/share/jitsi-videobridge/lib/jetty-http.jar
/usr/share/jitsi-videobridge/lib/jetty-io.jar
/usr/share/jitsi-videobridge/lib/jetty-proxy.jar
/usr/share/jitsi-videobridge/lib/jetty-rewrite.jar
/usr/share/jitsi-videobridge/lib/jetty-security.jar
/usr/share/jitsi-videobridge/lib/jetty-server.jar
/usr/share/jitsi-videobridge/lib/jetty-servlet.jar
/usr/share/jitsi-videobridge/lib/jetty-util.jar
/usr/share/jitsi-videobridge/lib/jetty-webapp.jar
/usr/share/jitsi-videobridge/lib/jetty-xml.jar
/usr/share/jitsi-videobridge/lib/jicoco.jar
/usr/share/jitsi-videobridge/lib/jitsi-android-osgi.jar
/usr/share/jitsi-videobridge/lib/jitsi-configuration.jar
/usr/share/jitsi-videobridge/lib/jitsi-dnsservice.jar
/usr/share/jitsi-videobridge/lib/jitsi-fileaccess.jar
#/usr/share/jitsi-videobridge/lib/jitsi-lgpl-dependencies.jar
/usr/share/jitsi-videobridge/lib/jitsi-netaddr.jar
/usr/share/jitsi-videobridge/lib/jitsi-packetlogging.jar
/usr/share/jitsi-videobridge/lib/jitsi-protocol-jabber.jar
/usr/share/jitsi-videobridge/lib/jitsi-protocol.jar
/usr/share/jitsi-videobridge/lib/jitsi-protocol-media.jar
/usr/share/jitsi-videobridge/lib/jitsi-resourcemanager.jar
/usr/share/jitsi-videobridge/lib/jitsi-ui-service.jar
/usr/share/jitsi-videobridge/lib/jitsi-util.jar
/usr/share/jitsi-videobridge/lib/jna.jar
/usr/share/jitsi-videobridge/lib/jnsapi.jar
/usr/share/jitsi-videobridge/lib/json-simple.jar
/usr/share/jitsi-videobridge/lib/libidn.jar
/usr/share/jitsi-videobridge/lib/libjitsi.jar
/usr/share/jitsi-videobridge/lib/log4j-api.jar
/usr/share/jitsi-videobridge/lib/log4j-core.jar
/usr/share/jitsi-videobridge/lib/log4j.jar
/usr/share/jitsi-videobridge/lib/logging.properties
/usr/share/jitsi-videobridge/lib/native
/usr/share/jitsi-videobridge/lib/netty.jar
/usr/share/jitsi-videobridge/lib/orange-extensions.jar
/usr/share/jitsi-videobridge/lib/org.apache.felix.framework.jar
/usr/share/jitsi-videobridge/lib/org.apache.felix.main.jar
/usr/share/jitsi-videobridge/lib/org.osgi.core.jar
/usr/share/jitsi-videobridge/lib/sdes4j.jar
/usr/share/jitsi-videobridge/lib/sdp-api.jar
/usr/share/jitsi-videobridge/lib/sigar.jar
/usr/share/jitsi-videobridge/lib/slf4j-api.jar
/usr/share/jitsi-videobridge/lib/slf4j-jdk14.jar
/usr/share/jitsi-videobridge/lib/smack.jar
/usr/share/jitsi-videobridge/lib/smackx.jar
/usr/share/jitsi-videobridge/lib/tinder.jar
/usr/share/jitsi-videobridge/lib/videobridge.rc
/usr/share/jitsi-videobridge/lib/weupnp.jar
/usr/share/jitsi-videobridge/lib/xml-apis.jar
/usr/share/jitsi-videobridge/lib/xpp3.jar
/usr/share/jitsi-videobridge/lib/zrtp4j-light.jar
/usr/share/jitsi-videobridge/lib/slf4j-simple.jar
/usr/share/jitsi-videobridge/lib/xmlpull.jar
#/usr/share/jitsi-videobridge/lib/influxdb-java.jar
/usr/share/jitsi-videobridge/lib/jzlib.jar
#/usr/share/jitsi-videobridge/lib/okhttp.jar
#/usr/share/jitsi-videobridge/lib/okio.jar
#/usr/share/jitsi-videobridge/lib/retrofit.jar
#/usr/share/jitsi-videobridge/lib/native/linux-64
/usr/share/jitsi-videobridge/lib/native/linux-64/libhwaddressretriever.so
/usr/share/jitsi-videobridge/lib/native/linux-64/libsigar-amd64-linux.so
%pre
if id -u "jvb" >/dev/null 2>&1; then
	userdel jvb
	rm -rf /usr/share/jitsi-videobridge
	echo "account \"jvb\" exists. Deleting account."
fi
if grep -q "^${jitsi}:" /etc/group; then
	echo "group \"jitsi\" exists"
else
	groupadd jitsi
fi
mkdir -p /usr/share/jitsi-videobridge
useradd -c "jvb ,,," -m -g jitsi -d /usr/share/jitsi-videobridge jvb
chown jvb:jitsi /usr/share/jitsi-videobridge
if [ ! -d "/var/log/jitsi" ]; then
	mkdir -p /var/log/jitsi
fi
chown jvb:jitsi /var/log/jitsi
chown jvb:jitsi /var/log/jitsi/jvb*
chmod 775 /var/log/jitsi

%post
#create symbolic links here
if ! [ -L "/usr/share/jitsi-videobridge/lib/native/linux-64/libvpx.so.1" ]; then 
	ln -s /usr/share/jitsi-videobridge/lib/native/linux-64/libvpx.so /usr/share/jitsi-videobridge/lib/native/linux-64/libvpx.so.1
fi
