# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import P6_number_of_paths as paths
app = FastAPI()

class DrugRequest(BaseModel):
    drug_id: str

@app.post("/pathways/")
def get_number_of_pathways(request: DrugRequest):
    file_path = './drugbank_partial.xml'

    path = paths.create_number_of_interacting_paths(file_path)
    
    drug_id = request.drug_id
    
    pathway = path['drugbank-id'].apply(lambda x: drug_id in x)
    pathway_count = path[pathway]['pathway_count'].values
    
    if len(pathway_count) > 0:
        pathway_count = int(pathway_count[0])
    else:
        pathway_count = 0
    return {"drug_id": drug_id, "pathway_count": pathway_count}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)