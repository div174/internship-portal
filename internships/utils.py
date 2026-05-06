import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDate

def get_chart_data(applications):
    """
    Generate JSON data for Chart.js
    """
    # Pie/Doughnut Chart Data: Status Distribution
    status_counts = applications.values('status').annotate(count=Count('status'))
    pie_data = {
        'labels': [item['status'] for item in status_counts],
        'data': [item['count'] for item in status_counts],
        'colors': []
    }
    for item in status_counts:
        if item['status'] == 'Pending':
            pie_data['colors'].append('#f59e0b') # amber
        elif item['status'] == 'Selected':
            pie_data['colors'].append('#10b981') # emerald
        else:
            pie_data['colors'].append('#ef4444') # red

    # Line Chart Data: Applications over time (last 7-30 days)
    timeline = applications.annotate(date=TruncDate('created_at')).values('date').annotate(count=Count('id')).order_by('date')
    line_data = {
        'labels': [item['date'].strftime('%b %d') for item in timeline],
        'data': [item['count'] for item in timeline]
    }

    return {
        'pie_data': json.dumps(pie_data, cls=DjangoJSONEncoder),
        'line_data': json.dumps(line_data, cls=DjangoJSONEncoder)
    }
