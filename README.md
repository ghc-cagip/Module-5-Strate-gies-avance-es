# ✅ **Lab Module 5 — Stratégies avancées (avec utilisation obligatoire de `copilot-instruction.md`)**

> Pour chaque exercice :
> **Vous devez utiliser le fichier `copilot-instruction.md` comme protocole de travail.**
>
> Cela signifie que, AVANT que Copilot modifie un fichier, vous devez lui demander :
>
> ✅ de produire un **plan de modification**
> ✅ d’annoncer le **nombre de modifications**
> ✅ de n’appliquer qu’**une modification à la fois** en attendant votre validation
> ✅ d’expliquer ce qu’il change et pourquoi

Exemple de prompt à utiliser systématiquement :

> « Suis strictement les directives du fichier `copilot-instruction.md`.
> Propose un plan détaillé des modifications, puis exécute **uniquement la modification n°1** et attends ma confirmation. »

> **Aucune modification ne doit être faite par Copilot sans plan préalable.**
>
> → C’est l’application systématique du fichier `copilot-instruction.md`.

---
## **Exercice 1 : Comprendre le contexte multi-fichiers**

**Description**
Démontrer que Copilot utilise le contexte du workspace (`main.py`, `config.py`, `utils/parser.py`) pour générer du code cohérent.

**Instructions**

1. Ouvrir `main.py`.
2. Écrire uniquement :

```py
# Charger API_URL/TIMEOUT depuis config,
# appeler une API fictive et afficher parse_response(...)
```

3. Dans Copilot :

   > « Selon `copilot-instruction.md`, propose un plan détaillé avant de générer du code. »

4. Valider les modifications **une par une**.

**Critères de réussite**

* `main.py` importe `config` et `utils.parser`.
* Le script tourne (mock API accepté).
* Copilot a suivi le protocole **plan → modification séquentielle**.

---

## **Exercice 2 : Ajouter une fonctionnalité transverse (multi-fichiers)**

**Description**
Créer un logger commun utilisé par plusieurs fichiers.

**Instructions**

1. Créer / ouvrir `logging_utils.py` et mettre uniquement :

```py
# Fournir get_logger(name) configuré en JSON (stdout, niveau INFO par défaut)
```

2. Dans Copilot :

   > « Suis `copilot-instruction.md`. Propose un plan, puis génère `get_logger`. »

3. Modifier `main.py` et `utils/parser.py` **via Copilot**, en lui demandant :

   > « Quels fichiers dois-je modifier selon ton plan ? Fais uniquement la modification n°1. »

**Critères de réussite**

* Logs JSON uniformes.
* Pas de duplication de config.
* Imports corrects.

---

## **Exercice 3 : Explication & review de code par Copilot**

**Description**
Faire analyser le projet et obtenir des suggestions d’amélioration.

**Instructions**

Dans le chat, à la racine :

* « Explique l’architecture du projet en 5 points. »
* « Suis `copilot-instruction.md`. Propose un plan de refactor léger. »
* « Applique uniquement la modification n°1 du plan. »

**Critères de réussite**

* Explication courte.
* ≥ 2 améliorations intégrées.
* Diffs clairs.

---

## **Exercice 4 : Dépendances & contrat inter-modules**

**Description**
Rendre explicite le contrat entre fichiers via docstrings + tests.

**Instructions**

1. Ajouter des docstrings dans `utils/parser.py`.

2. Dans Copilot :

   > « Suis `copilot-instruction.md`. Génère `tests/test_parser.py` avec pytest. »

3. Demander :

   > « Liste les fonctions publiques + pré/post-conditions. »

**Critères de réussite**

* Docstrings présentes.
* ≥ 3 tests verts.
* Contrats explicites.

---

## **Exercice 5 : Hallucination buster**

**Description**
Détecter et corriger une invention de fonction/import par Copilot.

**Instructions**

1. Dans `main.py`, ajouter :

```py
# Exporter les résultats en CSV compressé
```

2. Si Copilot invente un fichier inexistant :

> « Cette fonction n’existe pas. Suis `copilot-instruction.md`.
> Crée le fichier et la fonction minimale + tests. »

**Critères de réussite**

* Pas de références fantômes.
* Import valide.
* Test OK.

---

## **Exercice 6 : Vigilance sécurité**

**Description**
Détecter du code dangereux et le corriger.

**Instructions**

1. Ouvrir `danger.py`.

2. Dans Copilot :

   > « Analyse les risques et propose un plan d’amélioration selon `copilot-instruction.md`. »

3. Valider modifications une par une.

**Critères de réussite**

* Suppression des pratiques dangereuses (`shell=True`, secrets en clair).
* Logs de sécurité ajoutés.

---

## **Exercice 7 : Migration/refactor multi-fichiers**

**Description**
Renommer un fichier et modifier tous les imports.

**Instructions**

1. Renommer manuellement :

   ```
   utils/parser.py → utils/response_parser.py
   ```
2. Dans Copilot :

   > « Selon `copilot-instruction.md`, mets à jour tous les imports et liste les fichiers impactés. Applique uniquement la modification n°1. »

**Critères de réussite**

* Aucun `ImportError`.
* Tests fonctionnels.

---

## **Exercice 8 : Revue finale du workspace**

**Description**
Faire une **checklist qualité** : lisibilité, logs, tests, sécurité.

**Instructions**

Dans le chat, à la racine :

> « Fais une revue globale du projet selon `copilot-instruction.md`. Propose un plan d’amélioration en 5 points. Applique uniquement le point n°1. »

**Critères de réussite**

* Plan priorisé.
* ≥ 2 quick wins appliqués.
* Projet stable & propre.

