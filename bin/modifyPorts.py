# setup WAS ND ports and host to bind to gear IP
import os;

def modifyServerPort(serverName, endPointName, hostName):
    print 'About to change server %s endpoint %s to new host %s' % (serverName, endPointName, hostName)
    opts = '[-endPointName %s -host %s -modifyShared true]' % (endPointName, hostName)
    AdminTask.modifyServerPort(serverName, opts)

node = AdminConfig.getid('/Node:127Node01/')
serverEntries = AdminConfig.list('ServerEntry', node).split(java.lang.System.getProperty('line.separator'))
serverName = "server1"
ip = os.environ["OPENSHIFT_WASND_IP"]
#ip = "127.1.246.1"

print 'Setting endpoints host name'

for serverEntry in serverEntries:
  sName = AdminConfig.showAttribute(serverEntry, "serverName")
  if sName == serverName:
     sepString = AdminConfig.showAttribute(serverEntry, "specialEndpoints")
     sepList = sepString[1:len(sepString)-1].split(" ")
     for specialEndPoint in sepList:
        endPointName = AdminConfig.showAttribute(specialEndPoint, "endPointName")
        modifyServerPort(serverName, endPointName, ip)

print 'Done'

#Servers > Server Types > WebSphere application servers > server1 > Container Settings > Container services > ORB Service. Then in the Additional Properties section, click Custom properties 
#set variables
#com.ibm.CORBA.LocalHost=ip
#com.ibm.ws.orb.transport.useMultiHome=false

print 'Setting ORB properties'

for orb in AdminConfig.list('ObjectRequestBroker').splitlines():
   AdminConfig.modify(orb, [ [ 'properties', [ [ ['name', 'com.ibm.ws.orb.transport.useMultiHome'], ['value', 'false'] ] ] ] ])
   AdminConfig.create('Property', orb, [ ['name', 'com.ibm.CORBA.LocalHost'], ['value', ip] ])

print 'Done'

#Servers > Application servers > server1, and then, in the Server Infrastructure section, click Java and process management > Process definition > Java virtual machine > Custom Properties
#com.ibm.websphere.network.useMultiHome=false
#java.net.preferIPv4Stack=true for using IPv4
#java.net.preferIPv6Addresses=true for using IPv6

print 'Setting JVM properties'

for jvm in AdminConfig.list('JavaVirtualMachine').splitlines():
   AdminConfig.create('Property', jvm, [ ['name', 'java.net.preferIPv4Stack'], ['value', 'true'] ])
   AdminConfig.create('Property', jvm, [ ['name', 'com.ibm.websphere.network.useMultiHome'], ['value', 'false'] ])

print 'Done'

AdminConfig.save()