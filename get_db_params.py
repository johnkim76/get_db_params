#!/usr/bin/env python
import os

#postgresql-demo-apb    rhscl-postgresql-apb
#POSTGRES_USER          POSTGRESQL_USER
#POSTGRES_PASSWORD      POSTGRESQL_PASSWORD
#POSTGRES_HOST          POSTGRESQL_HOST
#POSTGRES_DB            POSTGRESQL_DATABASE

def get_db_user():
    ret = os.environ.get('POSTGRES_USER')
    if ret == None:
        ret = os.environ.get('POSTGRESQL_USER')
    return ret

def get_db_password():
    ret = os.environ.get('POSTGRES_PASSWORD')
    if ret == None:
        ret = os.environ.get('POSTGRESQL_PASSWORD')
    return ret

def get_db_host():
    ret = os.environ.get('POSTGRES_HOST')
    if ret == None:
        ret = os.environ.get('POSTGRESQL_HOST')
    return ret

def get_db_name():
    ret = os.environ.get('POSTGRES_DB')
    if ret == None:
        ret = os.environ.get('POSTGRESQL_DATABASE')
    return ret

get_db_param = {
    'user' : get_db_user,
    'password' : get_db_password,
    'host' : get_db_host,
    'name' : get_db_name,
}

if __name__ == '__main__':
    ret = get_db_param['user']()
    print "\n\n USERNAME parm is : %s" % ret

    ret = get_db_param['password']()
    print "\n PASSWORD parm is : %s" % ret

    ret = get_db_param['host']()
    print "\n HOST parm is : %s" % ret

    ret = get_db_param['name']()
    print "\n DB NAME parm is : %s\n" % ret
