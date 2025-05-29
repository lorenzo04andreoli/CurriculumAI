import uuid
from helper import extract_data_analysis, get_pdf_paths, read_uploaded_file 
from database import AnalysisDataBase
from ai import GroqClient
from models.resums import Resum
from models.file import File
import fitz  

database = AnalysisDataBase()
ai = GroqClient()
job = database.get_job_by_name('Vaga de Desenvolvedor BackEnd')

cv_paths = get_pdf_paths('curriculos')

for path in cv_paths:
    content = read_uploaded_file(path)
    resum = ai.resum_cv(content)
    opnion = ai.generate_opnion(content, job)
    score = ai.generate_score(content, job)

    resum_schema = Resum(
        id= str(uuid.uuid4()),
        job_id= job.get('id'),
        content=resum,
        file=str(path),
        opnion = opnion
    )

    file_schema = File(
        file_id = str (uuid.uuid4()),
        job_id = job.get('id')
    )

    print("Resumo gerado pelo AI:\n", resum)

    analysis_schema = extract_data_analysis(resum, job.get('id'), resum_schema.id, score)

    database.resums.insert(resum_schema.model_dump())
    database.analysis.insert(analysis_schema.model_dump())
    database.files.insert(file_schema.model_dump())