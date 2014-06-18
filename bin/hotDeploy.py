# enable apps hot deployment in WAS ND
import os;

print 'Enabling hot deployment dir'
dir = os.environ["OPENSHIFT_REPO_DIR"] + "deployments/"
c1 = AdminConfig.getid('/Cell:127Node01Cell')
md = AdminConfig.showAttribute(c1, "monitoredDirectoryDeployment")
AdminConfig.modify(md, [ ['enabled', "true"], ['monitoredDirectory', dir] ])
AdminConfig.save()
print 'Done'