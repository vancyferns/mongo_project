from application import app, db
from flask import render_template, flash, request, redirect, url_for
from bson import ObjectId
from datetime import datetime
from application.forms import TodoForm

@app.route("/")
def index():
    todos = []
    for todo in db.todo_flask.find().sort("date_created", -1):
        todo["_id"] = str(todo["_id"])
        todo["date_created"] = todo["date_created"].strftime("%b %d %Y %H:%M:%S")
        todos.append(todo)
    return render_template("view_todos.html", todos=todos)

@app.route("/add_todo", methods=["GET", "POST"])
def add_todo():
    form = TodoForm()
    if form.validate_on_submit():
        db.todo_flask.insert_one({
            "name": form.name.data,
            "description": form.description.data,
            "completed": form.completed.data,
            "date_created": datetime.utcnow()
        })
        flash("Todo added successfully!", "success")
        return redirect(url_for("index"))
    return render_template("add_todo.html", form=form)

@app.route("/update_todo/<id>", methods=["GET", "POST"])
def update_todo(id):
    form = TodoForm()
    todo = db.todo_flask.find_one({"_id": ObjectId(id)})

    if not todo:
        flash("Todo not found", "danger")
        return redirect(url_for("index"))

    if form.validate_on_submit():
        db.todo_flask.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "name": form.name.data,
                "description": form.description.data,
                "completed": form.completed.data,
                "date_created": datetime.utcnow()
            }}
        )
        flash("Todo updated successfully!", "success")
        return redirect(url_for("index"))

    # Pre-fill form on GET
    form.name.data = todo["name"]
    form.description.data = todo["description"]
    form.completed.data = todo["completed"]

    return render_template("add_todo.html", form=form)

@app.route("/delete_todo/<id>")
def delete_todo(id):
    db.todo_flask.delete_one({"_id": ObjectId(id)})
    flash("Todo deleted!", "success")
    return redirect(url_for("index"))
