WebSphere Application Server Network Deployments profiles cartridge.

Using this cartridge you could create WAS ND gears in OpenShift. Each gear will create its own App Server profile and server instance. 

Installation steps:

1. Install WAS ND at WAS_INSTALL_ROOT = /opt/IBM/WebSphere/AppServer

This cartridge was tested with WAS ND 8.5 however it is very likely it will work with earlier WAS ND versions as well. 

2. Create group for gear users i.e. profilers

2.1 Edit /etc/openshift/node.conf: 

GEAR_SUPPLEMENTARY_GROUPS=profilers

2.2 Grant WAS_INSTALL_ROOT rw privileges to profilers:

chmod -R 771 $WAS_INSTALL_ROOT                   
chown -R root:profilers $WAS_INSTALL_ROOT    

2.3 Modify SELinux policies to grant WAS_INSTALL_ROOT rw privileges to profilers or setenforce 0

This privileges might be limited to number of WAS_INSTALL_ROOT subdirectories.

3. Download and install cartridge:

oo-admin-cartridge --action install --source /path/to/cartridge/

4. Copy deleteGearProfiles script to from cartridge bin directory to WAS_INSTALL_ROOT/bin and create cron task to schedule it execution (this could be done later and only once per node)

crontab -e

10 */1 * * * /opt/IBM/WebSphere/AppServer/bin/deleteGearProfiles >> /var/log/cron 2>&1 

Enjoy!

This gear features were tested and should work for you:

Template based git repo created during gear install

Default app deployment during gear install

Maven build

Jenkins build

Hot deployment

Auto scaling

Embedded db cartridge

Jython scripting

WAS ND web admin console installed

Port forwarding

Please browse Issues page to see what enhancements are planned and bugs are discovered.
 