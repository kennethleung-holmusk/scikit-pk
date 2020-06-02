# ===================================
#       Front-End User Script
# ===================================

# Import necessary libraries
import os
os.chdir(r'/home/klty0988/Desktop/scikit-pk/src')

# Main script for testing classes and functions
import skpk
import pickle


# Testing functions from mainFunctions.py
skpk.main.test_print(2,3)

# ===================================
#     Testing Compartment Class
# ===================================

C1 = skpk.Cmt('Absorption', 23)

C2 = skpk.Cmt('First-Pass', 10)

C3 = skpk.Cmt('Free Plasma Drug')

C2.set_attr('New First-Pass', 30)

C2.cmt_name
C2.Vd
C2.cmt_attr

C2.get_attr()

# Saving compartments

# C2.save_cmt('test_save_C2.pkl') - Use main function to save instead

skpk.main.save_cmt(C1, C2, C3)

skpk.main.list_saved_cmt()


# C1, C2, C3 = pickle.load(open('test_save_C2.pkl', "rb", -1))


D1 = skpk.main.load_cmt('Absorptdion')







# Testing Zone

skpk.main.load_cmt()

# ===================================
#         Testing Model Class
# ===================================

A = skpk.Model('Model1')

A.add_link([(3,4,5), (1,2,3)])

A.add_link([(4,)])

A.add_link([(4,7)])

# A.add_cmt([(3,22)])

A.add_bi_link([(6,4)])

A.cmt_list

A.link_list

A.get_link_params()

A.get_cmt_params()

A.get_cmt_id()

A.clear_all()

A.add_path([1,2,3,4,5,6], [23,25,44,33,24])

A.get_params()

A.get_cmt_after(4)

A.get_cmt_prior(4)

A.get_linked_cmt(4)

A.has_cmt_after(2)

A.has_cmt_prior(4)

A.remove_link([(1,2),(3,4),(4,5)])

A.get_params()
