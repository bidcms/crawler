```javascript
FROM alpine

RUN echo @edge https://mirror.tuna.tsinghua.edu.cn/alpine/latest-stable/community >> /etc/apk/repositories 
RUN echo @edge https://mirror.tuna.tsinghua.edu.cn/alpine/latest-stable/main >> /etc/apk/repositories RUN apk update RUN apk upgrade

RUN apk -U add \
gcc \
bash \
bash-doc \
bash-completion \
libffi-dev \
libxml2-dev \
libxslt-dev \
libevent-dev \
musl-dev \
openssl-dev \
python-dev \
py-imaging \
py-pip \
vim \
git \
redis \
libexif \
curl \
ca-certificates \
udev \
chromium \
chromium-chromedriver
RUN update-ca-certificates

RUN apk add --no-cache tzdata 
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime 
RUN echo "Asia/Shanghai" > /etc/timezone
## 清除缓存 
RUN rm -rf /var/cache/apk/* /tmp/* /var/tmp/* $HOME/.cache
RUN pip install --upgrade pip 
RUN pip install Scrapy

RUN pip install scrapyd 
RUN pip install scrapyd-client 
RUN pip install scrapy-redis 
RUN pip install scrapy-splash 
RUN pip install scrapydweb 
RUN pip install selenium

RUN pip install fake_useragent 
RUN pip install scrapy_proxies 
RUN pip install sqlalchemy 
RUN pip install mongoengine 
RUN pip install redis

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
