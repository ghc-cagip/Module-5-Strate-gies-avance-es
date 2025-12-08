# LIGNES DIRECTRICES OPÉRATIONNELLES POUR LES MODIFICATIONS DE COPILOT

## DIRECTIVE PRINCIPALE
    Répondre toujours en francais pour tes explications
	Des modifications simultanées multiples sur un fichier entraîneront une corruption.
	Discuter et expliquer ce que tu fais pendant le codage.
	Génére de Message de commit a chaque proposition

## PROTOCOLE POUR LES GRANDS FICHIERS ET LES MODIFICATIONS COMPLEXES

### PHASE DE PLANIFICATION OBLIGATOIRE
	Lorsque vous travaillez avec des fichiers volumineux (> 300 lignes) ou des modifications complexes :
		1. COMMENCEZ TOUJOURS par créer un plan détaillé AVANT d'effectuer des modifications
            2. Votre plan DOIT inclure :
                   - Toutes les fonctions/sections qui doivent être modifiées
                   - L'ordre dans lequel les modifications doivent être appliquées
                   - Les dépendances entre les modifications
                   - Le nombre estimé de modifications distinctes nécessaires
				
## PLAN DE MODIFICATION PROPOSÉ
	Travail sur : [nom du fichier]
	Nombre total de modifications prévues : [nombre]

### EFFECTUER LES MODIFICATIONS
	- Se concentrer sur un changement conceptuel à la fois
	- Montrer des extraits clairs « avant » et « après » lors de la proposition de modifications
	- Inclure des explications concises de ce qui a changé et pourquoi
	- Toujours vérifier si la modification maintient le style de codage du projet

### Séquence de modifications :
	1. [Première modification spécifique] - Objet : [pourquoi]
	2. [Deuxième modification spécifique] - Objet : [pourquoi]
	3. Approuvez-vous ce plan ? Je procéderai à la modification [numéro] après votre confirmation.
	4. ATTENDRE la confirmation explicite de l'utilisateur avant d'effectuer DES modifications lorsque l'utilisateur valide la modification [numéro]

### PHASE D'EXÉCUTION
	- Après chaque modification individuelle, indiquer clairement la progression :
		"✅ Modification [ # ] sur [total] terminée. Prêt pour la modification suivante ?"
	- Si vous découvrez des modifications supplémentaires nécessaires pendant la modification :
	- ARRÊTEZ-VOUS et mettez à jour le plan
	- Obtenez l'approbation avant de continuer

### ORIENTATIONS DE REFACTORING
	Lors du refactoring de fichiers volumineux :
	- Décomposer le travail en blocs logiques et fonctionnellement indépendants
	- S'assurer que chaque état intermédiaire maintient les fonctionnalités
	- Envisager la duplication temporaire comme une étape intermédiaire valide
	- Toujours indiquer le modèle de refactoring appliqué

### ÉVITEMENT DES LIMITES DE DÉBIT
	- Pour les très gros fichiers, il est conseillé de répartir les modifications sur plusieurs sessions
	- Prioriser les modifications qui constituent des unités logiques complètes
	- Toujours fournir des points d'arrêt clairs

## Exigences générales
	Utiliser les technologies modernes décrites ci-dessous pour toutes les suggestions de code. Privilégier un code propre et maintenable avec des commentaires appropriés.

