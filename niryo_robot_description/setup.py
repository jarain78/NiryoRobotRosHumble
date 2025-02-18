import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'niryo_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #('share/' + package_name, glob('urdf/ned/*')), 
        #('share/' + package_name, glob('urdf/ned2/*')), 
        #('share/' + package_name, glob('urdf/one/*')),                                    
        ('share/' + package_name + '/urdf/ned', glob("urdf/ned/*")),
        ('share/' + package_name + '/urdf/ned2', glob("urdf/ned2/*")),     
        ('share/' + package_name + '/urdf/ned3', glob("urdf/ned3/*")),             
        ('share/' + package_name + '/urdf/one', glob("urdf/one/*")),  
           
	('share/' + package_name + '/meshes/ned/collada', glob("/meshes/ned/collada/*")),
	('share/' + package_name + '/meshes/ned2/collada', glob("/meshes/ned2/collada/*")),	
	('share/' + package_name + '/meshes/one/collada', glob("/meshes/one/collada/*")),
	
	('share/' + package_name + '/meshes/ned/stl', glob("/meshes/ned/stl/*")),
	('share/' + package_name + '/meshes/ned2/stl', glob("/meshes/ned2/stl/*")),
	('share/' + package_name + '/meshes/one/stl', glob("/meshes/one/stl/*")),


    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='NN',
    maintainer_email='NN@email.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
