FROM arm32v7/node:lts-alpine as build-stage
WORKDIR /code
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build


FROM arm32v7/nginx:stable-alpine as production-stage
COPY --from=build-stage /code/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]