## Exigences JavaScript/TypeScript
	- **Style de codage **: Suivre les conventions de style populaires (par exemple, Airbnb, Google) pour la lisibilité et la cohérence.
	- **Linter/Formatter **: Utiliser ESLint avec des règles strictes et Prettier pour le formatage automatique.
	- **Modules **: Utiliser les modules ES (import/export) au lieu de CommonJS.
	- **Gestion des dépendances **: Utiliser npm ou yarn pour la gestion des packages
	- **Compatibilité minimale **: ECMAScript 2020 (ES11) ou supérieure
	- **Fonctionnalités à utiliser **:
	- Fonctions fléchées
	- Littéraux de gabarit
	- Affectation de déstructuration
	- Opérateurs de propagation/de repos
	- Async/await pour le code asynchrone
	- Classes avec héritage approprié lorsque la POO est nécessaire
	- Notation abrégée des objets
	- Chaînage facultatif (`?.`)
	- Fusion nulle (`??`)
	- Imports dynamiques
	- BigInt pour les grands entiers
	- `Promise.allSettled()`
	- `String.prototype.matchAll()`
	- Objet `globalThis` 
	- Champs et méthodes de classe privés
	- Syntaxe d'exportation * comme espace de noms
	- Méthodes de tableau (`map`, `filter`, `reduce`, `flatMap`, etc.)
	- **À éviter **:
	- Mot clé `var` (utiliser `const` et `let`)
	- jQuery ou toute bibliothèque externe
	- Modèles asynchrones basés sur des rappels lorsque les promesses peuvent être utilisées
	- Compatibilité Internet Explorer
	- Formats de modules hérités (utiliser les modules ES)
	- Limiter l'utilisation de `eval()` en raison des risques de sécurité
	- **Considérations relatives aux performances **:
	- Recommander le fractionnement du code et les imports dynamiques pour le chargement différé
	**Gestion des erreurs **:
	- Utiliser les blocs `try-catch` **de manière cohérente** pour les appels asynchrones et les appels d'API, et gérer explicitement les rejets de promesses.
	- Faire la distinction entre :
	- **Erreurs réseau** (par exemple, délais d'attente, erreurs serveur, limitation de débit)
	- **Erreurs de logique fonctionnelle/métier** (faux pas logiques, entrée utilisateur non valide, échecs de validation)
	- **Exceptions d'exécution** (erreurs inattendues telles que les références nulles)
	- Fournir des messages d'erreur **conviviaux** (par exemple, « Une erreur s'est produite. Veuillez réessayer ultérieurement. ») et consigner des détails plus techniques aux développeurs/opérations (par exemple, via un service de journalisation).
	- Envisager une fonction de gestionnaire d'erreurs centralisée ou un événement global (par exemple, `window.addEventListener('unhandledrejection')`) pour consolider les rapports.

## Exigences Python
    - Documentation : Ajouter des DocStrings (Python) et en anglais.
	- Style de codage : Suivre PEP 8 pour la lisibilité et la cohérence.
	- Typage : Utiliser des annotations de type (Python) pour la clarté.
	- Gestion des dépendances : Utiliser pip et virtualenv/venv pour la gestion des packages.
	- Compatibilité minimale : Python 3.8 ou supérieure.
	- Fonctionnalités à utiliser :
	- Compréhensions de liste, de dictionnaire et d'ensemble
	- F-strings pour le formatage des chaînes
	- Gestionnaire de contexte (`with` statement)

## Exigences Ansible
	- Tous les noms de tâches sont explicites et en anglais.
	- Les messages d’erreur et de succès sont professionnels et visuels (✅/❌) et en anglais.
	- Les sections sont bien séparées et documentées en anglais.
	- Utiliser des rôles Ansible pour organiser les tâches réutilisables.
	- Utiliser des variables et des fichiers de configuration pour gérer les paramètres.
	- Utiliser des boucles et des conditions pour éviter la duplication de code.
	- Utiliser des modules Ansible intégrés au lieu de commandes shell lorsque cela est possible
	- Utiliser des gestionnaires pour les actions déclenchées par des changements d'état.
	- Utiliser des balises pour permettre l'exécution sélective de parties du playbook.

## Considérations de sécurité
	- Nettoyer soigneusement toutes les entrées utilisateur.
	- Paramétrer les requêtes de base de données.
	- Appliquer des politiques de sécurité de contenu (CSP) strictes.
	- Utiliser la protection CSRF le cas échéant.
	- Garantir des cookies sécurisés (`HttpOnly`, `Secure`, `SameSite=Strict`).
	- Limiter les privilèges et appliquer le contrôle d'accès basé sur les rôles.
	- Mettre en œuvre une journalisation et une surveillance internes détaillées.