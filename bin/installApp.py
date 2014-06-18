#install ROOT.war application
import os;

deployWAR=os.environ["OPENSHIFT_REPO_DIR"] + "deployments/ROOT.war"
print 'Installing ' + deployWAR 
appName="oserootapp"
attr="-appname " + appName + " "
AdminApp.install(deployWAR, "["+attr+"]" );
AdminConfig.save();
print 'Done'