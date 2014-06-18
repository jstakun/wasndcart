# enable apps hot deployment in WAS ND
c1 = AdminConfig.getid('/Cell:127Node01Cell')
md = AdminConfig.showAttribute(c1, "monitoredDirectoryDeployment")
AdminConfig.modify(md, [['enabled', "true"]])
AdminConfig.save()
