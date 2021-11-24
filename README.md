# Webinaire: Comprendre les vues de django et flask en profondeur en comprenant WSGI

L'objectif de ce webinaire est de comprendre le fonctionnement d'une application 
web python en descendant au plus bas niveau d'abstraction offert par le langage, 
la spécification WSGI décrite dans la PEP 3333. Nous allons donc discuter d'une 
méthode indépendante du framework choisi pour permettre à un client http, comme 
un navigateur web, postman, curl/httpie, de communiquer avec une application hébergée 
sur un serveur.

La matière présentée dans ce webinaire n'a pas pour objectif de remplacer le travail 
réalisé sous le capot par des frameworks comme Flask, FastApi ou Django. L'objectif 
poursuivi est essentiellement pédagogique.

Pour creuser le sujet, je recommande les ressources suivante:

- Un tutoriel d'intérêt historique sur le fonctionnement de WSGI. C'est du python 2, mais facilement transposable: https://wsgi.tutorial.codepoint.net/
- Un cours payant, mais très instructif, sur comment se créer son propre framework web from scratch: https://testdriven.io/courses/python-web-framework/
- La PEP décrivant la spécification WSGI: https://www.python.org/dev/peps/pep-3333/