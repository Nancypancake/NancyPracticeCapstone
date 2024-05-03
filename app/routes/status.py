from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Status, Response
from app.classes.forms import StatusForm, ResponseForm
from flask_login import login_required
import datetime as dt

@app.route('/status/new', methods=['GET', 'POST'])
@login_required
def statusNew():
    form = StatusForm()
    if form.validate_on_submit():
        newStatus = Status(
            user = current_user.id,
            mood = form.mood.data,
            note = form.note.data,
            favorite = form.favorite.data,
            modify_date = dt.datetime.utcnow
        )
        newStatus.save()
        return redirect(url_for("status",statusID=newStatus.id))
    
    if form.submit.data:
        if form.mood.data == 'None':
            form.mood.errors = ['Required']
        if form.favorite.data == 'None':
            form.favorite.errors = ['Required']
        
    return render_template("statusform.html",form=form)

@app.route('/status/edit/<statusID>', methods=['GET', 'POST'])
@login_required
def statusEdit(statusID):
    form = StatusForm()
    editStatus = Status.objects.get(id=statusID)
    if editStatus.user != current_user:
        flash("You can't edit a status you don't own.")
        return redirect(url_for('statuses', statusID=statusID))
    
    if form.validate_on_submit():
        editStatus.update(
            mood = form.mood.data,
            note = form.note.data,
            favorite = form.favorite.data,
            modify_date = dt.datetime.utcnow
        )
        return redirect(url_for("status",statusID=editStatus.id))
    
    form.mood.data = editStatus.mood
    form.note.data = editStatus.note
    form.favorite.data = editStatus.favorite
    return render_template("statusform.html",form=form)

@app.route('/status/<statusID>')
@login_required

def status(statusID):
    thisStatus = Status.objects.get(id=statusID)
    return render_template("status.html",status=thisStatus)

@app.route('/statuses')
@login_required

def statuses():
    statuses = Status.objects()
    return render_template("statuses.html",statuses=statuses)

@app.route('/status/delete/<statusID>')
@login_required
def statusDelete(statusID):
    deleteStatus = Status.objects.get(id=statusID)
    if current_user == deleteStatus.user:
        deleteStatus.delete()
        flash('Status has been deleted.')
    else:
        flash("You can't delete a status that isn't yours.")
    statuses = Status.objects()  
    return render_template('statuses.html',statuses=statuses)

@app.route('/response/new/<statusID>', methods=['GET', 'POST'])
@login_required
def responseNew(statusID):
    status = Status.objects.get(id=statusID)
    form = ResponseForm()
    if form.validate_on_submit():
        newResponse = Response(
            author = current_user.id,
            status = statusID,
            note = form.note.data
        )
        newResponse.save()
        return redirect(url_for('status',statusID=statusID))
    return render_template('responseform.html',form=form,status=status)

@app.route('/response/edit/<responseID>', methods=['GET', 'POST'])
@login_required
def responseEdit(responseID):
    editResponse = Response.objects.get(id=responseID)
    if current_user != editResponse.author:
        flash("You can't edit a response you didn't write.")
        return redirect(url_for('status',statusID=editResponse.status.id))
    status = Status.objects.get(id=editResponse.status.id)
    form = ResponseForm()
    if form.validate_on_submit():
        editResponse.update(
            note = form.note.data,
            modifydate = dt.datetime.utcnow
        )
        return redirect(url_for('status',statusID=editResponse.status.id))

    form.note.data = editResponse.note

    return render_template('responseform.html',form=form,status=status)   

@app.route('/response/delete/<responseID>')
@login_required
def responseDelete(responseID): 
    deleteResponse = Response.objects.get(id=responseID)
    deleteResponse.delete()
    flash('The response was deleted.')
    return redirect(url_for('status',statusID=deleteResponse.status.id))