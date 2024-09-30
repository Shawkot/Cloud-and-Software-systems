FROM alpine:3.18
WORKDIR /app

COPY lucas.sh echo.sh ./
RUN chmod +x ./lucas.sh ./echo.sh

ENV COUNT=8
ENV MSG="Hello Docker!"

CMD ["/bin/sh", "-c", "/app/lucas.sh && /app/echo.sh"]



