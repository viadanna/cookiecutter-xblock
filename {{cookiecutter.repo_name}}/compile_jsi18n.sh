DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
./manage.py compilejsi18n \
    --settings {{cookiecutter.package_name}}.translations.settings \
    --namespace {{cookiecutter.class_name}}i18n \
    --domain text \
    --output $DIR/{{cookiecutter.package_name}}/public/js/translations
