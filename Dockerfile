# FROM python:3.8-alpine

FROM python:slim


RUN mkdir /lab1
WORKDIR /lab1
RUN pip install numpy scipy
# RUN apk add --update make cmake gcc g++ gfortran
# RUN pip install numpy scipy

# RUN apk add --update python py-pip python-dev
# RUN pip install cython
# RUN pip install numpy
# RUN pip install scikit-learn

#RUN apk --no-cache --update-cache add  python3 py3-pip py3-arrow  py3-pandas # and py3-anything package need to be compiled
#RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

LABEL maintainer="Dheeraj <jadheeraj.inbox@gmail.com>" \version="1.0"


CMD ["python", "src/lab1.py"]
