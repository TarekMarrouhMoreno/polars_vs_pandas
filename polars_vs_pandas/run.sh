pip install --no-cache-dir -r requirements.txt

python main.py

docker build -t codebase .

docker run codebase
