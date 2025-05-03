from ultralytics import YOLO
import cv2

# Carrega o modelo treinado
modelo = YOLO("modelo/best.pt")  # Substitua com o caminho correto

# Leitura da imagem ou vídeo
imagem = cv2.imread("imagens/rua_com_motos.jpg")  # Ou vídeo/câmera

# Roda a detecção
resultados = modelo(imagem)[0]

# Contador de motocicletas
contador = 0

# Itera sobre detecções
for box in resultados.boxes:
    classe_id = int(box.cls[0])
    label = modelo.names[classe_id]
    if label.lower() == "motocicleta":  # nome da classe usada no Roboflow
        contador += 1
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0].item()
        cv2.rectangle(imagem, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(imagem, f"{label} {conf:.2f}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

# Mostrar resultado
cv2.putText(imagem, f"Total motocicletas: {contador}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Deteccao", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
