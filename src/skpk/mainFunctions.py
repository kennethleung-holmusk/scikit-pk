# ==========================
#  Non-Class Main Functions
# ==========================
# Import necessary dependencies
import os
import pickle
from .compartments import Cmt
from .models import Model

# ========================
#  Compartment Functions
# ========================
def __check_path_exist_before_save(path):
    """Check that there is an existing folder path that matches `path` argument,
    before saving Cmt or Model instances

    If path does not exist, create new folder path and access that folder.

    Parameters
    ----------
    path : pathname
        Name of the path where Cmt or Model instances will be saved and stored.

    """

    if not os.path.exists(path):
        os.makedirs(path) # Create new folder/path
        print(f'Created new folder ({path}) to store saved instances')
        os.chdir(path) # Change path to specified input path
    else:
        print(f'Saved in existing folder: {path}')
        os.chdir(path) # Change path to specified input path


def save(*objects, path = './skpk_saved'):
    """Save Cmt and/or Model instance(s) in the specified `path`.

    If argument `path` is not passed in, the default path './skpk_saved' is used.
    If path './skpk_saved' does not yet exist, then the path will be created

    Parameters
    ----------
    *objects : Cmt class, Model class
         Variable length list of instances of Cmt class or Model class.
    path : pathname
        Name of the path where the saved Cmt/Model instance(s) will be stored.

    Raises
    -------
    ValueError
        If *objects are not of Cmt or Model class

    """
    for object in objects:
        if isinstance(object, (Cmt, Model)) == False:
            raise ValueError('Input arguments must be of Cmt or Model class')

    cwd = os.getcwd() # Save current working directory
    __check_path_exist_before_save(path) # Check that `path` already exists

    for object in objects:
        # For compartment (Cmt) instances
        if isinstance(object, Cmt):
            cmt_pickle_filename = f'cmt_{object.cmt_attr[1]}' + '.pkl'
            # Saving as pickle file, and overwrites any existing file
            with open(cmt_pickle_filename, 'wb') as output:
                pickle.dump(object, output, -1)
        # For Model instances
        else:
            model_pickle_filename = f'model_{object.modelname}' + '.pkl'
            # Saving as pickle file, and overwrites any existing file
            with open(model_pickle_filename, 'wb') as output:
                pickle.dump(object, output, -1)

    # Return console back to original working directory
    os.chdir(cwd)


def __check_path_exist_before_load(path):
    """Check that `path` exists before loading instances from the input `path`.

    Changes working directory to `path` if folder path exists.

    Parameters
    ----------
    path : pathname
        Name of the path where Cmt and/or Model instance(s) will be loaded from.

    Raises
    -------
    Exception
        If argument `path` does not exist.

    """
    if not os.path.exists(path):
        raise Exception(f'Folder path {path} does not exist.')
    else:
        # Change working directory to path if folder path exists
        os.chdir(path)


def list_all(path = './skpk_saved'):
    """Prints a list of all Cmt and Model instance pickle files within the
     input `path` folder.

    Parameters
    ----------
    path : pathname
        Name of folder path where Cmt/Model instance pickle files are to be
        listed from.

    """
    cwd = os.getcwd() # Save current working directory
    __check_path_exist_before_load(path) # Check if folder path exists

    print('\n--- List of saved instances ---')
    n_count = 1 # Counter for number of Cmt/Model instances in the folder
    for file in os.listdir('.'): # List pkl files in current directory
        if file.endswith('.pkl') and (file.startswith('cmt') or \
            file.startswith('model')):
            print(n_count, str(' - '),file)
            n_count +=1
    # Return console back to original working directory
    os.chdir(cwd)


def load_cmt(*filenames, path = './skpk_saved'):
    """Loads Cmt instance(s) by pickle filename from the input `path` folder.

    Parameters
    ----------
    *filenames
        Variable length list of names of Cmt instances (e.g. 'cmt_Free_Plasma').
    path : pathname
        Name of the folder path where Cmt instance(s) will be loaded from.
        If no argument `path` is passed, default path './skpk_saved' will be used

    Returns
    -------
    list
        List of Cmt class instances as objects

    Raises
    -------
    Exception
        If input filename(s) do not match any saved Cmt pickle filenames in path

    """
    cwd = os.getcwd() # Save current working directory
    __check_path_exist_before_load(path) # Check if folder path exists
    list_cmts = [] # Create empty list to store Cmt objects

    for filename in filenames:
        pickle_filename = filename + '.pkl' # Convert to pickle file string
        if not os.path.exists(pickle_filename): # Check if filename exists
            existing_cmts = [file for file in os.listdir('.') if \
                            file.startswith('cmt') and file.endswith('.pkl')]
            os.chdir(cwd) # Return console to original directory
            raise Exception(f"""{pickle_filename} does not exist.
            \nList of existing compartment instances: {existing_cmts}""")
        else:
            cmt_object = pickle.load(open(pickle_filename, "rb", -1)) # Load pickle
            list_cmts.append(cmt_object)

    os.chdir(cwd) # Return console back to original working directory
    if len(list_cmts) == 0:
        raise Exception('No compartment loaded. Please check argument input')
    if len(list_cmts) == 1:
        return list_cmts[0] # Unpack single-element list into a variable
    else:
        return list_cmts


