import os
import numpy as numpy

import nibabel as nib

example_filename = os.path.join("./sample_data", "Brats18_CBICA_AVV_1_t1.nii.gz")
img = nib.load(example_filename)

print("Image shape: {}".format(img.shape))
print("Data type of data stored in image: {}".format(img.get_data_dtype()))
print("Image affine: {}".format(img.affine))
print("Image affine shape: {}".format(img.affine.shape))
print("\n")

# access to the image data as a numpy array
print("... Accessing to the data stored in the image as a numpy array... ")
data = img.get_fdata()
print("Data shape: {}".format(data.shape))
print("Data type: {}".format(type(data)))
print("\n")

#saving the data back into a .nii.gz file
new_img = nib.Nifti1Image(data, img.affine)
nib.save(img, os.path.join('./output_data','saved_data.nii.gz'))
print("New data was saved successfully in {}".format(os.path.join('./output_data','saved_data.nii.gz')))