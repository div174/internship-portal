#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

if [[ -n "${DJANGO_SUPERUSER_USERNAME}" ]] && [[ -n "${DJANGO_SUPERUSER_PASSWORD}" ]]; then
  python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists() or User.objects.create_superuser('${DJANGO_SUPERUSER_USERNAME}', 'admin@example.com', '${DJANGO_SUPERUSER_PASSWORD}')"
  echo "Superuser created successfully"
fi
