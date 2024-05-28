from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'niryo_one_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/urdf'+'/v1', glob("urdf/v1/*")),
        ('share/' + package_name + '/urdf'+'/v2', glob("urdf/v2/*")),               
        ('share/' + package_name + '/urdf'+'/v3', glob("urdf/v3/*")),     

        #('share/' + package_name + '/meshes'+'/v1' +'/collada', glob("meshes/v1/collada/*")),
        #('share/' + package_name + '/meshes'+'/v2' +'/collada', glob("meshes/v2/collada/*")),    
        #('share/' + package_name + '/meshes'+'/v1' +'/stl', glob("meshes/v1/stl/*")),
        #('share/' + package_name + '/meshes'+'/v2' +'/stl', glob("meshes/v2/stl/*")),                

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jarain78',
    maintainer_email='jarincon@ubu.upv.es',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
         
        ],
    },
)
