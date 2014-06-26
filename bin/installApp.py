# script to install a EAR or WAR in WebSphere Application Server
#
import os;
 
cellName = '127Node01Cell'
nodeName = '127Node01'
serverName = 'server1'
strAppToInstall = "ROOT.war"
 
filePath1 = os.environ["OPENSHIFT_REPO_DIR"] + "deployments/" + strAppToInstall
contextRoot = ""
     
print "Installing ", strAppToInstall, " from ", filePath1;
     
#Uninstall the app if already deployed.
appToUninstall = ""
appsBefore = AdminApp.list().split("\n");
for iApp in appsBefore:   
    if str(iApp).find(strAppToInstall) >= 0:   
            appToUninstall = iApp;

if appToUninstall:
    print "Uninstalling app: ", appToUninstall
    appToUninstall = str(appToUninstall).strip();
    AdminApp.uninstall(appToUninstall);
    AdminConfig.save();
     
#Install the app
print "Installing App: ", strAppToInstall
AdminApp.install(filePath1, "-usedefaultbindings");   
#AdminApp.install(filePath1, "-contextroot /"+contextRoot+" -defaultbinding.virtual.host default_host -usedefaultbindings");   
print "Application installed successfully"
AdminConfig.save();