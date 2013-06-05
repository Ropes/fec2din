from setuptools import setup, find_packages

with open('README.md', 'r') as l:
    long_desc = l.read()

setup(
   name='fec2',
   version='0.0.1',

   author='Scott Bigelow',
   author_email='epheph@gmail.com',
   description='''This is a small python script, which makes extensive use of boto, to provide human-readable out similar to ec2-describe-instances (ec2din). fec2din can be run with no arguments or a single argument of an instance ID, instance type, security group, etc. Simply named "f" + "ec2din", the command can easily be run after viewing the horrific ec2din output by simply typing "f!!" in a modern shell. This simple shortcut is why I left the standard ".py" extension off''',
   long_description=long_desc,

   maintainer='Josh Roppo',
   maintainer_email='joshroppo@gmail.com',

   scripts=['src/fec2din', 'src/fec2run'],
   install_requires=['boto>=2.9.5', 'argparse>=1.2.1'],

)
