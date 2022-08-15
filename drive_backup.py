import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import shutil

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']


def get_gdrive_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)


def upload_files():
    """
    Creates a folder and upload a file to it
    """
    repeat=0
    # authenticate account
    service = get_gdrive_service()
    
    
        
    # Call the Drive v3 API
    results = service.files().list(
        pageSize=100, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
        
    if not items:
        print('No files found.')
        return
    print('Files:')
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))
        if item['name']=='its.zip':
            repeat=1
            fol_rep=item['id']
            print(fol_rep)
            
            print("found its")
            break 

    
    
    if repeat==0:
        
        file_metadata = {
            "name": "its.zip",
            "parents": ['1b7Tx97hL7e_vN8PJSQi2EckjY_Ws6om8']
            }
        # upload
        #media = MediaFileUpload("weather.csv", resumable=True)
        shutil.make_archive('its', 'zip', 'C:\ITS-2.4.5b1')
        media = MediaFileUpload("its.zip", mimetype='application/zip',resumable=True)
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print("File created, id:", file.get("id"))
    else:
        #file_up = service.files().get(fileId=fol_rep).execute()
        file_metadata = {
            "name": "its.zip",
            "parents": ['1b7Tx97hL7e_vN8PJSQi2EckjY_Ws6om8']
            }
        # upload
        print("wait zipping file....")
        shutil.make_archive('its', 'zip', 'C:\ITS-2.4.5b1')
        print("zip finish")
        media = MediaFileUpload("its.zip", mimetype='application/zip',resumable=True)
        
        file = service.files().update(fileId=fol_rep, media_body=media).execute()
        print("File updated, id:", file.get("id"))
                       
    
if __name__ == '__main__':
    upload_files()