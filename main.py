from inference import InferencePipeline
import cv2

#Trata os resultados
def my_sink(result, video_frame):
    if result.get("output_image"):
        cv2.imshow("Imagem com detecções", result["output_image"].numpy_image)
        cv2.waitKey(1)

    motocicletas = [p for p in result["predictions"] if p["class_name"].lower() == "motocicleta"]
    print(f"Motocicletas detectadas: {len(motocicletas)}")


# Câmera/webcam
def p_camera(api_key, workspace_name, workflow_id, camera_id=0, max_fps=15):
    pipeline = InferencePipeline.init_with_workflow(
        api_key=api_key,
        workspace_name=workspace_name,
        workflow_id=workflow_id,
        video_reference=camera_id,
        max_fps=max_fps,
        on_prediction=my_sink
    )
    pipeline.start()
    pipeline.join()


# Vídeo local
def p_local(api_key, workspace_name, workflow_id, video_path, max_fps=15):
    pipeline = InferencePipeline.init_with_workflow(
        api_key=api_key,
        workspace_name=workspace_name,
        workflow_id=workflow_id,
        video_reference=video_path,
        max_fps=max_fps,
        on_prediction=my_sink
    )
    pipeline.start()
    pipeline.join()


# Roboflow
API_KEY = "zl2QCx0S5KqmkOzxvjJs"
WORKSPACE = "safeyard"
WORKFLOW_ID = "detect-count-and-visualize"


# Video Local
# video_local = "videos/exemplo.mp4"
# p_local(API_KEY, WORKSPACE, WORKFLOW_ID, video_local)

# Camera
p_camera(API_KEY, WORKSPACE, WORKFLOW_ID, camera_id=0)
