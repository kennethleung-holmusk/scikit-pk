# ****************************************
#          Front-End User Script
# ****************************************

# Import necessary libraries
import os
#os.chdir(r'/home/klty0988/Desktop/scikit-pk/src')
os.chdir(r'C:\Users\klty0\Desktop\scikit-pk\src')
#os.chdir(r'C:\Users\Kenneth Leung\Desktop\scikit-pk\src')

# ===========================================
#              Demonstration
# ===========================================

import skpk

C1 = skpk.Cmt(1, 'A1', 1)
C2 = skpk.Cmt(2, 'First-Pass', 10)
C3 = skpk.Cmt(3, 'Free Plasma Drug')
C4 = skpk.Cmt(4, 'Protein Bound Plasma', 20)
C5 = skpk.Cmt(5, 'Peripheral Tissues', 15)

C1.get_attr()
C1.set_attr(new_cmt_name = 'Absorption')
C1.get_attr()

C1.list_cmt_names
C1.list_cmt_ids

C2.get_attr()
C2.set_attr(new_cmt_vol = 15)
C2.get_attr()

skpk.main.save(C1, C2, C3, C4, C5)
skpk.main.list_all(path = './skpk_saved')

D1 = skpk.main.load_cmt('cmt_Free Plasma Drug')
D1.get_attr()


# Instantiate a model
A = skpk.Model('Model_Test')

A.add_cmt(C1)
A.add_cmt([C2,C3,C4,C5])

A.add_link((C2, C1, 25))
A.add_link((C3, C1, 50))
A.add_link([(C4, C3, 1520), (C3, C5 ,550)])
A.add_link((C2, C5, 123))

A.get_all_cmts()
A.get_all_links()
A.linked_cmts()

A.summary()

A.get_all_cmts()
A.set_cmt_attr(1, 'Absorption Cmt')
A.set_cmt_attr(1, cmt_vol = 123)
A.set_cmt_attr(2, 'First-Pass Metabolism', 150)
A.get_all_cmts()

A.set_link_attr(3,1,9000)

A.remove_link(2,1)
A.get_all_links()

A.remove_cmt(3)
A.get_all_cmts()
A.get_all_links()
A.list_cmt_links

A.get_matrix()

A.clear_model()
del A


# ===========================================
#    Generating Compartment (CMT) Instances
# ===========================================

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

skpk.main.save(A, B)

skpk.main.save_model(A)

skpk.main.list_all(path = './skpk_saved')


# =====================================
#     Loading compartments /Models
# =====================================

D1 = skpk.main.load_cmt('cmt_First-Pass', path = './skpk_saved')

D2 = skpk.main.load_cmt('First-Pass', folder_path = './wrongpath')

E1, E2 = skpk.main.load_cmt('Absorption', 'First-Pass')

D1.get_attr()

saved_cmts = skpk.main.load_all_cmts()

saved_models = skpk.main.load_all_models()

new_model = skpk.main.load_model('model_Model_Test')

new_model.get_all_links()

# Testing Zone

all_models = skpk.main.load_all_models()

# ===================================
#         Testing Model Class
# ===================================


# Testing cmt not added to model
C99 = skpk.Cmt(99, 'Brain ECF', 10)

A.add_cmt(C99)

A.add_link((C99, C1, 10))

A.linked_cmts()
A.get_links()

skpk.main.save_model(A)

A.list_cmt_links

A.list_cmt_links_tuples


A.get_all_cmts()


A.get_cmt_after(4)

A.get_cmt_prior(4)

A.get_linked_cmt(4)

A.has_cmt_after(2)

A.has_cmt_prior(4)

A.remove_link([(1,2),(3,4),(4,5)])

A.get_params()

A.get_matrix()

A.linked_cmts()

A.get_linked_cmts_in_model()


# ==============================
#       Testing GraphViz
# ==============================
import pydotplus
import graphviz
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

from IPython.display import display, Image

G = pydot.Dot(graph_type='digraph')
node = pydot.Node('test_node', style='filled',fillcolor='green')
G.add_node(node)


im = Image(G.create_png())
display(im)

plt.imshow()











