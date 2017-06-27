import os

def rename_files():
    # 1) get file names from a folder
    file_list = os.listdir(r'prank/')
    cwd = os.getcwd()
    os.chdir(r'prank/')
    # 2) rename the files
    for file_name in file_list:
        print('Old name:' + file_name)
        print('New name:' + file_name.translate(None, '0123456789'))
        os.rename(file_name, file_name.translate(None, '0123456789'))
    os.chdir(cwd)
    
rename_files()
