#!/bin/bash

#SBATCH --job-name=fasterCNN
#SBATCH --nodes=1                
#SBATCH --ntasks=1     
#SBATCH --cpus-per-task=4      
#SBATCH --mem=64G   
#SBATCH --partition=gtx1080    
#SBATCH --gres=gpu:2    
#SBATCH --time=2-00:00:00       
#SBATCH --output=fasterCNN%j.out   
#SBATCH --error=fasterCNN%j.err       
#SBATCH --exclusive

module load cuda/10.2           

python main.py                

echo "Training complete."
