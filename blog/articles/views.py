from flask import Blueprint, render_template, redirect, request, url_for
from werkzeug.exceptions import NotFound
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload

from blog.models import Articles, Author, Tag
from blog.forms.article import CreateArticleForm
from blog.extensions import db

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


@article.route('/create', methods=['POST', 'GET'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)

    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if request.method == 'POST' and form.validate_on_submit():
        _article = Articles(title=form.title.data.strip(), text=form.text.data)
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)
        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        db.session.add(_article)
        db.session.commit()
        print(f'{_article} created!')

        return redirect(url_for('auth.index'))

    return render_template('articles/create.html', form=form)


@article.route('/', endpoint='articles_list', methods=['GET'])
def articles_list():
    articles = Articles.query.all()
    tags = Tag.query.all()
    if not articles:
        return redirect(url_for('article.create_article'))
    return render_template('articles/articles.html', articles=articles, tags=tags)


@article.route('/<int:article_id>', endpoint='article_detail', methods=['GET'])
@login_required
def get_article(article_id):
    _article = Articles.query.filter_by(id=article_id).options(joinedload(Articles.tags)).one_or_none()
    if not _article:
        raise NotFound(f'Article #{article_id} not found')
    return render_template('articles/detail.html', article=_article)
