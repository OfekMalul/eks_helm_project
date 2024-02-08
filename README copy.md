# Weather App

Weather app provides the weekly forecast for any location around the globe!

## Features
* Current Weather - Get real-time updates on current weather conditions.
* Day and Night Weather - Detailed forecasts for both day and night conditions.
* Humidity Levels - Track and display humidity levels
* Error Handling - Ensures smooth operation even with missing or erroneous user inputs.

## Requirements
* Python3
* Flask
* Jinja
* Gunicorn
* Nginx

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install Python3
pip install Flask
pip install Jinja
pip install Gunicorn
pip install Nginx
```

## Configuration
Create systemd service for Gunicorn: /etc/systemd/system/my-app
```` 
[Unit]
Description=Gunicorn instance to serve my weather app
After=network.target

[Service]
User={your_user}
Group=www-data
WorkingDirectory=/home/{your_user}/Final_project_weather_forcast
Environment="PATH=/home/{your_user}/Final_project_weather_forcast/bin"
ExecStart=/usr/bin/gunicorn --workers 3 --bind unix:app.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
````
run service!
``` bash
sudo systemctl daemon-reload
sudo systemctl start my-app
sudo systemctl enable my-app
```

Configure Nginx file: /etc/nginx/sites-available/{file-name}
```
limit_req_zone $binary_remote_addr zone=mylimit:10m rate=3r/s;
server {
        listen 80;
        server_name 10.1.0.47;
                 # limit connections per ip
                limit_conn conn_limit_per_ip 5;

        location /{
                include proxy_params;
                proxy_pass http://unix:/home/ofek2/Final_project_weather_forcast/app.sock;

                # Rate Limit config
                limit_req zone=mylimit;
                limit_req_status 429;

                deny 10.10.1.183;
        }
}
```
Add configuration to Nginx file: /etc/nginx/nginx.conf
```
# add to html section
limit_conn_zone $binary_remote_addr zone=conn_limit_per_ip:10m;
```
link file and permissions for Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/{file-name} /etc/nginx/sites-enabled
sudo systemctl restart nginx
sudo ufw allow 'Nginx Full'
```
