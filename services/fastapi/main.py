from fastapi import FastAPI, responses
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import os
from os import path
import ast


from libs.classes import *

from libs.utils import create_datetime_name

# Custom
from logger import LoggingHandler
from libs.queues import RedisQueue
from libs.minio_tools import (
    create_bucket,
    get_minio_client,
    put_object
)

# ENV VARS
REDIS_NAME =  os.environ['REDIS_NAME']
REDIS_HOST =  os.environ['REDIS_HOST']
REDIS_PORT =  int(os.environ['REDIS_PORT'])


MINIO_HOST = os.environ['MINIO_HOST']
MINIO_KEY = os.environ['MINIO_KEY']
MINIO_SECRET = os.environ['MINIO_SECRET']
MINIO_SECURE = os.environ['MINIO_SECURE']
MINIO_BUCKET = os.environ['MINIO_BUCKET']
MINIO_DIR_TOPIC = os.environ['MINIO_DIR_TOPIC']


_DATA_FOLDER_PATH = os.getcwd() + "/" + "data"

_secure = False
if MINIO_SECURE == "1":
    _secure = True


# Aux functions
def set_filesystem(directory_fs):
    if not path.exists(directory_fs):
        os.makedirs(directory_fs)

# Create data dir if not exists
set_filesystem( _DATA_FOLDER_PATH )

# Logger
log = LoggingHandler()

# Minio client
minio_client =  get_minio_client(
    host = MINIO_HOST,
    key = MINIO_KEY,
    secret = MINIO_SECRET,
    secure = _secure
)


# Create S3 bucket
create_bucket(client =  minio_client, bucket_name = MINIO_BUCKET)


# Queue
Q = RedisQueue(name=REDIS_NAME, host=REDIS_HOST, port = REDIS_PORT, )


# Fast api instance
app = FastAPI()


@app.get("/api")
def home():
    return f"<h1>Hello from SALUD, current queue size: {Q.qsize()}</h1>"


@app.post('/api/v1/logger', response_model=LoggDataOut)
async def create_log(logg_data: LoggDataIn):

    index = logg_data.index
    kind_log = logg_data.kind
    logg_text = logg_data.text
    
    if kind_log == "ERROR":
        log.logger.error("Houston, we have a problem: %s", logg_text,  exc_info=1)
    else:
        log.logger.info("Houston, here is info: %s", logg_text,  exc_info=1)

    return LoggDataOut(index = index)


@app.post('/api/v1/create_queue')
async def create_queue(props: CreateQueueIn):
    """
        This creates the queue for job for CIs and birth dates.
    """
    # Flush 
    Q.flushdb()

    # read props and create IDs
    data_list = props.data
    
    Q.push(str(data_list))

    return { "total_jobs": Q.qsize() }


@app.get("/api/v1/user_details")
async def user_details(props: UserData):
    # Returns the parameters
    user_ci = props.ci
    user_birthdate = props.birth_date

    return { 'user_birthdate': user_birthdate, 'user_ci': user_ci, 'status': 'QUANTUM_UNCERTANLY'  }


@app.get("/api/v1/dequeue")
async def dequeue():
    # Create batch of indexes
    if Q.qsize() > 0:
            
        result_raw = Q.pop().decode("utf-8") 

        result = ast.literal_eval(result_raw)

        return { 'job': result }

    return { 'job': [] }


@app.get("/api/v1/queue_size")
def queue_size():
    # Get the queue size
    return { 'queue_size': Q.qsize() }