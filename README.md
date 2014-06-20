Websphere Application Server Network Deployments profiles cartridge.

With this cartridge you could create WAS ND gears in Openshift.

Before you use this cartridge you must install WAS ND binaries at 
WASND_INSTALL_ROOT=/opt/IBM/WebSphere/AppServer 

You need to add Openshift gear users to profilers group and make sure profilers group members
have granted rw permission to WAS_INSTALL_ROOT. For demo purposes you might cosider to execute 
setenforce 0 to avoid SELinux related permission issues.
