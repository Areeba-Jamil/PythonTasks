#Todo App Using Flask


#flask run command to run the app on deployment server


#import required modules
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect

app = Flask(__name__)

#config method to locate db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

#initialize db
db = SQLAlchemy(app)

#create db model and define columns
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)
    comment = db.Column(db.String(500), nullable=False)


    #function to return task and its ID
    def __rep__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        task_content = request.form['content']
        task_comment = request.form['comment']

        new_task = Todo(content=task_content,comment=task_comment)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error adding the task'
    else:
        tasks = Todo.query.all()
        return render_template("index.html", tasks=tasks)

#route for deleting tasks
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Error occured while deleting task'

#route for updating tasks
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
       
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue while updating that task'

    else:
        return render_template('update.html', task=task)



if __name__ == "__main__":
    #True to run app on the deployment server
    app.run(debug=True)
