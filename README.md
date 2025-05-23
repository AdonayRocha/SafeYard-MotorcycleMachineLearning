
SafeYard - Detecção de Motocicletas 🏍️
=======================================

Este projeto detecta motocicletas em tempo real usando Roboflow e OpenCV.

Requisitos
----------
- Python 3.7+
- inference (Roboflow SDK)
- opencv-python

Instalação
----------
1. Clone o repositório:
   git clone https://github.com/seu-usuario/safeyard-detection.git
   cd safeyard-detection

2. Instale as dependências:
   pip install inference opencv-python

Configuração
------------
Edite no código:
- API_KEY = "sua_chave"
- WORKSPACE = "seu_workspace"
- WORKFLOW_ID = "seu_workflow"

Uso
---
Para usar com webcam:
    p_camera(API_KEY, WORKSPACE, WORKFLOW_ID)

Para usar com vídeo local:
    p_local(API_KEY, WORKSPACE, WORKFLOW_ID, "videos/video.mp4")

Funcionamento
-------------
- Mostra imagem com detecções (OpenCV)
- Conta motocicletas detectadas no console

Autor
-----
Projeto SafeYard
