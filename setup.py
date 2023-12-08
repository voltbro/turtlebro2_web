from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'turtlebro_web'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # ('share/ament_index/resource_index/packages',
            # ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # (os.path.join('share', package_name), ['launch/web_server.xml']),
        # (os.path.join('share', package_name), 'launch/web_server.xml')
        ('share/' + package_name + '/launch', glob('launch/*'))
        # ('.', glob('launch/*'))
    ],
    install_requires=['setuptools','flask'],
    include_package_data=True,
    zip_safe=False,
    maintainer='pi',
    maintainer_email='cola@cactus.ru',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'web_server = turtlebro_web.web_server:main'
        ],
    },
)
