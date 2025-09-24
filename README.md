

# **Lab Module 5 – Stratégies avancées**

---

## **Exercice 1 : Comprendre le contexte multi-fichiers**

**Description**  
 Montrer que Copilot utilise imports \+ fichiers du workspace (`main.py`, `config.py`, `utils/parser.py`) pour générer du code cohérent.

**Instructions**

* Ouvrez le projet `Exercices`.

* Dans `main.py`, écrivez seulement :

```py
# Charger API_URL/TIMEOUT depuis config,
# appeler une API fictive et afficher parse_response(...)
```

* Laissez **Copilot (complétion)** proposer les imports et le squelette.

* Finalisez via **chat** si nécessaire (ex. gestion d’erreurs réseau avec `requests`).

**Critères de réussite**

* `main.py` importe bien `config` et `utils.parser`.

* Le script s’exécute (API simulée ou mock simple).

* Les propositions Copilot sont cohérentes avec les autres fichiers.

  ---

  ## **Exercice 2 : Ajouter une fonctionnalité transverse (multi-fichiers)**

**Description**  
 Implémenter une **journalisation commune** utilisée par plusieurs modules.

**Instructions**

* Complétez `logging_utils.py` avec seulement :

```py
# Fournir get_logger(name) configuré en JSON (stdout, niveau INFO par défaut)
```

* Laissez Copilot écrire `get_logger`.

* Modifiez `main.py` et `utils/parser.py` pour utiliser `get_logger`.

* Demandez au chat : « Quels fichiers dois-je modifier pour appliquer ce logger ? »

**Critères de réussite**

* Logs JSON uniformes.

* Pas de duplication de config logging.

* Import correct depuis plusieurs fichiers.

  ---

  ## **Exercice 3 : Explication & review de code par Copilot**

**Description**  
 Obtenir une **explication synthétique** et des **améliorations** sur le projet fourni.

**Instructions**

* Dans le chat, à la racine du workspace :

  * « Explique l’architecture du projet en 5 points. »

  * « Identifie 3 améliorations rapides. »

  * « Propose un petit refactor sans changer le comportement. »

* Appliquez 1–2 suggestions proposées.

**Critères de réussite**

* Explication correcte et concise.

* ≥ 2 améliorations intégrées.

* Diffs propres et compréhensibles.

  ---

  ## **Exercice 4 : Dépendances & contrat inter-modules**

**Description**  
 Rendre explicites les **contrats** entre fichiers (types, retours) et vérifier via tests.

**Instructions**

* Ajoutez des **docstrings** dans `utils/parser.py`.

* Demandez à Copilot : « Génère `tests/test_parser.py` avec pytest » (cas normal, clé manquante, dict vide).

* Dans le chat : « Liste les fonctions publiques et leurs pré/post-conditions. »

**Critères de réussite**

* Docstrings claires.

* ≥ 3 tests verts.

* Contrats inter-modules explicités.

  ---

  ## **Exercice 5 : Hallucination buster**

**Description**  
 Détecter quand Copilot invente un import ou une fonction inexistante.

**Instructions**

* Dans `main.py`, ajoutez un commentaire vague :  
   `# Exporter les résultats en CSV compressé`

* Si Copilot propose `from utils.csv_export import to_csv_gzip`, demandez-lui :  
   « Cette fonction n’existe pas. Crée le fichier et la fonction minimale avec tests. »

* Créez `utils/csv_export.py` avec la fonction réelle et un test simple.

**Critères de réussite**

* Pas de références fantômes.

* Fonction créée et testée.

* Import valide dans `main.py`.

  ---

  ## **Exercice 6 : Vigilance sécurité**

**Description**  
 Analyser et corriger du code risqué dans `danger.py`.

**Instructions**

* Ouvrez `danger.py` (déjà présent dans le bundle).

* Dans le chat : « Analyse les risques sécurité et propose une correction. »

* Appliquez les correctifs :

  * Supprimer `shell=True`.

  * Remplacer API\_KEY codée en dur par une variable obligatoire.

  * Ajouter des logs sécurisés.

**Critères de réussite**

* Recommandations pertinentes et appliquées.

* Patterns dangereux supprimés.

* Commentaire clair expliquant le risque.

  ---

  ## **Exercice 7 : Migration/refactor multi-fichiers**

**Description**  
 Renommer un module et adapter tous les imports avec Copilot.

**Instructions**

* Renommez `utils/parser.py` en `utils/response_parser.py`.

* Dans le chat : « Mets à jour tous les imports et liste les fichiers impactés. »

* Validez les diffs proposés (multi-fichiers).

**Critères de réussite**

* Aucune `ImportError`.

* Tests verts.

* Commit clair.

  ---

  ## **Exercice 8 : Revue finale du workspace**

**Description**  
 Utiliser Copilot pour une **checklist de fin** : lisibilité, logs, erreurs, tests, sécurité.

**Instructions**

* Dans le chat (racine) :

  * « Fais une revue globale : points faibles, dette technique, quick wins. »

  * « Propose un plan d’actions priorisé en 5 items. »

* Implémentez 1–2 quick wins rapides (factorisation, test manquant).

**Critères de réussite**

* Plan concret et priorisé.

* ≥ 2 quick wins appliqués.

* Projet exécutable et tests verts.