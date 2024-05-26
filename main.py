import os
import sys
import subprocess

HOME = os.getcwd()
path = os.path.join(HOME, 'TrainFasterRCNN')
data = os.path.join(path, 'data_configs', 'acne.yaml')

print(HOME)
os.chdir(path)

"""## Train model"""
subprocess.run([sys.executable, 'train.py','--model', 'fasterrcnn_resnet50_fpn', '--disable-wandb','--epochs', '150', '--batch', '8', '--imgsz', '800', '--lr', '0.0009', '--data', data, '--name', 'fasterRCNN_acne'])


"""## Validating model"""

os.chdir(path)

subprocess.run([sys.executable, 'eval.py', '--model', 'fasterrcnn_resnet50_fpn', '--weights', 'outputs/training/fasterRCNN_acne/best_model.pth', '--data', data])

