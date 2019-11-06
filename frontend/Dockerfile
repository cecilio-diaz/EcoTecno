FROM node:lts-alpine as builder
WORKDIR /app
COPY ./package*.json ./
RUN npm install
COPY ./ ./
RUN npm run build

FROM nginx:stable-alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY ./nginx/conf.d/default.template /etc/nginx/conf.d/default.template
ARG SERVICE_PORT
EXPOSE ${SERVICE_PORT}
ENV ESC='$'
CMD ["./entrypoint.sh"]
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
