# to build image on top of other image here we are using node image which is build on alpine(linux distribution light weight os) os
FROM node:14.16.0-alpine3.10

# can only copy files from current dir(dir with docker file) into app dir in image. If no dir app it creates dir app.
COPY package.json Reame.md /app/

WORKDIR /app

#to copy all files and dir from current dir into workdir
COPY . .

#to copy file with space or other form we can use to copy file into workdir
COPY ["hello world.txt", "."]

#installs dependencies in package.json file
RUN npm install

#as apt is not supported in alpine we use apk to install dependencies.
RUN apk install python

#setting env varible
ENV API_URL=http://abc.com

#To create grp called app and to created user called app (-S for suster user -G for primary group).
RUN addgroup app && adduser -S -G app app

#TO use user called app for all the following actions. Move it to top to get access on all files in dir.
USER app

#SHELL FORM: default command to be executed if none provide on docker run. If muli cmd present only last one get exec Eg: docker run img_name npm start
CMD npm start

#EXEC FORM: In shell form it creates shell and executes it(resource waste).
CMD ["npm", "start"]

# need to use --entrypoint to replace this command
ENTRYPOINT ["npm", "start"]