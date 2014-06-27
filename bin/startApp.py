#Start the app   
import sys

cellName = '127Node01Cell'
nodeName = '127Node01'
serverName = 'server1'
strAppToInstall = "ROOT.war"

apps = AdminApp.list().split("\n");   
theApp = ""   
for iApp in apps:
    if str(iApp).find(strAppToInstall) >= 0:
         theApp = iApp;
         print "Starting App: ", theApp
         try:
         	appManager = AdminControl.queryNames('cell='+cellName+',node='+nodeName+',type=ApplicationManager,process='+serverName+',*')
         	AdminControl.invoke(appManager, 'startApplication', theApp)
         	print "Application started successfully"
         except: 
            print "Application might be running: ", sys.exc_info()