def load_all_cmts(path = './skpk_saved'):
    """Load all saved Cmt instances (pickle files) from input folder path.

    Parameters
    ----------
    path : pathname
        Name of the path here Cmt instances (pickle files) will be loaded from.
        If no argument `path` is passed, default path './skpk_saved' will be used

    Returns
    -------
    list
        List of Cmt class instances as objects

    Raises
    -------
    Exception
        If no Cmt instance(s) are loaded from the folder path

    """
    cwd = os.getcwd() # Save current working directory
    __check_path_exist_before_load(path) # Check if folder path exists

    list_cmts = [] # Create empty list to store cmt objects
    for file in os.listdir('.'): # For files in current directory
        if (file.endswith('.pkl') and file.startswith('cmt')):
            cmt_object = pickle.load(open(file, "rb", -1))
            list_cmts.append(cmt_object)

    os.chdir(cwd) # Return console to original directory
    if len(list_cmts) == 0:
        raise Exception('No instances loaded. Please check arguments passed')
    if len(list_cmts) == 1:
        return list_cmts[0] # Directly unpack single-element list into a variable
    else:
        return list_cmts


def load_model(*filenames, path = './skpk_saved'):
    """Loads Model instance(s) by pickle filename from the input `path` folder.

    Parameters
    ----------
    *filenames
        Variable length list of names of Model instances (e.g. 'model_PK_Model').
    path : pathname
        Name of the folder path where Model instance(s) will be loaded from.
        If no argument `path` is passed, default path './skpk_saved' will be used.

    Returns
    -------
    list
        List of Model class instance(s) as objects

    Raises
    -------
    Exception
        If input filename(s) do not match any saved Model pickle filenames in path

    """
    cwd = os.getcwd() # Save current working directory
    __check_path_exist_before_load(path) # Check if folder path exists
    list_models = [] # Create empty list to store cmt objects

    for filename in filenames:
        pickle_filename = filename + '.pkl' # Convert to pickle file string
        if not os.path.exists(pickle_filename): # Check if filename exists
            existing_models = [file for file in os.listdir('.') if \
                            file.startswith('model') and file.endswith('.pkl')]
            os.chdir(cwd) # Return console to original directory
            raise Exception(f"""{pickle_filename} does not exist.
            List of existing model instances:
            {existing_models}""")
        else:
            model_object = pickle.load(open(pickle_filename, "rb", -1)) # Load pickle
            list_models.append(model_object)

    os.chdir(cwd) # Return console to original directory
    if len(list_models) == 0:
        raise Exception('No model loaded. Please check argument input')
    if len(list_models) == 1:
        return list_models[0] # Unpack single-element list into a variable
    else:
        return list_models


def load_all_models(path = './skpk_saved'):
    """Load all saved Model instances (pickle files) from input folder path.

    Parameters
    ----------
    path : pathname
        Name of the path here Model instance(s) (pickle files) will be loaded from.
        If no argument `path` is passed, default path './skpk_saved' will be used

    Returns
    -------
    list
        List of Model class instance(s) as objects

    Raises
    -------
    Exception
        If no Model instance(s) are loaded from the folder path

    """
    cwd = os.getcwd() # Save current working directory
    __check_path_exist_before_load(path) # Check if folder path exists

    list_models = [] # Create empty list to store model objects
    for file in os.listdir('.'): # For files in current directory
        if file.startswith('model') and file.endswith('.pkl'):
            model_object = pickle.load(open(file, "rb", -1))
            list_models.append(model_object)

    os.chdir(cwd) # Return console to original directory
    if len(list_models) == 0:
        raise Exception('No objects loaded. Please check argument input')
    if len(list_models) == 1:
        return list_models[0] # Unpack single-element list into a variable
    else:
        # Returns list of multiple compartment/model instances
        return list_models


def solve_ode():
    pass
