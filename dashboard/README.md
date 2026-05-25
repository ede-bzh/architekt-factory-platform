# Dashboard legacy (port 8080)

Ce serveur (`dashboard/server.py`, SQLite `factory.db`) est **legacy**.

Pour le monitoring et la preuve qualité, utilisez la plateforme Architekt :

- **Monitoring live** : `/monitoring` et `GET /api/monitoring/live`
- **Preuve / DORA** : `/proof`
- **FinOps** : `/finops`

Le répertoire `dashboard/platform/` a été supprimé sur `main` — ne pas le recréer.
