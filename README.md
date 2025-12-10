# **Lab Module 5 — Stratégies avancées (avec utilisation obligatoire de `copilot-instruction.md`)**

> Pour chaque exercice :
> **Vous devez utiliser le fichier `copilot-instruction.md` comme protocole de travail.**
>
> Cela signifie que, AVANT que Copilot modifie un fichier, vous devez lui demander :
>
> de produire un **plan de modification**
> d’annoncer le **nombre de modifications**
> de n’appliquer qu’**une modification à la fois** en attendant votre validation
> d’expliquer ce qu’il change et pourquoi

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

   > « Selon `copilot-instruction.md`, propose un plan détaillé avant de <à compter> »

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

 <à compter>

**Critères de réussite**

* Logs JSON uniformes.
* Pas de duplication de config.
* Imports corrects.

---

## **Exercice 3 : Explication & review de code par Copilot**

**Description**
Faire analyser le projet et obtenir des suggestions d’amélioration.
1- Expliquer l’architecture du projet en 5 points.
2- Proposer un plan de refactor léger.

**Instructions**

 <à compter>

**Critères de réussite**

* Explication courte.
* ≥ 2 améliorations intégrées.
* Diffs clairs.

---

## **Exercice 4 : Dépendances & contrat inter-modules**

**Description**
Rendre explicite le contrat entre fichiers via docstrings + tests.

**Instructions**

 <à compter>

**Critères de réussite**

* Docstrings présentes.
* ≥ 3 tests verts.
* Contrats explicites.

---

## **Exercice 5 : Hallucination buster**

**Description**
Détecter et corriger une invention de fonction/import par Copilot.
```py
# Exporter les résultats en CSV compressé
```

**Instructions**

 <à compter>

**Critères de réussite**

* Pas de références fantômes.
* Import valide.
* Test OK.

---

## **Exercice 6 : Vigilance sécurité**

**Description**
Détecter du code dangereux et le corriger.

1- Ouvrir `danger.py`.

**Instructions**

<à compter>

**Critères de réussite**

* Suppression des pratiques dangereuses (`shell=True`, secrets en clair).
* Logs de sécurité ajoutés.

---

## **Exercice 7 : Migration/refactor multi-fichiers**

**Description**
Renommer un fichier et modifier tous les imports.

Renommer manuellement :

   ```
   utils/parser.py → utils/response_parser.py
   ```
2. Dans Copil

**Instructions**

 <à compter> 

**Critères de réussite**

* Aucun `ImportError`.
* Tests fonctionnels.

---

## **Exercice 8 : Revue finale du workspace**

**Description**
Faire une **checklist qualité** : lisibilité, logs, tests, sécurité.

**Instructions**

 «<à compter> »

**Critères de réussite**

* Plan priorisé.
* ≥ 2 quick wins appliqués.
* Projet stable & propre.

