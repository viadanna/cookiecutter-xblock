Use this translations directory to provide internationalized strings for your XBlock project.

For more information on how to enable translations, visit the Open edX XBlock tutorial on Internationalization:
http://edx.readthedocs.org/projects/xblock-tutorial/en/latest/edx_platform/edx_lms.html

The template uses django-statici18n to provide translations to static javascript
using `gettext`.

The included `compile_jsi18n.sh` is a shortcut to generate translated javascript
which is used during `make` to load the Docker test environment.