# podman build -f podman.dockerfile -t podman:latest .

# syntax=docker/dockerfile:1

ARG NODE_VERSION = 22.8.0
ARG ALPINE_VERSION = 3.20

# FROM node:${NODE_VERSION}-alpine${ALPINE_VERSION} AS base
FROM node:22.8.0-alpine3.20 AS base
WORKDIR /src

# Error: building at STEP "COPY package*.json ./": checking on sources under "/var/tmp/libpod_builder1425495022/build": Rel: can't make  relative to /var/tmp/libpod_builder1425495022/build; copier: stat: ["/package*.json"]: no such file or directory

FROM base AS build
COPY package*.json ./
RUN npm ci
RUN npm run build

FROM base AS production
COPY package*.json ./
RUN npm ci --omit=dev && npm cache clean --force
COPY --from=build /src/dist/ .
CMD ["node", "app.js"]