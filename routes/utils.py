import requests
import os
from models import Url
from extensions import db


API_KEY = os.environ.get('GOOGLE_API_KEY')

def get_seo_metrics(url):
    response = requests.get(f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={API_KEY}')
    if response.status_code == 200:
        data = response.json()
        metrics = {
            "speed_index": float(
                data['lighthouseResult']['audits']['speed-index']['displayValue'].split()[0].replace(',', '.')
            ),
            "time_to_interactive": float(
                data['lighthouseResult']['audits']['interactive']['displayValue'].split()[0].replace(',', '.')
            )
        }
        return metrics
    return None

def get_or_create_url(url):
    url_instance = Url.query.filter_by(url=url).first()
    if not url_instance:
        metrics = get_seo_metrics(url)
        if metrics:
            url_instance = Url(url=url,
                                speed_index=metrics['speed_index'], 
                                time_to_interactive=metrics['time_to_interactive'])
            db.session.add(url_instance)
            db.session.commit()
    return url_instance