from setuptools import setup

package_name = 'helloworld_rclpy_pkg'

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
    description='Package description',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'helloworld_publisher = helloworld_rclpy_pkg.helloworld_publisher:main',
            'helloworld_subscriber = helloworld_rclpy_pkg.helloworld_subscriber:main',
        ],
    },
)
