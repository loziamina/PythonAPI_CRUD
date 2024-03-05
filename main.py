from fastapi import FastAPI , status, HTTPException, Depends
from database import Base, engine, SessionLocal
from pydantic import BaseModel
from sqlalchemy.orm import Session 
import models
import schemas
from typing import List


class ToDoRequest(BaseModel):
    task: str

Base.metadata.create_all(engine)

app = FastAPI()

def get_session(): 
    session = SessionLocal()
    try: 
        yield session
    finally : 
        session.close()

@app.get("/")
def root(): 
    return "todoo"





@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoCreate,  session: Session = Depends(get_session)):

    tododb = models.ToDo(task= todo.task)
    session.add(tododb)
    session.commit()
    session.refresh(tododb)

    id = tododb.id
    session.close()

    return f"created todo item with {id}" 


@app.get("/todo/{id}")
def read_todo(id: int,  session: Session = Depends(get_session)):
   

    todo = session.query(models.ToDo).get(id)
    #todo = session.query(ToDo).all()
    session.close()

    return todo



@app.put("/todo/{id}")
def update_todo(id: int, task: str,  session: Session = Depends(get_session)):


    # get the todo item with his id
    todo = session.query(models.ToDo).get(id)
# update todo with the given task

    if todo: 
        todo.task = task
        session.commit()
    
    session.close()

# check if todo item with given id existsif not = error 404
    if not todo: 
        raise HTTPException(status_code=404, detail = False)
    
    return todo




@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: int,  session: Session = Depends(get_session)):

    todo = session.query(models.ToDo).get(id)

    if todo:
        session.delete(todo)
        session.commit()
        session.close()
    else: 
        raise HTTPException(status_code=404, detail=False)
    
    return None





@app.get("/todo", response_model= List[schemas.ToDo])
def read_todo_list( session: Session = Depends(get_session)):

    todo_list = session.query(models.ToDo).all()
    session.close()

    return todo_list


