#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Uploading Files to Dropbox

import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)

def main():
    access_token = '2c3GooLQSkwAAAAAAAAAAYD-F-JziqmUWaCpwuXmKFkGJfG9pUqL6SbkwklWeb9v'
    transferData = TransferData(access_token)

    file_from = input('Enter Path of File to be uploaded:- ')
    for root,dirs, files in os.walk(".", topdown=False):
        for name in files:
            file_from = os.path.join(root, name)

    file_to = '/Project_101/'  # The full path to upload the file to, including the file name
    fileto = input('Enter The File name to be saved with:- ')
    file_to = os.path.join(str(file_to), str(fileto))
    # API v2
    transferData.upload_file(file_from, file_to)
    print('File Uploaded !!')

main()