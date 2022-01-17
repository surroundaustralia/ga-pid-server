FROM httpd:2.4
COPY ./htdocs/ /usr/local/apache2/htdocs/
COPY ./conf/httpd.conf /usr/local/apache2/conf/httpd.conf
RUN mkdir -p /usr/local/apache2/conf/sites/
COPY ./conf/sites/geopid.surroundaustralia.com.conf /usr/local/apache2/conf/sites/geopid.surroundaustralia.com.conf
