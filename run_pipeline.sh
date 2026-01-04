#!/bin/bash
set -e

echo ""
echo "Starting full pipeline execution..."
echo ""

# --- STEP 0: GPU Setup ---
#./setup_gpu_support.sh

## --- STEP 1: Point Cloud Initialization ---
#echo ""
#echo "[1/6] Point Cloud Initialization"
#docker compose run --rm point-cloud-init
#
## --- STEP 2: Semantic Segmentation Preprocessing ---
#echo ""
#echo "[2/6] Scene Semantic Segmentation Preprocessing"
#docker compose run --rm scene-semantic-segmentation-preprocessing
#
## --- STEP 3: Semantic Segmentation (GPU) ---
#echo ""
#echo "[3/6] Scene Semantic Segmentation"
#docker compose run --rm scene-semantic-segmentation
#
## --- STEP 4: Scene Interest Points Extraction ---
#echo ""
#echo "[4/6] Scene Interest Points Extraction"
#docker compose run --rm scene-interest-points-extraction

## --- STEP 5: Pose Classification (GPU) ---
echo ""
echo "[5/6] Pose Classification"
docker compose run --rm pose-classification

## --- STEP 6: Action Recognition ---
#echo ""
#echo "[6/6] Action Recognition"
#docker compose run --rm action-recognition
#
#echo ""
#echo "Pipeline completed successfully."