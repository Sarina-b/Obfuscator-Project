FROM openjdk:11-jre-slim

RUN apt-get update && apt-get install -y wget

RUN mkdir -p /antlr

RUN wget https://www.antlr.org/download/antlr-4.13.1-complete.jar -O /antlr/antlr-4.13.1-complete.jar

COPY ./grammers /grammars/

CMD ["java", "-jar", "/antlr/antlr-4.13.1-complete.jar", "-Dlanguage=Python3", "-o", "/output", "/grammars/MiniC.g4"]
