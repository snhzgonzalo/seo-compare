from flask import render_template, request
from extensions import db
from models import Comparison
from routes import main
from .utils import get_or_create_url

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/compare', methods=['POST'])
def compare():
    if request.method == 'POST':
        url1 = request.form['url1']
        url2 = request.form['url2']

        url_instance1 = get_or_create_url(url1)
        url_instance2 = get_or_create_url(url2)

        if url_instance1 and url_instance2:
            comparison = Comparison(
                url1_id=url_instance1.id,
                url2_id=url_instance2.id
            )
            db.session.add(comparison)
            db.session.commit()
            return render_template('results.html', comparison=comparison)
    return render_template('error.html', error_message="Error al obtener datos")

@main.route('/history', methods=['GET'])
def history():
    comparisons = Comparison.query.all()
    return render_template('history.html', comparisons=comparisons)
