import os;

def variable(varname, vardesc):
    
    varvalue = os.environ[vaname]
  
 	cellName = '127Node01Cell'
 	nodeName = '127Node01'
 	varMapserver = AdminConfig.getid('/Cell:'+ cellName +'/Node:'+ nodeName +'/VariableMap:/')

 	nameattr1 = ['symbolicName', varname]
 	valattr1 = ['value', varvalue]
 	desc1 = ["description", vardesc]
 	attr1 = [nameattr1, valattr1, desc1]
 	attrs1 = [attr1]

 	entries1 = ['entries', attrs1 ]

 	print "creating new variable " + varname

 	AdminConfig.modify(varMapserver, [entries1] )

 	AdminConfig.save()

variable('OPENSHIFT_POSTGRESQL_DB_HOST', 'PostgreSQL host name')
variable('OPENSHIFT_POSTGRESQL_DB_PASSWORD', 'PostgreSQL password')
variable('OPENSHIFT_POSTGRESQL_USERNAME', 'PostgreSQL user name')
variable('OPENSHIFT_POSTGRESQL_DB_PORT', 'PostgreSQL port')
variable('OPENSHIFT_POSTGRESQL_DB_NAME', 'PostgreSQL database name')
