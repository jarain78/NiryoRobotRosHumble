from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'test_niryo_v3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, "launch"), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, "config"), glob('config/*')),
   
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jarain78',
    maintainer_email='jrincon@dsic.upv.es',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_niryo_v3_node = test_niryo_v3.test_niryo_v3:main',
            'test_niryo_unity_v3_node = test_niryo_v3.test_niryo_unity_v1:main'
        ],
    },
)
