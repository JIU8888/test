from flask import Flask

app = Flask(__name__)

topics = [
    {'id': 1, 'title': '고양이', 'body': '고양이 is 먀먀먀먀'},
    {'id': 2, 'title': '오리', 'body': '오리 is 엥모야'},
    {'id': 3, 'title': '슝슝이', 'body': '슝슝이 is 이히힝'}
]

def template(contents. content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
        </body>
    </html>
    '''
def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')


@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')

if __name__ == '__main__':
    app.run()
