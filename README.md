**SafeYard - Detecção de Motocicletas**

Este projeto utiliza a Roboflow Inference Pipeline para detectar motocicletas
em tempo real usando webcam ou arquivos de vídeo. Ideal para soluções de 
monitoramento em estacionamentos, vias públicas ou ambientes industriais.

🚀 Funcionalidades
------------------------------------------------------------
✔ Processamento de vídeo em tempo real (Webcam ou Arquivo)
✔ Inferência com modelo Roboflow (object detection)
✔ Exibição visual das detecções com bounding boxes (OpenCV)
✔ Contagem automática de motocicletas detectadas
✔ Fácil configuração via API Key e Workflow ID

🧰 Pré-requisitos
------------------------------------------------------------
- Python 3.8 ou superior
- Roboflow Inference SDK
- OpenCV (cv2)
- Uma conta na Roboflow com projeto treinado

📦 Instalação
------------------------------------------------------------
pip install roboflow inference opencv-python
------------------------------------------------------------

🔧 Configuração
------------------------------------------------------------
Substitua os valores abaixo com suas credenciais da Roboflow:

API_KEY = "sua-api-key"
WORKSPACE = "seu-workspace"
WORKFLOW_ID = "seu-workflow-id"

🎬 Executando
------------------------------------------------------------
▶ Webcam:
    p_camera(API_KEY, WORKSPACE, WORKFLOW_ID, camera_id=0)

▶ Vídeo Local:
    video_path = "videos/exemplo.mp4"
    p_local(API_KEY, WORKSPACE, WORKFLOW_ID, video_path)

📊 Exemplo de Saída
------------------------------------------------------------
Motocicletas detectadas: 2
Motocicletas detectadas: 1
Motocicletas detectadas: 0

📌 Observações
------------------------------------------------------------
- O modelo da Roboflow deve conter a classe "motocicleta".
- Para melhor acurácia, use vídeos com boa iluminação.
- Pressione ESC para encerrar a janela do OpenCV.

📄 Licença
------------------------------------------------------------
Distribuído sob a licença MIT. Consulte LICENSE para mais detalhes.
