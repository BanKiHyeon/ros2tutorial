import glob
import os

from setuptools import find_packages
from setuptools import setup

package_name = 'topic_service_action_example'
share_dir = 'share/' + package_name

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (share_dir + '/launch', glob.glob(os.path.join('launch', '*.launch.py'))),
        (share_dir + '/param', glob.glob(os.path.join('param', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ban',
    maintainer_email='BanKiHyeon@gmail.com',
    description='Package description',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'argument = topic_service_action_example.arithmatic.argument:main',
            'operator = topic_service_action_example.arithmatic.operator:main',
            'calculator = topic_service_action_example.calculator.main:main',
            'checker = topic_service_action_example.checker.main:main',
        ],
    },
)
