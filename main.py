from aws_ops import aws_operations
from azure_ops import azure_operations


def dosomething(obj):
    obj.put()
    obj.get()
    obj.delete()
    print obj.getProvider()
    print obj.getProfile()
    print obj.getFilename()


obj = aws_operations("111", "/etc/passwd")
dosomething(obj)
obj = azure_operations("222", "/etc/shadows")
dosomething(obj)