from generate import generate
from network import network_model
from train import train
from utils import create_music,get_notes

if __name__ == '__main__':
  fire.Fire({
      'generate':generate,
      'network_model':network_model,
      'train':train,
      'create_music':create_music,
      'get_notes':get_notes,
  })