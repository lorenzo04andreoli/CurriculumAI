import uuid
from models.job import Job
from database import AnalysisDataBase

database = AnalysisDataBase()

name = 'Vaga de Desenvolvedor BackEnd'

activities = '''
Gerenciar banco de dados SQL
auxiliar na criação de projetos em python
Resolver problemas cotidianos em aplicações
Acompanhar e ajudar o time de desenvolvedores
'''

prerequisites = '''
Experiencia com API's
Experiência com Docker
Disponibilidade para trabalhar presencial uma vez na semana
Domínio em python
Experiência com IA
'''

differentials = '''
Conhecimento em frameworks
Interesse em aprender e crescer na empresa
Experiência de 1 ano em TI
'''

job = Job(
    id = str(uuid.uuid4()),
    name = name,
    main_activities = activities,
    prerequisites = prerequisites,
    differentials = differentials
)

database.jobs.insert(job.model_dump())