import pandas as pd
import requests
import os
import json

# Retrieve the answer from the College Board API
def retrieve_answer_from_college_board(school_name: str ) -> str:
  # Check if the school_name exists in the DataFrame
    if school_name in data['school_name'].values:
        # Retrieve the row corresponding to the school_name
        school_info = data[data['school_name'] == school_name]
        # Convert the DataFrame row to a dictionary, then to a JSON string
        return json.dumps({
            'status': 'success',
            'data': school_info.to_dict(orient='records')[0]
        })
    else:
        # Return a JSON string indicating the school was not found
        return json.dumps({'status': 'School not found'})

  
  