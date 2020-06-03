# Import necessary libraries
import os
import pickle

# Fold all functions: Ctrl + Alt + Shift + [
def test_print(x,y):
    number = x * y
    print(f'{x} * {y} = {number}')


# ========================
#  Compartment Functions
# ========================

def save_cmt(*args, folder_path = './skpk_saved_cmts'):
    '''
    Saves the compartment instances as pickle files inside folder
    '''
    # If directory does not exist, create new folder and then access that folder
    if not os.path.exists(folder_path):
        os.makedirs(folder_path) # Create new directory
        print(f'Created new folder ({folder_path}) to store the saved files')
        os.chdir(folder_path) # Change directory to the folder path
    else:
        print(f'Saving in existing folder: {folder_path}')
        os.chdir(folder_path) # Change directory to the folder path

    # Create an individual pickle file for each compartment instance
    for arg in args:
        pickle_filename = f'{arg.cmt_name}' + '.pkl'
        with open(pickle_filename, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(arg, output, -1)
    os.chdir(os.path.dirname(os.getcwd())) # Return console to parent directory



def __check_path_exist(folder_path):
    if not os.path.exists(folder_path):
        raise Exception(f'Folder path {folder_path} does not exist')
    else:
        os.chdir(folder_path)  # Change directory if folder exists



def list_cmt(folder_path = './skpk_saved_cmts'):
    '''
    Lists the saved compartmente instances (pickle files) inside the specified folder path
    '''
    __check_path_exist(folder_path) # Check if folder path exists
    n_count = 1 # Counter for number of compartments in the folder

    print('\n=== List of saved instances ===')
    for file in os.listdir('.'): # List pkl files in current directory
        if file.endswith('.pkl'):
            print(n_count, str(' - '),file)
            n_count +=1
    os.chdir(os.path.dirname(os.getcwd())) # Return console to parent directory



def load_cmt(*filenames, folder_path = './skpk_saved_cmts'):
    '''
    Load saved compartment instance(s) from an existing folder path or library
    '''
    __check_path_exist(folder_path) # Check if folder path exists

    list_of_cmts = [] # Create empty list to store cmt objects

    for filename in filenames:
        pickle_filename = filename + '.pkl' # Convert to pickle file string
        if not os.path.exists(pickle_filename): # Check if filename exists
            raise Exception(f'{pickle_filename} does not exist')
            os.chdir(os.path.dirname(os.getcwd()))  # Return console to parent directory
        else:
            cmt_object = pickle.load(open(pickle_filename, "rb", -1)) # Load pickle
            print(f'Compartment {pickle_filename} loaded')
            list_of_cmts.append(cmt_object)

    os.chdir(os.path.dirname(os.getcwd())) # Return console to parent directory
    if len(list_of_cmts) == 0:
        raise Exception('No compartments loaded. Please check argument input')
    if len(list_of_cmts) == 1:
        return list_of_cmts[0] # Directly unpack single-element list into a variable
    else:
        return list_of_cmts # Returns list of compartment instances



def load_all_cmt(folder_path = './skpk_saved_cmts'):
    '''
    Load all saved compartment instances (pickle files) in specified folder path
    '''
    __check_path_exist(folder_path) # Check if folder path exists

    list_of_cmts = [] # Create empty list to store cmt objects

    for file in os.listdir('.'):
        if file.endswith('.pkl'):
            print(f'Loaded compartment {file}')
            cmt_object = pickle.load(open(file, "rb", -1))
            list_of_cmts.append(cmt_object)

    os.chdir(os.path.dirname(os.getcwd())) # Return console to parent directory

    if len(list_of_cmts) == 0:
        print('No pickle files found in folder')
    else:
        return list_of_cmts


# ========================
#     Model Functions
# ========================

def save_model():
    pass



def load_model():
    pass
