from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://sql12726309:q6MhKw4xCj@sql12.freesqldatabase.com/sql12726309?charset=utf8mb4"
)


def load_jobs_from_db():
    with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      jobs = list(result.mappings())
      return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("select * from jobs where id = :val")
            .bindparams(val=id))
        rows = list(result.mappings())
        if len(rows) == 0:
            return None
        else:
            return rows[0]
            
        

