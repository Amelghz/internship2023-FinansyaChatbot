privateGPT
Posez des questions à vos documents sans connexion Internet, en utilisant la puissance des LLM. 100% privé, aucune donnée ne quitte votre environnement d'exécution à tout moment. Vous pouvez ingérer des documents et poser des questions sans connexion Internet!

Construit avec LangChain, GPT4All, LlamaCpp, Chroma et SentenceTransformers.

Créez deux dossiers : le premier nommé "source_documents", contenant tous les fichiers nécessaires, et le deuxième nommé "models", contenant le modèle téléchargé depuis Hugging Face (https://huggingface.co/eachadea/ggml-vicuna-13b-1.1/blob/main/ggml-vic13b-q5_1.bin).


Configuration de l'environnement
 
python3 -m venv myenv
source myenv/bin/activate (linux)
myenv/bin/activate    (windows)



Afin de configurer votre environnement pour exécuter le code ici, installez d'abord toutes les exigences:

pip3 install -r requirements.txt


Ensuite, téléchargez le modèle LLM et placez-le dans un répertoire de votre choix:

LLM: par défaut à ggml-gpt4all-j-v1.3-groovy.bin. Si vous préférez un modèle compatible GPT4All-J différent, téléchargez-le et référençons-le dans votre .env fichier.


et modifier les variables de manière appropriée dans le .env fichier.

MODEL_TYPE: supports LlamaCpp or GPT4All
PERSIST_DIRECTORY: is the folder you want your vectorstore in
MODEL_PATH: Path to your GPT4All or LlamaCpp supported LLM
MODEL_N_CTX: Maximum token limit for the LLM model
MODEL_N_BATCH: Number of tokens in the prompt that are fed into the model at a time. Optimal value differs a lot depending on the model (8 works well for GPT4All, and 1024 is better for LlamaCpp)
EMBEDDINGS_MODEL_NAME: SentenceTransformers embeddings model name (see https://www.sbert.net/docs/pretrained_models.html)
TARGET_SOURCE_CHUNKS: The amount of chunks (sources) that will be used to answer a question


Remarque: à cause du chemin langchain charge le SentenceTransformers embeddings, la première fois que vous exécutez le script, il faudra une connexion Internet pour télécharger le modèle d'embeddings lui-même.


Jeu de données de test:
Ce repo utilise les données de Finansya.

Instructions pour l'ingestion de votre propre ensemble de données
Mettez tous vos fichiers dans le source_documents répertoire

Les extensions prises en charge sont:

.csv: CSV,
.docx: Document Word,
.doc: Document Word,
.enex: EverNote,
.eml: Email,
.epub: EPub,
.html: Fichier HTML,
.md: Markdown,
.msg: Message Outlook,
.odt: Ouvrir le texte du document,
.pdf: Format de document portable ( PDF ),
.pptx: Document PowerPoint,
.ppt: Document PowerPoint,
.txt: Fichier texte ( UTF-8 ),
Exécutez la commande suivante pour ingérer toutes les données.

python ingest.py

La sortie devrait ressembler à ceci:
Creating new vectorstore
Loading documents from source_documents
Loading new documents: 100%|██████████████████████| 1/1 [00:01<00:00,  1.73s/it]
Loaded 1 new documents from source_documents
Split into 90 chunks of text (max. 500 tokens each)
Creating embeddings. May take some minutes...
Using embedded DuckDB with persistence: data will be stored in: db
Ingestion complete! You can now run privateGPT.py to query your documents

Il créera un db dossier contenant le magasin de vecteurs local. Prendra 20 à 30 secondes par document, selon la taille du document. Vous pouvez ingérer autant de documents que vous le souhaitez et tout sera accumulé dans la base de données des intégrations locales. Si vous souhaitez démarrer à partir d'une base de données vide, supprimez le db dossier.

Remarque: pendant le processus d'ingestion, aucune donnée ne quitte votre environnement local. Vous pouvez ingérer sans connexion Internet, sauf pour la première fois que vous exécutez le script d'ingestion, lorsque le modèle d'intégration est téléchargé.

Posez des questions à vos documents, localement!
Pour poser une question, exécutez une commande comme:
export FLASK_APP=app.py (linux)
set FLASK_APP=app.py (windows)
python app.py



Comment ça marche?
Sélection des bons modèles locaux et de la puissance de LangChain vous pouvez exécuter l'ensemble du pipeline localement, sans que les données quittent votre environnement et avec des performances raisonnables.

ingest.py utilise LangChain des outils pour analyser le document et créer des intégrations localement en utilisant HuggingFaceEmbeddings (SentenceTransformers). Il stocke ensuite le résultat dans une base de données vectorielle locale à l'aide Chroma magasin de vecteurs.
privateGPT.py utilise un LLM local basé sur GPT4All-J ou LlamaCpp comprendre les questions et créer des réponses. Le contexte des réponses est extrait de la boutique vectorielle locale à l'aide d'une recherche de similitude pour localiser le bon contexte à partir des documents.
GPT4All-Jwrapper a été introduit dans LangChain 0.0.162.


Exigences système:
Version Python
Pour utiliser ce logiciel, vous devez avoir installé Python 3.10 ou une version ultérieure. Les versions antérieures de Python ne se compileront pas.

flask:
pour installer flask pip install flask

Compilateur C + +
Si vous rencontrez une erreur lors de la construction d'une roue pendant la pip install traiter, vous devrez peut-être installer un compilateur C + + sur votre ordinateur.

Pour Windows 10/11
Pour installer un compilateur C + + sur Windows 10/11, procédez comme suit:

Installez Visual Studio 2022.
Assurez-vous que les composants suivants sont sélectionnés:
Développement de plate-forme Windows universelle
C + + Outils CMake pour Windows
Téléchargez le programme d'installation MinGW à partir du Site Web de MinGW.
Exécutez le programme d'installation et sélectionnez le gcc composant.


![chatbot_1](https://github.com/Amelghz/internship2023-FinansyaChatbot/assets/92169711/cde1863e-2e58-43f6-b116-b48cd69c96d1)

![chatbot_2](https://github.com/Amelghz/internship2023-FinansyaChatbot/assets/92169711/b1470bd3-f647-43fb-bc16-bfa075f95802)


![chatbot_3png](https://github.com/Amelghz/internship2023-FinansyaChatbot/assets/92169711/57c919f7-32f4-46c7-b8bd-6cdf96886df7)


![chatbot_4](https://github.com/Amelghz/internship2023-FinansyaChatbot/assets/92169711/8c951444-1d89-4334-a02f-fc0a023f8baf)


![chatbot_5](https://github.com/Amelghz/internship2023-FinansyaChatbot/assets/92169711/e71ebc2a-53a4-46e9-abd3-7dabfa8fa858)



Remarque:
La capacité de RAM et de CPU ou GPU requise pour le modèle eachadea/ggml-vicuna-13b-1.1 varie en fonction de l'utilisation que vous en faites. Pour une utilisation légère, comme la génération de texte de base, vous pouvez vous en sortir avec 16 Go de RAM et un processeur Intel Core i5 ou équivalent.
Il est important de noter que ces sont des exigences minimales. 
