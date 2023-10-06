import hydra
from omegaconf import DictConfig

@hydra.main(config_path="./cfg", config_name="config")
def main(cfg: DictConfig):
    while True:
        print(cfg)
    

if __name__=="__main__":
    main()