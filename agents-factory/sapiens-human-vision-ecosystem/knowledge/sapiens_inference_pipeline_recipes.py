"""
Sapiens Human Vision Inference Recipes (Sapiens-Lite Production Engine)
Autor: Leonel Salcedo / Nomack Studio & Antigravity

Soporta inferencia modular para las 4 tareas de Meta Sapiens:
1. Pose Estimation (308 keypoints)
2. Body-Part Segmentation (28 classes)
3. Depth Estimation (1024x1024 metric/relative)
4. Surface Normal Estimation (1024x1024 3D vectors)
"""

import os
import cv2
import numpy as np
import torch
from typing import Dict, Any, Tuple, Optional

class SapiensPipeline:
    def __init__(self, model_path: str, task: str = "normal", device: str = "cuda", dtype: torch.dtype = torch.bfloat16):
        self.device = torch.device(device if torch.cuda.is_available() else "cpu")
        self.dtype = dtype if self.device.type == "cuda" else torch.float32
        self.task = task.lower()
        
        print(f"[Sapiens] Cargando modelo {self.task} desde: {model_path} en {self.device}...")
        self.model = torch.jit.load(model_path, map_location=self.device)
        self.model.eval()
        
        self.mean = torch.tensor([0.485, 0.456, 0.406], device=self.device).view(1, 3, 1, 1)
        self.std = torch.tensor([0.229, 0.224, 0.225], device=self.device).view(1, 3, 1, 1)

    def preprocess(self, image_bgr: np.ndarray) -> Tuple[torch.Tensor, Tuple[int, int]]:
        orig_h, orig_w = image_bgr.shape[:2]
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        resized = cv2.resize(image_rgb, (1024, 1024), interpolation=cv2.INTER_LINEAR)
        
        tensor = torch.from_numpy(resized).permute(2, 0, 1).unsqueeze(0).float() / 255.0
        tensor = tensor.to(self.device)
        normalized = ((tensor - self.mean) / self.std).to(self.dtype)
        
        return normalized, (orig_w, orig_h)

    def infer_normals(self, image_bgr: np.ndarray) -> np.ndarray:
        tensor, (orig_w, orig_h) = self.preprocess(image_bgr)
        
        with torch.inference_mode():
            output = self.model(tensor)
            
        normals = output[0].float().cpu().numpy().transpose(1, 2, 0)
        # Normalizar a rango [0, 255]
        norm = np.linalg.norm(normals, axis=-1, keepdims=True)
        normals = normals / (norm + 1e-6)
        normal_rgb = ((normals + 1.0) * 0.5 * 255.0).clip(0, 255).astype(np.uint8)
        
        return cv2.resize(normal_rgb, (orig_w, orig_h), interpolation=cv2.INTER_LINEAR)

    def infer_depth(self, image_bgr: np.ndarray) -> np.ndarray:
        tensor, (orig_w, orig_h) = self.preprocess(image_bgr)
        
        with torch.inference_mode():
            output = self.model(tensor)
            
        depth = output[0, 0].float().cpu().numpy()
        # Normalizar profundidad para visualización
        depth_min, depth_max = depth.min(), depth.max()
        depth_norm = ((depth - depth_min) / (depth_max - depth_min + 1e-6) * 255.0).astype(np.uint8)
        
        return cv2.resize(depth_norm, (orig_w, orig_h), interpolation=cv2.INTER_LINEAR)

    def infer_segmentation(self, image_bgr: np.ndarray) -> np.ndarray:
        tensor, (orig_w, orig_h) = self.preprocess(image_bgr)
        
        with torch.inference_mode():
            output = self.model(tensor)
            
        seg_mask = torch.argmax(output[0], dim=0).cpu().numpy().astype(np.uint8)
        return cv2.resize(seg_mask, (orig_w, orig_h), interpolation=cv2.INTER_NEAREST)

    def infer_pose(self, image_bgr: np.ndarray) -> np.ndarray:
        tensor, (orig_w, orig_h) = self.preprocess(image_bgr)
        
        with torch.inference_mode():
            output = self.model(tensor)
            
        # 308 keypoints heatmaps -> argmax / coords
        heatmaps = output[0].float().cpu().numpy() # [308, 256, 256]
        keypoints = []
        for k in range(heatmaps.shape[0]):
            hm = heatmaps[k]
            y, x = np.unravel_index(np.argmax(hm), hm.shape)
            conf = float(hm[y, x])
            kx = (x / hm.shape[1]) * orig_w
            ky = (y / hm.shape[0]) * orig_h
            keypoints.append([kx, ky, conf])
            
        return np.array(keypoints, dtype=np.float32)

if __name__ == "__main__":
    print("[Sapiens] Módulo de recetas de inferencia listo para ejecución.")
