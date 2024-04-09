from setuptools import setup

package_name = 'test_quality_of_service'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ban',
    maintainer_email='BanKiHyeon@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'deadline = test_quality_of_service.deadline:main',
        ],
    },
)


#'incompatible_qos = test_quality_of_service.incompatible_qos:main',
#'lifespan = test_quality_of_service.lifespan:main',
#'liveliness = test_quality_of_service.liveliness:main',
#'message_lost_listener = test_quality_of_service.message_lost_listener:main',
#'qos_overrides_listener = test_quality_of_service.qos_overrides_listener:main',
#'qos_overrides_talker = test_quality_of_service.qos_overrides_talker:main',

