```javascript

FROM alpine:latest

RUN echo @edge https://mirror.tuna.tsinghua.edu.cn/alpine/latest-stable/community >> /etc/apk/repositories 
&& echo @edge https://mirror.tuna.tsinghua.edu.cn/alpine/latest-stable/main >> /etc/apk/repositories RUN apk update && apk upgrade

RUN apk -U add 
gcc 
bash 
bash-doc 
bash-completion 
libffi-dev 
libxml2-dev 
libxslt-dev 
libevent-dev 
musl-dev 
openssl-dev 
python-dev 
py-imaging 
py-pip 
vim 
git 
redis 
libexif 
curl 
ca-certificates 
udev 
chromium 
chromium-chromedriver 
&& update-ca-certificates

RUN apk add --no-cache tzdata 
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime 
&& echo "Asia/Shanghai" > /etc/timezone

RUN rm -rf /var/cache/apk/* /tmp/* /var/tmp/* $HOME/.cache ## 清除缓存 RUN pip install --upgrade pip 
&& pip install Scrapy

RUN pip install scrapyd 
&& pip install scrapyd-client 
&& pip install scrapy-redis 
&& pip install scrapy-splash 
&& pip install scrapydweb 
&& pip install selenium

RUN pip install fake_useragent 
&& pip install scrapy_proxies 
&& pip install sqlalchemy 
&& pip install mongoengine 
&& pip install redis

WORKDIR /runtime/app RUN git clone https://github.com/scrapinghub/splash/

EXPOSE 5000 
EXPOSE 6800 
EXPOSE 8000 
EXPOSE 22 
EXPOSE 80 
EXPOSE 21 
EXPOSE 888 
EXPOSE 8888 
EXPOSE 443 
EXPOSE 3306 
EXPOSE 8050
```javascript
