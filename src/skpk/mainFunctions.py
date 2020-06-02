def test_print(x,y):
    number = x * y
    print(f'{x} * {y} = {number}')


# Functions to save and load multiple models/compartments
def save_cmt(*args, folder = 'skpk_saved'):
    '''
    Saves the compartment instances as pickle file inside folder
    '''
    # Store the pickle files in a designated folder
    os = __import__('os')

    # Get current working directory
    cwd = os.getcwd()

    # If directory does not exist, create new folder and enter that folder
    if not os.path.exists(f'./{folder}'):
        os.makedirs(f'./{folder}')
        print(f'Created new folder (/{folder}) to store the saved files')
        os.chdir(f'./{folder}')
    else:
        print(f'Saving in existing folder: {folder}')
        os.chdir(f'./{folder}')

    # Save the objects as a pickle file
    pickle = __import__('pickle')

    # Create individual pickle file for each compartment instance
    for arg in args:
        pickle_filename = f'{arg.cmt_name}' + '.pkl'
        with open(pickle_filename, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(arg, output, -1)

    # Return back to previous working directory
    os.chdir(cwd)


def list_saved_cmt(folder = 'skpk_saved'):
    os = __import__('os')
    if not os.path.exists(f'./{folder}'):
        raise Exception('Folder does not exist')
    else:
        print('List of saved instances')
        for file in os.listdir(f'./{folder}'):
            if file.endswith('.pkl'):
                print(file)




def load_cmt(filename, folder = 'skpk_saved'):
    '''
    docstring
    '''
    os = __import__('os')

    # Get current working directory
    cwd = os.getcwd()

    # Check if the input folder exists
    if not os.path.exists(f'./{folder}'):
        raise Exception('Folder does not exist')

    # Change directory if folder exists
    else:
        os.chdir('./' + folder)
        pickle = __import__('pickle')

    # Unpack single pkl file specified in filename input.
    # Convert to pickle file string
        pickle_filename = filename + '.pkl'
        if not os.path.exists(pickle_filename):
            raise Exception(f'{pickle_filename} does not exist')
            # Return back to previous working directory
            os.chdir(cwd)
        else:
            file = pickle.load(open(pickle_filename, "rb", -1))
            # Return back to previous working directory
            os.chdir(cwd)

            return file




# def load_cmt(filename):
#     pickle = __import__('pickle')
#     pickle_filename = filename + '.pkl'
#     with open('company_data.pkl', 'rb') as input:
#     company1 = pickle.load(input)


def load_multi_cmt():
    pass

# def save_multi_model(*args, filename):
#     pickle = __import__('pickle')
#     models_to_save =
#     with open(f'{filename}.pkl', 'wb') as output:  # Overwrites any existing file.
#         pickle.dump(*args, output, pickle.HIGHEST_PROTOCOL)
