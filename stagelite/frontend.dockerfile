RUN mkdir /stagelite
COPY ./stagelite /stagelite
WORKDIR /stagelite/frontend
CMD yarn start