import shutil
import os
import time

def main():
    # Initializing the count    
    deleted_folders_count = 0
    deleted_files_count = 0
    
    # Specify the path
    path = "/PATH_TO_DELETE"

    # Specify the days
    days = 30

    # Converting days to seconds
    seconds = time.time() - (days * 24 * 60 * 60)

    # Checking whether file exists in the path
    if os.path.exists(path):

        # Itrating over each and every folder and file in the path
        for root_folder, folders, files in os.walk(path):
            
            # Comparing the days
            if seconds >= get_file_or_folder_age(root_folder):

                # Removing the folder
                remove_folder(root_folder)
                deleted_folders_count += 1
                
                # Breaking after removing the root folder
                break
            
            else:

                # Checking folder from the root folder
                for folder in folders:

                    # Folder path
                    folder_path = os.path.join(root_folder, folder)

                    # Comparing with days
                    if seconds >= get_file_or_folder_age(folder_path):

                        # Invoking the remove_folder function
                        remove_folder(folder_path)
                        deleted_folders_count += 1

                # Checking files from the root folder
                for file in files:

                    # Folder path
                    file_path = os.path.join(root_folder, file)

                    # Comparing with days
                    if seconds >= get_file_or_folder_age(file_path):

                        # Invoking the remove_folder function
                        remove_file(file_path)
                        deleted_files_count += 1

                    else:

                        # If path is not a directory
                        # Comparing with the days
                        if seconds >= get_file_or_folder_age(path):

                            # Invoking the file
                            remove_file(path)
                            deleted_files_count +=1

                        else:

                            # If file/folder is not found
                            print(f'"{path}" is not found')
                            deleted_files_count += 1

                            print(f"Total folders delted: {deleted_folders_count}")
                            print(f"Total files delted: {deleted_files_count}")
                    
                def remove_folder(path):

                    # Removing the folder
                    if not shutil.rmtree(path):

                        # Success message
                        print(f"{path} is removed succesfuly")
                    
                    else:

                        # Failure message
                        print("Unable to delete " + path)

                def remove_file(path):

                    # Removing the file
                    if not os.remove(path):
                        
                        # Success message
                        print(f"{path} is removed succesfully")

                    else:

                        # Failure message
                        print("Unable to delete" + path)    

                def get_file_or_folder_age(path):
                    # Getting time of the file/folder in seconds
                    ctime = os.stat(path).st_ctime

                    # Returning the time
                    return ctime

main()