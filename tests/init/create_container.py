#!/usr/bin/python3

from azure.storage.blob import BlobServiceClient
import os
import urllib3

"""
create_container.py - script for initial provisioning of Azurite
"""
urllib3.disable_warnings()

os.environ['AZURE_STORAGE_CONNECTION_STRING'] = 'DefaultEndpointsProtocol=https;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=https://127.0.0.1:10000/devstoreaccount1;'
os.environ['STORAGE_CONTAINER'] = 'my-test-container'

blob_service_client = BlobServiceClient.from_connection_string(conn_str=os.environ.get("AZURE_STORAGE_CONNECTION_STRING"),
                                                               retry_total=0,
                                                               connection_verify=False)
try:
    blob_service_client.create_container(os.environ.get("STORAGE_CONTAINER"))
except Exception as e:
    print(e)
