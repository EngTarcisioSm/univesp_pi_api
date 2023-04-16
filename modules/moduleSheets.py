from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import time

# Define escopo de atuacao sobre a api 
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Localiza o nome do arquivo sheets em trabalho 
SAMPLE_SPREADSHEET_ID = '1V_CQnIdQdlPZEbMZ45un_ID4JYSpTMKrlT0uqylmn5A'



class InterationSheets:
    
    def __init__(self) -> None:
        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

        dirname = os.path.dirname(__file__)
        filename_token = os.path.join(dirname, "token.json")
        filename_credential = os.path.join(dirname, "credential.json")

        if os.path.exists(filename_token):
            self.creds = Credentials.from_authorized_user_file(filename_token, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    filename_credential, SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(filename_token, 'w') as token:
                token.write(self.creds.to_json())
        
    
    def getSheets(self, nomePasta:str, pontInitLeitura:str, pontFimLeite:str)->list:
        
        sample_range_name = nomePasta + "!" + pontInitLeitura + ":" + pontFimLeite

        try:
            # Conexão com o serviço google em específico o google sheets 
            service = build(
                'sheets', 
                'v4', 
                credentials=self.creds
            )

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,             
                range=sample_range_name
            ).execute()
        

        except HttpError as err:
            print(err)
            return None
        # armazena os valores lidos 
        return result.get('values', [])
    
    def putSheet(self, nomePasta:str, pontInitLeitura:str, listaDados: list)->list:
        
        sample_range_name = nomePasta + "!" + pontInitLeitura

        try:
            # Conexão com o serviço google em específico o google sheets 
            service = build(
                'sheets', 
                'v4', 
                credentials=self.creds
            )

            # Call the Sheets API
            sheet = service.spreadsheets()

            result = sheet.values().update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range= sample_range_name,
                valueInputOption='RAW',
                body={
                    "values": listaDados
                }
            ).execute()

            print("OK")

        
        except HttpError as err:
            print(err)
        

if __name__ == "__main__":    
    teste = InterationSheets()
    teste.getSheets("Sheet1", "A1", "B369")

    listInsert = [
        ['A', '999'],
        ['B', '888'],
        ['C', '777'],
        ['D', '666'],
        ['E', 1],
        ['F', 2],
        ['G', 3],
        ['H', 4],
        ['I', 5],
        ['J', 6],
        ['K', 7],
        ['L', '=15+50+1000']
    ]

    teste.putSheet('Sheet1', 'A369', listInsert)