from setuptools import find_packages, setup

package_name = 'wheel_odometry_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='maria',
    maintainer_email='maria@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
	'odometry_publisher = wheel_odometry_pkg.odometry_publisher:main',
        'odometry_subscriber = wheel_odometry_pkg.odometry_subscriber:main',
        ],
    },
)
