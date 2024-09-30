import sys
import os

# Adicione o caminho do projeto ao sys.path
sys.path.insert(0, '/home/magrelinho/comoEstamos')

from app import app as application

if __name__ == "__main__":
   application.run()
