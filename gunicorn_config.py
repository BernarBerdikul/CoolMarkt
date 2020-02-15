command = '/root/code/CoolMarkt/venv/bin/gunicorn'
pythonpath = '/root/code/CoolMarkt/CoolMarkt'
bind = '0.0.0.0:8001'
workers = 3
user = 'root'
limit_request_fields = 32000
limit_request_fields = 0
raw_venv = 'DJANGO_SETTING_MODULE=webshop.settings'
