Oui ❤️ Si le leader a déjà créé le repository GitHub et la branche, et que toi tu as déjà le code sur ton PC, voici l’ordre exact des commandes à retenir.

🧠 Le principe
GitHub
   ↓
clone / pull
   ↓
ta branche
   ↓
git add
   ↓
git commit
   ↓
git push
   ↓
GitHub
   ↓
Pull Request → leader
1️⃣ Première fois seulement : récupérer le projet

Si le projet n'est pas encore sur ton PC :

git clone URL_DU_REPOSITORY

Puis :

cd NOM_DU_PROJET
2️⃣ Vérifier les branches
git branch

Tu verras par exemple :

* main
  videlina

Le * indique la branche actuelle.

Pour voir aussi les branches GitHub :

git branch -a
3️⃣ Récupérer les dernières modifications du leader

Avant de commencer à travailler, fais :

git pull origin main

⚠️ Si le leader travaille sur une autre branche, remplace main par le nom de sa branche.

4️⃣ Aller dans TA branche

Si ta branche existe déjà :

git switch videlina

Puis, par sécurité :

git pull origin videlina

Si ta branche n'existe pas encore et tu dois la créer :

git switch -c videlina
5️⃣ Tu travailles sur ton code 💻

Tu modifies/crées tes fichiers.

Par exemple :

index.html
style.css
script.js
README.md
6️⃣ Vérifier ce que tu as modifié
git status

Tu peux voir :

modified: index.html
modified: style.css
7️⃣ Ajouter tes fichiers

Pour tous les fichiers modifiés :

git add .

Ou seulement un fichier :

git add index.html

Puis vérifie :

git status

Les fichiers devraient apparaître en vert.

git commit -m "Add my changes"

Par exemple :

git commit -m "Add login page"

Le commit = tu sauvegardes officiellement ton changement dans Git.

9️⃣ Envoyer ta branche sur GitHub
git push origin videlina

🎉 Maintenant ton code est sur GitHub, dans ta branche videlina.

10️⃣ Créer une Pull Request

Sur GitHub :

Your repository
      ↓
Pull requests
      ↓
New pull request

Choisis :

base: main
compare: videlina

Puis :

Create pull request

Le leader va vérifier ton code et pourra le merge dans main.

⭐ La séquence à mémoriser

Si tout est déjà configuré, ton quotidien sera principalement :

git switch videlina
git pull origin main

# tu travailles sur ton code

git status
git add .
git commit -m "Describe my changes"
git push origin videlina

Puis tu vas sur GitHub → Pull Request.

🔄 Et si le leader a fait des changements pendant que tu travaillais ?

Avant de pousser, récupère les changements du leader :

git switch videlina
git pull origin main

S'il y a des conflits, Git te le dira. Tu corriges les fichiers concernés, puis :

git add .
git commit -m "Resolve merge conflicts"
git push origin videlina
⚠️ Une chose très importante

Ne fais pas :

git push origin main

si vous travaillez en équipe et que main appartient au leader.

Toi, tu dois généralement faire :

git push origin TA_BRANCHE

Donc dans ton cas :

git push origin videlina

En résumé :

1. git pull
       ↓
2. git switch ta-branche
       ↓
3. tu codes
       ↓
4. git status
       ↓
5. git add .
       ↓
6. git commit -m "..."
       ↓
7. git push origin ta-branche
       ↓
8. Pull Request
       ↓
9. Leader vérifie
       ↓
10. Leader merge

C'est exactement le workflow que tu vas utiliser pour ton travail de groupe. ❤️