import pymysql

pymysql.install_as_MySQLdb()

class ConfigDEV():
    
    def __init__(self):
        self.SECRET_KEY = 'django-insecure-!z-0bvsonpsy8u_r@bycu^j6-ci_j%@mbp@wz4cbbns4=2))n-'
        self.DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'database-2',
                    'USER' : 'admin',
                    'PASSWORD' : 's.j3033212',
                    'HOST' : 'database-2.csjvf23ojub6.ap-northeast-2.rds.amazonaws.com',
                    'PORT' : '3306',     
                    'OPTIONS': {
                                'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'"
                                },  
                            }
                    }



