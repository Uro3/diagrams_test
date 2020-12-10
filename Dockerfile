FROM python:3.8-alpine
RUN apk add --update --no-cache \
    graphviz \
    ttf-freefont \
    curl
RUN curl -O https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
    && mkdir -p /usr/share/fonts/noto \
    && unzip NotoSansCJKjp-hinted.zip -d /usr/share/fonts/noto/ \
    && fc-cache -fv \
    && rm NotoSansCJKjp-hinted.zip
RUN pip install diagrams
WORKDIR /app
ENTRYPOINT [ "python" ]
CMD [ "--version" ]
