WebSphere Application Server Network Deployments profiles cartridge.

Using this cartridge you could create WAS ND gears in OpenShift. Each gear will create its own App Server profile and server instance. 
This cartridge was tested with WAS ND 8.5 however it is very likely it will work with earlier WAS ND versions as well. 

Installation steps:

1. Install WAS ND on OpenShift node at WAS_INSTALL_ROOT = /opt/IBM/WebSphere/AppServer

2. Create group for gear users i.e. profilers

Edit /etc/openshift/node.conf: set GEAR_SUPPLEMENTARY_GROUPS=profilers

3. Grant WAS_INSTALL_ROOT rw privileges to profilers:

chmod -R 771 $WAS_INSTALL_ROOT                   
chown -R root:profilers $WAS_INSTALL_ROOT    

If you want to this privileges might be limited to number of WAS_INSTALL_ROOT subdirectories.

4. Modify SELinux policies to grant WAS_INSTALL_ROOT rw privileges to profilers or simply setenforce 0

If you want to this privileges might be limited to number of WAS_INSTALL_ROOT subdirectories.

5. Download and install cartridge:

oo-admin-cartridge --action install --source /path/to/cartridge/

6. Copy deleteGearProfiles script to from cartridge bin directory to WAS_INSTALL_ROOT/bin and create cron task to schedule it execution (this could be done later and only once per node)

crontab -e

10 */1 * * * /opt/IBM/WebSphere/AppServer/bin/deleteGearProfiles >> /var/log/cron 2>&1 

Enjoy!

Tested cartridge features:

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
 