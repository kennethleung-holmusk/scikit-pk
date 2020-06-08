# =========================
#     Compartment Class
# =========================
class Cmt:
    """A class used to represent a compartment in a pharmacokinetic (PK) model

    Attributes
    ----------
    list_cmt_ids : list
        List of compartment IDs of the instantiated compartment instances.
    list_cmt_names : list
        List of compartment names of the instantiated compartment instances.

    """
    list_cmt_ids = [] # List of IDs of all instantiated compartment instances
    list_cmt_names = [] # List of names of all instantiated compartment instances


    def __check_cmt_id_exist(self, cmt_id):
        """Check whether input cmt_id already exists in list of Cmt IDs.

        Parameters
        ----------
        cmt_id : int
            ID of PK compartment.

        Raises
        -------
        Exception
            If input compartment ID (cmt_id) already exists in list_cmt_ids.

        """
        if cmt_id in self.list_cmt_ids:
            raise Exception(f"""Compartment ID {cmt_id} already exists.
            \nList of existing compartment IDs: {self.list_cmt_ids}""")


    def __check_cmt_name_exist(self, cmt_name):
        """Check whether input cmt_name already exists in list_cmt_names.

        Parameters
        ----------
        cmt_name : str
            Name of PK compartment.

        Raises
        -------
        Exception
            If input compartment name (cmt_name) already exists in list_cmt_names.

        """
        if cmt_name in self.list_cmt_names:
            raise Exception(f"""Compartment name {cmt_name} already exists.
            List of existing compartment names: {self.list_cmt_names}""")


    def __check_cmt_id_dtype(self, cmt_id):
        """Check that input cmt_id is of integer type.

        Parameters
        ----------
        cmt_id : int, optional
            ID of PK compartment.

        Raises
        -------
        Exception
            If input cmt_id is not an integer value.

        """
        if isinstance(cmt_id, (int, type(None))) == False:
            raise Exception('Compartment ID (cmt_id) must be an integer')
        else:
            pass


    def __check_cmt_name_dtype(self, cmt_name):
        """Check that input cmt_name is of string type.

        Parameters
        ----------
        cmt_name : str, optional
            Name of PK compartment.

        Raises
        -------
        Exception
            If input cmt_name is not a string value.

        """
        if isinstance(cmt_name, (str, type(None))) == False:
            raise Exception('Compartment name (cmt_name) must be a string')
        else:
            pass


    def __check_cmt_vol_dtype(self, cmt_vol):
        """Checks that input cmt_vol is of integer or float type.

        Parameters
        ----------
        cmt_vol : int, float, optional
            Volume of PK compartment.

        Raises
        -------
        Exception
            If input cmt_vol is not an integer or float value.

        """
        if isinstance(cmt_vol, (int, float, type(None))) == False:
            raise ValueError('Compartment volume must be an integer or float')
        else:
            pass


    def __init__(self, cmt_id, cmt_name, cmt_vol = 0):
        """Constructor for the compartment (Cmt) class

        If argument `cmt_vol` is not passed in, the default cmt_vol of 0L is used

        Attributes are stored in the cmt_attr tuple

        Parameters
        ----------
        cmt_id : int
            ID of PK compartment
        cmt_name : str
            Name of PK compartment
        cmt_vol : int, float, optional
            Volume of PK compartment (default is 0L)

        Returns
        -------
        Cmt instance
            Instance of Compartment class.

        """
        self.__check_cmt_id_dtype(cmt_id) # Checks data type of cmt_id
        self.__check_cmt_name_dtype(cmt_name) # Checks data type of cmt_name
        self.__check_cmt_vol_dtype(cmt_vol) # Checks data type of cmt_vol
        self.__check_cmt_id_exist(cmt_id) # Checks that cmt_id already exists
        self.__check_cmt_name_exist(cmt_name) # Checks that cmt_name already exists
        self.cmt_attr = (cmt_id, cmt_name, cmt_vol) # Tuple of attributes
        self.list_cmt_ids.append(self.cmt_attr[0]) # Collate compartment IDs in list
        self.list_cmt_names.append(self.cmt_attr[1]) # Collate compartment names in list
        print(f'{cmt_id}-{cmt_name} compartment successfully generated')


    def set_attr(self, new_cmt_id = None, new_cmt_name=None, new_cmt_vol=None):
        """Modify the attributes of existing compartment instance
        (outside of Model instance).

        No modifications will be made if no arguments are passed

        Parameters
        ----------
        new_cmt_id : int, optional
            New ID assigned to PK compartment instance.
        new_cmt_name : str, optional
            New name assigned to PK compartment instance.
        new_cmt_vol : int, float, optional
            New volume assigned to PK compartment instance.

        """
        if new_cmt_id is None:
            pass # If no new ID input, then keep existing ID
        else:
            self.__check_cmt_id_dtype(new_cmt_id)
            self.__check_cmt_id_exist(new_cmt_id)

            # Remove current ID that is about to be replaced
            current_cmt_id = self.cmt_attr[0]
            self.list_cmt_ids.remove(current_cmt_id)

            tuple_as_list = list(self.cmt_attr)
            tuple_as_list[0] = new_cmt_id
            self.cmt_attr = tuple(tuple_as_list)

            # Append new cmt_id in list of cmt ids (list_cmt_ids)
            self.list_cmt_ids.append(new_cmt_id)

        if new_cmt_name is None:
            pass
        else:
            self.__check_cmt_name_dtype(new_cmt_name)
            self.__check_cmt_name_exist(new_cmt_name)
            current_cmt_name = self.cmt_attr[1]
            self.list_cmt_names.remove(current_cmt_name)

            tuple_as_list = list(self.cmt_attr)
            tuple_as_list[1] = new_cmt_name
            self.cmt_attr = tuple(tuple_as_list)

            # Append new cmt_id in list of cmt ids (list_cmt_ids)
            self.list_cmt_names.append(new_cmt_name)

        if new_cmt_vol is None:
            pass  # If no new cmt_vol, then keep current value
        else:
            self.__check_cmt_vol_dtype(new_cmt_vol)
            tuple_as_list = list(self.cmt_attr)
            tuple_as_list[2] = new_cmt_vol
            self.cmt_attr = tuple(tuple_as_list)


    def get_attr(self):
        """Print attributes of existing compartment (cmt) instance.

        Compartment ID, Compartment Name, and Compartment Volume (in litres).

        """
        print(f"Compartment ID: {self.cmt_attr[0]}")
        print(f"Compartment Name: {self.cmt_attr[1]}")
        print(f"Compartment Volume: {self.cmt_attr[2]} L")
