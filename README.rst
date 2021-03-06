============
django-build
============

django-build provides a management command 'build2s3' which labels,
tars and then gzips the source code and stores it in s3. Other features 
include a url to get the current version and some middleware which 
puts the version in the http headers.

Requirements
============

* boto: http://code.google.com/p/boto/
 
Installation
============

#. Add the `build` directory to your Python path.

#. Add your AWS access details to your project's `settings.py` file::

	AWS_ACCESS_KEY_ID = '...'
	AWS_SECRET_ACCESS_KEY = '...'
	
#. Optional: Add the `build` app to your `urls.py` file::
	
	(r'^build/', include('build.urls')),
	
#. Optional: Add the middleware to your project's `settings.py` file::

	MIDDLEWARE_CLASSES = (
		...
		'build.middleware.BuildMiddleware',
		...
	)
	
#. Now proceded to configuration to configure your project.

Configuration
=============

Here is an example configuration which is put into your `settings.py` file::

	AWS_BUILD_BUCKET_NAME = 'helloworld-releases'
	BUILD_VERSION = ('1', '0')
	BUILD_APPNAME = 'helloworld'
	BUILD_IGNORE = (
		os.path.normpath(os.path.join(PROJECT_ROOT, 'ignore_dir')),
	)
	
AWS_BUILD_BUCKET_NAME
	This is the bucket at s3 to save the code into.
	
BUILD_VERSION
	A tuple containing the major/minor version of your project.
	
BUILD_APPNAME
	Your project's name

BUILD_IGNORE
	A tuple of things to ignore when creating the build package.
	If given a directory, will ignore everything in that directory.
	
Usage
=====

build2s3
--------

To use it, run the `build2s3` management command::
	
	python manage.py build2s3
	
It should show a listing of files it is including then it will start uploading to s3.

version url
-----------

If the `urls.py` was updated to include the build app, then after running build2s3
you should be able to access the version at `/build/version/`

Note: This assumes that your template directory is `templates` on your project root 
as a VERSION.txt file gets written there.

License
=======

This software is provided under the MIT License. For more details please see the
LICENSE file that is included with the source code.