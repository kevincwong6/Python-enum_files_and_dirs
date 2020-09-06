'''
    A Python script to enumerate all files and/or folder based on user's inputs
'''
import os
import sys

FILE_ONLY           = 1
DIRECTORY_ONLY      = 2
BOTH_FILE_DIRECTORY = 3

def validate_num(obj, err_obj_msg, default_value):
    '''
        validate the string object to ensure it is numeric.
        then convert to a number, otherwise exit out
    '''
    if len(obj) == 0:
        return default_value

    if obj.isnumeric() is False:
        print("\n\nInvalid " + err_obj_msg + "!!!\n\n")
        sys.exit(1)

    return int(obj)

### -------------------------- move_file_into_folder ---------------------------
def move_file_into_folder(obj):
    '''create a folder name same as the file and move the file inside'''
    filename = obj.split(os.path.sep)[-1]
    temp_folder = obj + "-temp"
    os.mkdir(temp_folder) ### create a temp folder
    new_file_name = temp_folder + os.path.sep + filename

    os.rename(obj, new_file_name) ### move the file inside the temp folder
    os.rename(temp_folder, obj) ### then restore the directory name

### ----------------------------- num_file_and_dirs ----------------------------
def num_file_and_dirs():
    '''the main method to enumerate all files/folders'''
    print('Welcome to Python NumFilesAndDirs Utility\n')
    print('This utility will enumerate all files and/or directories\n')

    ### create folder if file?
    create_folder_flag = True

    ### get the working FOLDER path
    print('Please enter the path name : .' + os.path.sep + ' ? ', end='')
    path = input()
    if len(path) == 0:
        path = os.getcwd()
    if os.path.isdir(path) is False:
        print("\n\nInvalid path name!!!\n\n")
        sys.exit(1)

    ### get the starting sequence number
    print("Please enter the starting squence : ", end="1 ? ")
    star_seq_num = validate_num(input(), "Invalid starting sequence number", 1)

    ### for file, dirtory or both
    print("1) File only, 2) Directory, 3) Both file & direcotry : ", end="1 ? ")
    option = validate_num(input(), "Invalid option", FILE_ONLY)

    if DIRECTORY_ONLY == option:
        create_folder_flag = False
    else:
        print("Create folder if file : (y/n) ", end="y ? ")
        create_folder_input = input()
        if create_folder_input.upper() == 'N':
            create_folder_flag = False

    arr=os.listdir(path)
    for obj in arr:
        # apply the following if statement if we want to enumerate certain file extension
        # if obj.endswith('.pdf'):
        #
        oldname = path + os.path.sep + obj
        if os.path.isdir(oldname):
            if FILE_ONLY == option:
                continue
        else: ### must be a file
            if DIRECTORY_ONLY == option:
                continue
            if create_folder_flag:
                move_file_into_folder(oldname)

        print(oldname)
        newname = path + os.path.sep + str(star_seq_num) + " - "+obj
        os.rename(oldname, newname)
        print(newname)
        star_seq_num += 1

num_file_and_dirs()
sys.exit(0)
