import os
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from database import AnalysisDataBase

database = AnalysisDataBase()

st.set_page_config(layout='wide', page_title='Analisador')

option = st.selectbox(
    'Escolha a sua vaga:',
    [job.get('name') for job in database.jobs.all()],   
    index = None
)

if option:
    job = database.get_job_by_name(option)
    data = database.get_analysis_by_job_id(job.get('id'))

    df = pd.DataFrame(
        data if data else {},
        columns = [
            'name',
            'education',
            'skills',
            'languages',
            'score',
            'resum_id',
            'id'
        ]
    )

    df.rename(
        columns={
            'name': 'Nome',
            'education': 'Educação',
            'skills': 'Habilidades',
            'languages': 'Idiomas',
            'score': 'Score',
            'resum_id': 'Resum ID',
            'id': 'ID'
        },
        inplace=True
    )

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True)

    if data:
        gb.configure_column('Score', header_name='Score', sort='desc')
        gb.configure_selection(selection_mode='multiple', use_checkbox=True)

    grid_options = gb.build()

    st.subheader('Classificação dos Candidatos')
    st.bar_chart(df, x='Nome', y='Score', color='Nome', horizontal=True)

    response = AgGrid(
        df,
        gridOptions=grid_options,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.COLUMN_CHANGED,
        theme='streamlit'
    )

    selected_candidates = response.get('selected_rows', [])
    candidates_df = pd.DataFrame(selected_candidates)

    resums = database.get_resums_by_job_id(job.get('id'))

    def delete_files_resum(resums):
        for resum in resums:
            path = resum.get('file')
            if os.path.isfile(path):
                os.remove(path)

    if st.button('Limpar Análises'):
        database.delete_all_resums_by_job_id(job.get('id'))
        database.delete_all_analysis_by_job_id(job.get('id'))
        database.delete_all_files_by_job_id(job.get('id'))



    if not candidates_df.empty:
        cols = st.columns(len(candidates_df))
        for idx, row in enumerate(candidates_df.iterrows()):
            with st.container():
                if resum_data := database.get_resum_by_id(row[1] ['Resum ID']):
                    st.markdown(resum_data.get('content'))
                    st.markdown(resum_data.get('opnion'))

                    with open(resum_data.get('file'), 'rb') as file:
                        pdf_data = file.read()

                        st.download_button(
                            label= f"Download Currículo {row[1]['Nome']}",
                            data = pdf_data,
                            file_name=f"{row[1]['Nome']}.pdf",
                            mime='application/pdf'
                        ) 