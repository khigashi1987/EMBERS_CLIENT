import requests
import pandas as pd
import numpy as np
import io
import base64

class EMBERSClient:
    def __init__(self, base_url="http://palaeo.nig.ac.jp/embers_api"):
        self.base_url = base_url

    def get_samples(self, conditions):
        response = requests.post(f"{self.base_url}/get_samples", json=conditions)
        response.raise_for_status()
        return response.json()

    def get_composition_by_ids(self, sample_ids):
        response = requests.post(f"{self.base_url}/get_composition_by_ids_binary", json={"sample_ids": sample_ids})
        response.raise_for_status()
        data = response.json()
        
        # バイナリデータをNumPy配列に変換
        binary_data = base64.b64decode(data['binary_data'])
        composition_matrix = np.load(io.BytesIO(binary_data))
        
        # DataFrameを作成
        df = pd.DataFrame(composition_matrix, columns=data['metadata']['taxonomy_labels'])
        df.index = data['metadata']['sample_ids']
        
        return df

    def get_composition_by_metadata(self, conditions):
        response = requests.post(f"{self.base_url}/get_composition_by_metadata_binary", json=conditions)
        response.raise_for_status()
        data = response.json()
        
        # バイナリデータをNumPy配列に変換
        binary_data = base64.b64decode(data['binary_data'])
        composition_matrix = np.load(io.BytesIO(binary_data))
        
        # DataFrameを作成
        df = pd.DataFrame(composition_matrix, columns=data['metadata']['taxonomy_labels'])
        df.index = data['metadata']['sample_ids']
        
        return df
