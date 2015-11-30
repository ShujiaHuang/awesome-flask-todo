# awesome-flask-todo

## How do I deploy this flask web application
<http://www.jianshu.com/p/be9dd421fb8d>

```
    mkdir log
    echo_supervisord_conf > supervisor.conf   # 生成 supervisor 默认配置文件
    vi supervisor.conf                       # 修改 supervisor 配置文件，添加 gunicorn 进程管理

    supervisord -c supervisor.conf
    env/bin/supervisorctl -c supervisor.conf status
    env/bin/supervisorctl -c supervisor.conf reload
    env/bin/supervisorctl -c supervisor.conf start awesome-flask-todo
    #env/bin/supervisorctl -c supervisor.conf start all
```
