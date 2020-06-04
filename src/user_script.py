# ****************************************
#          Front-End User Script
# ****************************************

# Import necessary libraries
import os
#os.chdir(r'/home/klty0988/Desktop/scikit-pk/src')
#os.chdir(r'C:\Users\klty0\Desktop\scikit-pk\src')
os.chdir(r'C:\Users\Kenneth Leung\Desktop\scikit-pk\src')

# Main script for testing classes and functions
import skpk

# ===========================================
#    Generating Compartment (CMT) Instances
# ===========================================

C1 = skpk.Cmt(1, 'A1', 1)
C2 = skpk.Cmt(2, 'First-Pass', 10)
C3 = skpk.Cmt(3, 'Free Plasma Drug')
C4 = skpk.Cmt(4, 'Protein Bound Plasma', 20)
C5 = skpk.Cmt(5, 'Peripheral Tissues', 15)

C1.get_attr()
C2.get_attr()
C3.get_attr()
C4.get_attr()
C5.get_attr()

C2.set_attr(new_cmt_name = 'First-Pass Metabolism')
C2.get_attr()

C2.cmt_name
C2.Vd

C1.set_attr(new_cmt_name = 'Absorption')
C1.get_attr()

C1.set_attr(new_cmt_id = 15)
C1.get_attr()
C1.cmt_attr

C3.cmt_attr

skpk.Cmt.list_cmt_ids
skpk.Cmt.list_cmt_names

# ===========================
#     Saving compartments 
# ===========================

skpk.main.save_cmt(C1, C2, C3, C4)

skpk.main.list_cmt(folder_path = './skpk_saved_cmts')


# ===========================
#     Loading compartments 
# ===========================

D1 = skpk.main.load_cmt('First-Pass')

D2 = skpk.main.load_cmt('First-Pass', folder_path = './wrongpath')

E1, E2 = skpk.main.load_cmt('Absorption', 'First-Pass')

D1.get_attr()

saved_cmts = skpk.main.load_all_cmt()

# Testing Zone

del A

test_tuple = (1,2,3,4)

(isinstance(test_tuple[0], int) and isinstance(test_tuple[1], int))

test_existing_links = [(1,2,3), (4,5,6), (7,8,9)]

test_new_tuples = [(1,2,3),(11,12,13), (14,15,16)]


test_exist_links = [(item[0], item[1]) for item in test_existing_links]


for tuple in test_new_tuples:
    if (tuple[0], tuple[1]) in test_exist_links:
        print('Have already')


# ===================================
#         Testing Model Class
# ===================================

A = skpk.Model('Model_Test_1')

A.get_links()

saved_cmts = skpk.main.load_all_cmt()

A.add_cmt(C1)  # Single item
A.add_cmt([C2,C3])   # If multiple instances, put into list
A.add_cmt(C4, C5)  # Error if not in list

test_list_tuples = [(C1,C2,1), (C2,C1,2)]

# Need to add extra criterion to check that CMT already exists, before adding link
A.add_link((C2, C1, 25))
A.add_link([(C1,C2,10), (C3,C4,50)])


A.list_cmt_links


A.add_link([(4,)])

A.add_link([(4,7)])

# A.add_cmt([(3,22)])

A.add_bi_link([(6,4)])

A.cmt_list

A.link_list

A.get_link_params()

A.get_cmt_params()

A.get_cmt_id()

A.clear_model()

A.add_path([1,2,3,4,5,6], [23,25,44,33,24])

A.get_params()

A.get_cmt_after(4)

A.get_cmt_prior(4)

A.get_linked_cmt(4)

A.has_cmt_after(2)

A.has_cmt_prior(4)

A.remove_link([(1,2),(3,4),(4,5)])

A.get_params()

del A
