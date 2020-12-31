from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title':'test.txt'})
file1.setContentString("this is for test")

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))

file1.upload()