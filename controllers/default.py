def index():
    document = db().select(db.document.ALL, orderby=db.document.title)
    return dict(document=document)

def show():
    document = db.document(request.args(0,cast=int)) or redirect(URL('index'))
    db.document.document_id.default = document.id
    return dict(document=document)

def user():
    return dict(form=auth())

def download():
    return response.download(request, db)

def preview():
    return dict()

@auth.requires_login()
@auth.requires_membership('Manager')
def manage():
    grid = SQLFORM.smartgrid(db.document)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Manager')
def manageNew():
    document = db().select(db.document.ALL)
    return dict(document=document)

def edit():
    parameters = request.args
    submitted_id = parameters[0]
    if db(db.document.id == submitted_id):
        return dict(id=submitted_id)

def update():
    submitted_title = request.vars.title
    submitted_id = request.vars.id

    if db(db.document.id == submitted_id).select():

        db(db.document.id == submitted_id).update(
            title = submitted_title
        )
        return 'Update Succesful'
    else:
        return 'Error'

def delete():
    parameters = request.args
    submitted_id = parameters[0]

    if db(db.document.id == submitted_id).select():

        db(db.document.id == submitted_id).delete()
        redirect(URL('manageNew'))
    else:
        return 'No User with the ID found'

def add():
    return dict()

def store():
    submitted_title = request.vars.title
    submitted_file = request.vars.file.file

    results = db.document.insert(
                    title = submitted_title,
                    file = submitted_file
                )
    if results:
        redirect(URL('manageNew'))
    else:
        return "Error"
