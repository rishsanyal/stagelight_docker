FROM node:16-alpine
RUN mkdir /stagelite
ADD ./stagelite /stagelite
WORKDIR /stagelite/frontend
EXPOSE 3000
CMD yarn start