FROM public.ecr.aws/lambda/python:3.9

# Install the function's dependencies using file requirements.txt
# from your project folder.
COPY models ./models
#FROM python:3.9


#RUN pip install -r requirements.txt

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY main.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "main.handler" ]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"] 
#EXPOSE 5000
