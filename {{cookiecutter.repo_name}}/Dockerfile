FROM jbarciauskas/xblock-sdk
RUN mkdir -p /usr/local/src/{{cookiecutter.repo_name}}
VOLUME ["/usr/local/src/{{cookiecutter.repo_name}}"]
RUN echo "pip install -r /usr/local/src/{{cookiecutter.repo_name}}/requirements.txt" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
RUN echo "pip install -e /usr/local/src/{{cookiecutter.repo_name}}" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
RUN echo "/usr/local/src/{{cookiecutter.repo_name}}/compile_jsi18n.sh" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
RUN echo "exec python /usr/local/src/xblock-sdk/manage.py \"\$@\"" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
RUN chmod +x /usr/local/src/xblock-sdk/install_and_run_xblock.sh
ENTRYPOINT ["/bin/bash", "/usr/local/src/xblock-sdk/install_and_run_xblock.sh"]
CMD ["runserver", "0.0.0.0:8000"]
