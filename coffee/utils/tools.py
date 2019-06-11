# -*- encoding:utf-8 -*-
from coffee.config import DEBUG

def Debug(self,msg):
    if DEBUG==True:
        print ("[DEBUG]%s" % msg)