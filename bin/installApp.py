# script to install a EAR or WAR in WebSphere Application Server
#
 
cellName = '127Node01Cell'
nodeName = '127Node01'
serverName = 'server1'
 
filePath1 = os.environ["OPENSHIFT_REPO_DIR"] + "deployments/ROOT.war"
contextRoot = "/"
     
#Get the name of the WAR file:
strAppToInstall = filePath1[filePath1.rfind("/")+1:len(filePath1)];
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
        AdminApp.uninstall(appToUninstall)
        AdminConfig.save();
     
#Install the app
print "Installing App: ", strAppToInstall
AdminApp.install(filePath1, "-contextroot /"+contextRoot+" -defaultbinding.virtual.host default_host -usedefaultbindings");   
AdminConfig.save();   
     
#Start the app   
apps = AdminApp.list().split("\n");   
theApp = ""   
for iApp in apps:
    if str(iApp).find(strAppToInstall) >= 0:
         theApp = iApp;

print "Starting App: ", theApp
appManager = AdminControl.queryNames('cell='+cellName+',node='+nodeName+',type=ApplicationManager,process='+serverName+',*')
AdminControl.invoke(appManager, 'startApplication', theApp)
 print "Application installed and started successfuly!"